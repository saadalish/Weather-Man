from django.core.paginator import Paginator
from django.shortcuts import render

from products.models import Product


def index(request):
    products = Product.objects.all()
    paginator = Paginator(products, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'products': products, 'page_obj': page_obj}
    return render(request, 'products/index.html', context)
