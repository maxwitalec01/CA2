from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.views.generic import ListView, DetailView

# Create your views here.
class ProdCat(ListView):
    model = Product

    def get(self, request, category_id=None):
        category= None
        products = None
        if category_id != None:
            category = get_object_or_404(Category, id = category_id)
            products = Product.objects.filter(category = category, available = True)
        else:
            products = Product.objects.all().filter(available = True)
                
        return render(request, "shop/category.html",{'category':category, 'products':products})

class ProdDetail(DetailView):
    model = Product

    def get(self, request, category_id, product_id):
        try:
            product = Product.objects.get(category_id = category_id, id = product_id)
        except Exception as e:
            raise e
        return render(request, 'shop/product.html', {'product':product})