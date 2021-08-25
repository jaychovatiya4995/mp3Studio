from django.shortcuts import render

from django.shortcuts import render, redirect
from pytube import YouTube
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import os


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def copy(request):
    return render(request, 'copyright.html')


def dmca(request):
    return render(request, 'dmca.html')

def faqs(request):
    return render(request, 'faqs.html')


def contact(request):
    return render(request, 'contactus.html')


def privacy(request):
    return render(request, 'privacypolicy.html')


def terms(request):
    return render(request, 'termsofservice.html')
