from django.contrib import admin
from .models import Trinkets
from django.utils.html import format_html


# Register your models here.

class trinketsAdmin(admin.ModelAdmin):
    list_filter = ['country']
    list_display = ['year', 'country', 'city', 'author', 'picture', 'pictumb']

    def pictumb(self, obj):
        return format_html('<img src="/media/{}" width=50px />'.format(obj.picture))



admin.site.register(Trinkets, trinketsAdmin)
admin.site.site_header = 'Trinkets administration'

