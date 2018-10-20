from django.shortcuts import render
from .models import Trinkets
# Create your views here.

def trinket_list(request):
    trinkets = Trinkets.objects.all()
    return render(request, 'wwtmap/trinket_list.html', {'trinkets':trinkets})

def wwmap(request):
    trinkets = Trinkets.objects.all()
    return render(request, 'wwtmap/wwmap.html', {'trinkets':trinkets})

def mixview(request):
    trinkets = Trinkets.objects.all()
    return render(request, 'wwtmap/mixview.html', {'trinkets':trinkets})
