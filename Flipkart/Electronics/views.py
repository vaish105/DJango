from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    prod= Product.objects.all()
    fm = ProductForm() #fetch all products from database
    return render(request, 'Electronics/home.html', {'prod': prod, 'fm':fm})

