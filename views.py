from django.views import generic

from products.models import Product


class IndexView(generic.ListView):
    model = Product
    paginate_by = 50
    template_name = 'products/index.html'
    context_object_name = 'products'
