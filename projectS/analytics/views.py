from django.http import HttpResponse
from django.shortcuts import render
from .models import *
menu = [{'title': "Востребованность","url_name":'relevance'},
        {'title': "География","url_name":'geography'},
        {'title': "Навыки","url_name":'skills'},
        {'title': "Последние вакансии","url_name":'vacancy'}]

def index(request):
    posts = Analytics.objects.all()
    context ={
        'posts':posts,
        'menu':menu,
        'title':'Главная страница'
    }
    return render(request,'analytics/index.html', context=context)

def relevance(request):
    return render(request,'analytics/relevance.html',{'menu':menu,'title':'Востребованность профессии'})

def geography(request):
    return render(request,'analytics/geography.html',{'menu':menu,'title':'География'})

def skills(request):
    return render(request,'analytics/skills.html',{'menu':menu,'title':'Навыки'})

def vacancy(request):
    return render(request,'analytics/vacancy.html',{'menu':menu,'title':'Последние вакансии'})