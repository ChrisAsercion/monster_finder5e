from django.shortcuts import render
from .models import Monster
from .services import fetch_monsters

def index(request):
    monsters = fetch_monsters(request)
    return render(request, 'monsters/index.html', {'monsters': monsters})

def select_cr(request):
    return render(request, 'monsters/select_cr.html')