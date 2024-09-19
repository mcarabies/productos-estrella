from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product

# PAGINA DE INICIO
def home(req):
    featured_product = Product.objects.first()
    print(featured_product)
    products_page = Paginator(Product.objects.filter(published=True), 5)
    page = req.GET.get('page')
    products = products_page.get_page(page)
    
    context = {
        'products': products,
        'featured_product': featured_product
    }
    return render(req, 'core/home.html', context)

# PACINA DE RESEÑA DEL PRODUCTO
def review(req):
    return render(req, 'core/review.html')


# PAGINA DE CATEGORIA INDIVIDUAL
def category (req):
    return render(req, 'core/home.html')