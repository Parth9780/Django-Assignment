from django.shortcuts import render, redirect
from .models import ProductMst, ProductSubCat
from .forms import *
from django.contrib import messages


def index(request):
    products = ProductMst.objects.all()
    if request.method == 'POST':
        form = ProductSubCatForm(request.POST)
        if form.is_valid():
            form.save()
            print("Product Are Added !")
        else:
            form = ProductSubCatForm()
    return render(request,'index.html',{'products':products})
