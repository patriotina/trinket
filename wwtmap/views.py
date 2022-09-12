from django.shortcuts import render
from .models import Trinkets
# Create your views here.

def trinket_list(request):
    trinkets = Trinkets.objects.all()
    return render(request, 'wwtmap/trinket_list.html', {'trinkets':trinkets})

def wwmap(request):
    trinkets = Trinkets.objects.all()
    return render(request, 'wwtmap/wwmap_cluster.html', {'trinkets':trinkets})

def mixview(request):
    trinkets = Trinkets.objects.all()
    return render(request, 'wwtmap/mixview.html', {'trinkets':trinkets})

def statistic(request):
    trinkets = Trinkets.objects.order_by().values('country').distinct()

    return render(request, 'wwtmap/stat.html', {'trinkets':trinkets})
