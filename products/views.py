from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Category
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .forms import ProductForm
from django.db.models.functions import Lower


def all_products(request):
    """ A view to show all products, including sorting and search queries """
    products = Product.objects.all()
    categories = Category.objects.all()
    query = request.GET.get('q', None)

    if 'q' in request.GET:
        query = request.GET['q']
        if not query.strip():
            messages.error(request, "You didn't enter any search criteria!")
            context = {
                'products': Product.objects.all(),
                'search_term': None,
            }

            return redirect(reverse('products'))
          
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)

    if 'category' in request.GET:
        selected_category = request.GET['category']
        products = products.filter(category__slug=selected_category)

    sort = request.GET.get('sort', 'name_asc')

    if sort == 'name_asc':
        products = products.order_by(Lower('name'))
    elif sort == 'name_desc':
        products = products.order_by(Lower('name').desc())
    elif sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    elif sort == 'rating_desc':
        products = products.order_by('-rates')
    else:
        
        products = products.order_by('name')
   
    context = {
        'products': products,
        'search_term': query,
        'product_categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.'
            )
    else:
        form = ProductForm()

    for field_name, field in form.fields.items():
        existing_classes = field.widget.attrs.get('class', '')
        field.widget.attrs['class'] = (existing_classes + ' form-control').strip()

    template = 'products/add_edit_product.html'
    context = {
        'form': form,
        'action': 'Add',
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.'
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    for field_name, field in form.fields.items():
        existing_classes = field.widget.attrs.get('class', '')
        field.widget.attrs['class'] = (existing_classes + ' form-control').strip()

    template = 'products/add_edit_product.html'
    context = {
        'form': form,
        'product': product,
        'action': 'Edit',
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))