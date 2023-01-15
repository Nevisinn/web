from django.urls import path

from .views import *


urlpatterns = [
    path('',index, name='home'),
    path('relevance/', relevance,name='relevance'),
    path('geography/', geography,name='geography'),
    path('skills/', skills,name='skills'),
    path('vacancy/', vacancy,name='vacancy')
]