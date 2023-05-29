from django.shortcuts import render, redirect
from .models import *

def home(request):
    return render(request, 'home.html')


def product(request):
    productlist = ProductPost.objects.all()
    return render(request, 'product.html', {'productlist': productlist})


def posting(request, pk):
    post = ProductPost.objects.get(pk=pk)
    return render(request, 'posting.html', {'post':post})

def newProduct(request):
    if request.method == 'POST':
        if request.POST['productImage']:
            new_article=ProductPost.objects.create(
                postTitle=request.POST['postTitle'],
                postContents=request.POST['postContents'],
                productImage=request.POST['productImage'],
            )
        else:
            new_article=ProductPost.objects.create(
                postTitle=request.POST['postTitle'],
                postContents=request.POST['postContents'],
                productImage=request.POST['productImage'],
            )
        return redirect('/product/')
    return render(request, 'newProduct.html')