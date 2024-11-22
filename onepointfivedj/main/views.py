from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def new(request):
    return render(request, 'main/news.html')

def discography(request):
    return render(request, 'main/discography.html')

def concerts(request):
    return render(request, 'main/concerts.html')