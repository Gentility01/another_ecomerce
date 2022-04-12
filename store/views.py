from django.shortcuts import get_object_or_404, render

from .models import Category, Product

# Create your views here.



def all_product(request):
    # products = Product.objects.filter(in_active=True)
    products = Product.products.all()
    
    context = {
        'products':products,
    }
    return render(request, 'store/home.html', context )


def product_detail(request, slug):
    products = get_object_or_404(Product, slug=slug, in_stalk=True)
    # products = Product.objects.get(slug=slug, in_stalk=True)
    context = {
        'product':products
    }
    return render(request, 'store/product_detail.html', context)


def category_details(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    context = {
        'category':category,
        'products':products
    }
    return render(request, 'store/category_details.html',context)
    