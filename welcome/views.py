from unicodedata import name
from django.shortcuts import render
from welcome.models import user


# Create your views here.

def welcome(request):
    if request.method=='POST':
        name=request.POST.get('name')
        zodiac=request.POST.get('zodiac')
        data=user(name=name,zodiac=zodiac)
        data.save()
    return render(request, 'pages/welcome.html')
def scorpio(request):
    return render(request, 'pages/scorpio.html')
def aries(request):
    return render(request, 'pages/aries.html')
def sag(request):
    return render(request, 'pages/sagittarius.html')
def tau(request):
    return render(request, 'pages/taurus.html')
def pisces(request):
    return render(request, 'pages/pisces.html')
def aqua(request):
    return render(request, 'pages/aquarius.html')
def libra(request):
    return render(request, 'pages/libra.html')
def gemini(request):
    return render(request, 'pages/gemini.html')
def virgo(request):
    return render(request, 'pages/virgo.html')
def leo(request):
    return render(request, 'pages/leo.html')
def cancer(request):
    return render(request, 'pages/cancer.html')
def aboutme(request):
    return render(request, 'pages/aboutme.html')
def capr(request):
    return render(request, 'pages/cap.html')