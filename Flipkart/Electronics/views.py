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
        fm = ProductForm(request.POST, instance=prod) #bind the form with the product instance
        if fm.is_valid():
            fm.save()  #save the updated product details 
            return redirect('home')
    else:
        fm = ProductForm(instance=prod)  #create a form instance with the product data 

    return render(request, 'Electronics/edit.html', {'prod': prod, 'fm': fm}) #render the edit
