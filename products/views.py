from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Category
from django.contrib import messages
from django.db.models import Q


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
   
    context = {
        'products': products,
        'search_term': query,
        'categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)