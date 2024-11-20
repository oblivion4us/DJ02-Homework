from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new', views.new, name='second'),
    path('discography', views.discography, name='third'),
    path('new', views.new, name='second')
]