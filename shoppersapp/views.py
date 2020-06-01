from django.shortcuts import render
from .models import ScraperItem
#from .models import Classifications
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.shortcuts import render

def index(request):
    return render(request,'shoppersapp/index.html',{})

def mobiles_page(request):
    mobiles_list=ScraperItem.objects.filter(Q(category="mobiles") | Q(category="Mobile Phones"))
    paginator = Paginator(mobiles_list, 25)
    page = request.GET.get('page')
    try:
        mobiles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        mobiles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        mobiles = paginator.page(paginator.num_pages)

    return render(request,'shoppersapp/mobiles_page.html',{'mobiles': mobiles})

def cars_page(request):
    cars_list=ScraperItem.objects.filter(Q(category='cars')|Q(category="Cars"))
    paginator = Paginator(cars_list, 25)
    page = request.GET.get('page')
    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        cars = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        cars = paginator.page(paginator.num_pages)

    return render(request, 'shoppersapp/cars_page.html', {'cars': cars})

def motorcycles_page(request):
    motorcycles_list=ScraperItem.objects.filter(Q(category='motorcycles')|Q(category='Motorbikes & Scooters'))
    paginator = Paginator(motorcycles_list, 25)
    page = request.GET.get('page')
    try:
        motorcycles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        motorcycles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        motorcycles = paginator.page(paginator.num_pages)

    return render(request,'shoppersapp/motorcycles_page.html',{'motorcycles': motorcycles})


def laptops_page(request):

    laptops_list=ScraperItem.objects.filter(Q(category='laptops')|Q(category='Computers & Tablets'))
    paginator = Paginator(laptops_list, 25)
    page = request.GET.get('page')
    try:
        laptops = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        laptops = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        laptops = paginator.page(paginator.num_pages)

    return render(request,'shoppersapp/laptops_page.html',{'laptops':laptops})






