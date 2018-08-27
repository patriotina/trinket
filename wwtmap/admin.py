from django.contrib import admin
from .models import Trinkets

# Register your models here.

class trinketsAdmin(admin.ModelAdmin):
    list_filter = ['country']
    list_display = ['year', 'country', 'city', 'author']

admin.site.register(Trinkets, trinketsAdmin)
admin.site.site_header = 'Trinkets administration'

