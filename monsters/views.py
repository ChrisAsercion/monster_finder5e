from django.shortcuts import render
from .models import Monster
from .services import fetch_monsters

def index(request):
    monsters = fetch_monsters()
    return render(request, 'monsters/index.html', {'monsters': monsters})
