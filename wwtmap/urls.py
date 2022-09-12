from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.trinket_list, name='trinket_list'),
    url(r'trinket_list', views.trinket_list, name='trinket_list'),
    url(r'wwmap', views.wwmap, name='wwmap'),
    url(r'mix', views.mixview, name='mixview'),
    url(r'stat', views.statistic, name='statistic')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
