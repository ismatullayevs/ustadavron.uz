from django.shortcuts import render
from django.http import HttpResponse
from .models import CarouselImage, Product, Photo, Category

def home_page(request):
    carousel_images = CarouselImage.objects.all()
    products = Product.objects.all()
    categories = Category.objects.all()
    photos = Photo.objects.all()

    context = {
        'carousel_images': carousel_images,
        'products': products,
        'photos': photos,
        'categories': categories,
    }
    return render(request, 'home.html', context)

def about_page(request):
    return render(request, 'about.html')

def contact_page(request):
    return render(request, 'contact.html')