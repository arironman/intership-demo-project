from django.shortcuts import render

from User.utils import paginator_stuff
from Product.models import Product
from Product.forms import ProductForm

# Create your views here.
def product(request):
    '''
        handling the product both get and post request
    '''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid(): 
            product_obj = form.save()


    products = Product.objects.all()

    # paginator code
    page_number = request.GET.get('page')
    count = 4
    products = paginator_stuff(products, page_number, count)

    product_form = ProductForm()

    # we are rendering the products as post in template to use the same pagintor template
    params = {
        'posts': products,
        'title': 'Product',
        'product_form':product_form
    }
    return render(request, 'product/product.html', params)
