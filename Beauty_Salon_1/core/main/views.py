from django.shortcuts import render, redirect
from .models import Header, About, Service, Price, Contact, Portfolio, Team

# Create your views here.


def index(request):
    price = Price.objects.all()
    service = Service.objects.all()
    header = Header.objects.first()
    about = About.objects.first()
    team = Team.objects.all()
    if request.method == 'POST':
        user_name = request.POST.get('name')
        user_phone = request.POST.get('phone')
        user_email = request.POST.get('email')
        user_subject = request.POST.get('subject')
        user_message = request.POST.get('message')
        Contact.objects.create(name = user_name, phone = user_phone, email = user_email, subject = user_subject, message = user_message)
        return redirect('index')
    return render(request, 'main/index.html', context={
        'header':header,
        'about':about,
        'service':service,
        'price':price,
        'team':team,
        'link':'index'

    })

def about(request):
    about = About.objects.first()
    team = Team.objects.all()
    return render(request, 'main/about.html', context={
        'about':about,
        'team':team,
        'link':'about'
        
    })

def contact(request):
    if request.method == 'POST':
        user_name = request.POST.get('name')
        user_phone = request.POST.get('phone')
        user_email = request.POST.get('email')
        user_subject = request.POST.get('subject')
        user_message = request.POST.get('message')
        Contact.objects.create(name = user_name, phone = user_phone, email = user_email, subject = user_subject, message = user_message)
        return redirect('index')
    return render(request, 'main/contact.html', context={
        'link':'contact',
    })

def price(request):
    price = Price.objects.all()
    return render(request, 'main/price.html', context={
        'price':price,
        'link':'price',
    })

def service(request):
    service = Service.objects.all()
    return render(request, 'main/service.html', context={
        'service':service,
        'link':'service'
    })


def portfolio(request):
    portfolio = Portfolio.objects.all()
    return render(request, 'main/portfolio.html', context={
        'portfolio':portfolio,
        'link':'portfolio',
    })




