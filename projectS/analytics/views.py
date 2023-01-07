from django.http import HttpResponse
from django.shortcuts import render

def analytics(request):
    return HttpResponse("Аналитика по профессии")

def categories(request):
    return HttpResponse("Востребованность профессии")