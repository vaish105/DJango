from django.shortcuts import render
from .models import Product
from .forms import ProductForm

# Create your views here.
def home(request):
    prod= Product.objects.all()
    fm = ProductForm() #fetch all products from database
    return render(request, 'Electronics/home.html', {'prod': prod, 'fm':fm})

