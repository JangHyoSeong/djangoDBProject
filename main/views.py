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
                price=request.POST['price'],
                category=request.POST['category'],
                address=request.POST['address'],
            )
            new_upload=Upload.objects.create(
                userID=request.user,
                postID=new_article,
            )
        else:
            new_article=ProductPost.objects.create(
                postTitle=request.POST['postTitle'],
                postContents=request.POST['postContents'],
                productImage=request.POST['productImage'],
                price=request.POST['price'],
                category=request.POST['category'],
                address=request.POST['address'],
            )
            new_upload=Upload.objects.create(
                userID=request.user,
                postID=new_article,
            )
        return redirect('/product/')
    return render(request, 'newProduct.html')

def wishlist(request, pk):
    post = ProductPost.objects.get(pk=pk)

    if request.method == 'POST':
        new_wishlist=Wishlist.objects.create(
            userID=request.user,
            postID=post,
        )
        return redirect('product')
    return render(request, 'wishlist.html', {'wishlist': new_wishlist})

