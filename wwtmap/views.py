from django.shortcuts import render
from django.db.models import Count
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
    trinkets = Trinkets.objects.values('country').annotate(total=Count('id')).order_by('-total')
    people = Trinkets.objects.values('author').annotate(total=Count('id')).order_by('-total')
    cities = Trinkets.objects.values('city').annotate(total=Count('id')).order_by('-total')

    return render(request, 'wwtmap/stat.html', {'trinkets':trinkets, 'people':people, 'cities':cities})
