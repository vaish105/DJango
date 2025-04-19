from django.shortcuts import render , redirect
from .models import Product
from .forms import ProductForm

def home(request):
    fm = ProductForm()
    prod = Product.objects.all()

    if request.method == "POST":
        fm = ProductForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('home')

    return render(request, 'Electronics/home.html', {'prod': prod, 'fm': fm})

def edit_product(request, id):
    prod = Product.objects.get(id=id)   #fetch the product by id

    if request.method == "POST":
        fm = ProductForm(request.POST, instance=prod)
        if fm.is_valid():
            fm.save()
            return redirect('home')
    else:
        fm = ProductForm(instance=prod)
    return render(request, 'Electronics/edit_product.html', {'prod': prod, 'fm': fm})

def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    return render(request, 'Electronics/delete_product.html',{ 'product': product})
  