from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CarouselImage, Product, Photo, Category, Contact, HomePage
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

def home_page(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            body = {
                'name': name,
                'email': email,
                'message': message,
            }   

            contact = Contact(name=name, subject=subject, email=email, message=message)
            contact.save()

            email_message = "\n".join(body.values())
            try:
                send_mail(subject, email_message, "_mainaccount@ustadavron.uz", ['davron_35@mail.ru', 'ismatullayevpro@gmail.com']) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("home")


    carousel_images = CarouselImage.objects.all()
    products = Product.objects.all()
    categories = Category.objects.all()
    photos = Photo.objects.all()
    form = ContactForm()
    page = HomePage.objects.first()

    context = {
        'carousel_images': carousel_images,
        'products': products,
        'photos': photos,
        'categories': categories,
        'form': form,
        'page': page,
    }
    return render(request, 'home.html', context)

def about_page(request):
    return render(request, 'about.html')

def contact_page(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            body = {
                'name': name,
                'email': email,
                'message': message,
            }   

            contact = Contact(name=name, subject=subject, email=email, message=message)
            contact.save()

            email_message = "\n".join(body.values())
            try:
                send_mail(subject, email_message, "_mainaccount@ustadavron.uz", ['davron_35@mail.ru', 'ismatullayevpro@gmail.com']) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("home")


    form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, 'contact.html', context=context)