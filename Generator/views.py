from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    #return render(request, 'Generator/home.html')
    return render(request, 'Generator/home.html')

def AboutUs(request):
    return render(request, 'Generator/AboutUs.html' )

def password(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')
    thePassword = ''
    length = int(request.GET.get("length"))
    if request.GET.get('Upper-case'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('Numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('Special-characters'):
        characters.extend(list('~!@#$%^&*()_+'))
    for x in range(length):
        thePassword += random.choice(characters)

    return render(request, 'Generator/password.html' , {'password':thePassword} )

    
