from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name = 'index'),
     path('main/about', views.about, name = 'about'),
     path('main/contact', views.contact, name = 'contact'),
     path('main/price', views.price, name = 'price'),
     path('main/service', views.service, name = 'service'),
     path('main/portfolio', views.portfolio, name = 'portfolio'),

]