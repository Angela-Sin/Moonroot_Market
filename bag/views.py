from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from django.contrib import messages
from django.views.decorators.http import require_POST


def view_bag(request):
    """A view to allow the user to see the contents of their bag"""

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """Add a specified quantity of an item to the bag in the session"""
    
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    product = get_object_or_404(Product, pk=item_id)
    
    bag = request.session.get('bag', {})

    if item_id in bag:
        bag[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}.')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag.')

    request.session['bag'] = bag
    
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """Remove an item from the shopping bag"""
    
    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})
    item_id = str(item_id)

    if item_id in bag:
        del bag[item_id]
        messages.warning(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    
    return redirect('bag:view_bag')


@require_POST
def update_bag(request, item_id):
    """Update quantity of the specified item in the shopping bag"""
    action = request.POST.get('action')
    bag = request.session.get('bag', {})
    item_id = str(item_id)
    product = get_object_or_404(Product, pk=item_id)

    if item_id in bag:
        if action == 'increase':
            bag[item_id] += 1
            messages.success(request, f'Increased {product.name} to {bag[item_id]}')
        elif action == 'decrease':
            if bag[item_id] > 1:
                bag[item_id] -= 1
                messages.success(request, f'Decreased {product.name} to {bag[item_id]}')
            else:
                del bag[item_id]
                messages.warning(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect('bag:view_bag')