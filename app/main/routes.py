# from flask import render_template, flash, redirect, url_for, request, current_app
# from flask_login import current_user, login_required
# from app import db
# from app.main import bp
# from app.main.forms import ItemForm, SwapRequestForm
# from app.models import User, Item, Swap, ItemImage
# from werkzeug.utils import secure_filename
# import os

# @bp.route('/')
# @bp.route('/index')
# def index():
#     featured_items = Item.query.filter_by(is_approved=True, is_available=True).order_by(Item.timestamp.desc()).limit(5).all()
#     return render_template('index.html', featured_items=featured_items)

# @bp.route('/dashboard')
# @login_required
# def dashboard():
#     user_items = current_user.items.order_by(Item.timestamp.desc()).all()
#     pending_swaps = current_user.swaps_received.filter_by(status='pending').all()
#     completed_swaps = current_user.swaps_received.filter(Swap.status.in_(['accepted', 'completed'])).all()
#     return render_template('dashboard.html', 
#                          items=user_items, 
#                          pending_swaps=pending_swaps,
#                          completed_swaps=completed_swaps)

# @bp.route('/items')
# def items():
#     page = request.args.get('page', 1, type=int)
#     items = Item.query.filter_by(is_approved=True, is_available=True).order_by(Item.timestamp.desc()).paginate(
#         page, current_app.config['ITEMS_PER_PAGE'], False)
#     next_url = url_for('main.items', page=items.next_num) if items.has_next else None
#     prev_url = url_for('main.items', page=items.prev_num) if items.has_prev else None
#     return render_template('items/list.html', items=items.items, next_url=next_url, prev_url=prev_url)

# @bp.route('/item/<int:id>', methods=['GET', 'POST'])
# def item_detail(id):
#     item = Item.query.get_or_404(id)
#     form = SwapRequestForm()
#     if form.validate_on_submit() and current_user.is_authenticated:
#         if form.swap_type.data == 'points':
#             swap = Swap(requester_id=current_user.id,
#                         item_owner_id=item.user_id,
#                         item_id=item.id,
#                         is_points_swap=True,
#                         points_offered=form.points_offered.data,
#                         message=form.message.data)
#         else:
#             swap = Swap(requester_id=current_user.id,
#                         item_owner_id=item.user_id,
#                         item_id=item.id,
#                         message=form.message.data)
#         db.session.add(swap)
#         db.session.commit()
#         flash('Your swap request has been sent!')
#         return redirect(url_for('main.dashboard'))
#     return render_template('items/detail.html', item=item, form=form)

# @bp.route('/add_item', methods=['GET', 'POST'])
# @login_required
# def add_item():
#     form = ItemForm()
#     if form.validate_on_submit():
#         item = Item(title=form.title.data,
#                     description=form.description.data,
#                     category=form.category.data,
#                     item_type=form.item_type.data,
#                     size=form.size.data,
#                     condition=form.condition.data,
#                     points_value=form.points_value.data,
#                     user_id=current_user.id)
        
#         db.session.add(item)
#         db.session.commit()
        
#         # Handle file uploads
#         for file in form.images.data:
#             if file:
#                 filename = secure_filename(file.filename)
#                 file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
#                 file.save(file_path)
                
#                 image = ItemImage(filename=filename, item_id=item.id)
#                 db.session.add(image)
        
#         db.session.commit()
#         flash('Your item has been submitted for approval!')
#         return redirect(url_for('main.dashboard'))
#     return render_template('items/add.html', form=form)

# @bp.route('/admin/dashboard')
# @login_required
# def admin_dashboard():
#     if not current_user.is_admin:
#         return redirect(url_for('main.index'))
    
#     pending_items = Item.query.filter_by(is_approved=False).all()
#     reported_items = []  # Would be populated from a reporting system
#     return render_template('admin/dashboard.html', 
#                          pending_items=pending_items, 
#                          reported_items=reported_items)

# @bp.route('/admin/approve_item/<int:id>')
# @login_required
# def approve_item(id):
#     if not current_user.is_admin:
#         return redirect(url_for('main.index'))
    
#     item = Item.query.get_or_404(id)
#     item.is_approved = True
#     db.session.commit()
#     flash('Item has been approved!')
#     return redirect(url_for('main.admin_dashboard'))

# @bp.route('/admin/reject_item/<int:id>')
# @login_required
# def reject_item(id):
#     if not current_user.is_admin:
#         return redirect(url_for('main.index'))
    
#     item = Item.query.get_or_404(id)
#     db.session.delete(item)
#     db.session.commit()
#     flash('Item has been rejected and removed.')
#     return redirect(url_for('main.admin_dashboard'))

# @bp.route('/swap/accept/<int:id>')
# @login_required
# def accept_swap(id):
#     swap = Swap.query.get_or_404(id)
#     if swap.item_owner_id != current_user.id:
#         return redirect(url_for('main.index'))
    
#     swap.status = 'accepted'
    
#     if swap.is_points_swap:
#         # Transfer points
#         requester = User.query.get(swap.requester_id)
#         owner = User.query.get(swap.item_owner_id)
        
#         if requester.points >= swap.points_offered:
#             requester.points -= swap.points_offered
#             owner.points += swap.points_offered
#         else:
#             flash('Requester does not have enough points!')
#             return redirect(url_for('main.dashboard'))
    
#     # Mark item as unavailable
#     item = Item.query.get(swap.item_id)
#     item.is_available = False
    
#     db.session.commit()
#     flash('Swap accepted!')
#     return redirect(url_for('main.dashboard'))

# @bp.route('/swap/reject/<int:id>')
# @login_required
# def reject_swap(id):
#     swap = Swap.query.get_or_404(id)
#     if swap.item_owner_id != current_user.id:
#         return redirect(url_for('main.index'))
    
#     swap.status = 'rejected'
#     db.session.commit()
#     flash('Swap rejected.')
#     return redirect(url_for('main.dashboard'))

# @bp.route('/swap/complete/<int:id>')
# @login_required
# def complete_swap(id):
#     swap = Swap.query.get_or_404(id)
#     if swap.item_owner_id != current_user.id and swap.requester_id != current_user.id:
#         return redirect(url_for('main.index'))
    
#     swap.status = 'completed'
#     db.session.commit()
#     flash('Swap marked as completed!')
#     return redirect(url_for('main.dashboard'))