from django.shortcuts import render
from django.http import HttpResponse

def root_home_page(request):
    return render(request, 'blog/home.html')
