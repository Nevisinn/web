from django.http import HttpResponse
from django.shortcuts import render
from .models import *
menu = ["Востребованность","География","Навыки","Последние вакансии"]

def index(request):
    posts = Analytics.objects.all()
    return render(request,'analytics/index.html',{'posts': posts, 'menu':menu, 'title':'Главная страница'})

def about(request):
    return render(request,'analytics/about.html',{'menu':menu,'title':'О сайте'})
