from django.db import models
from django.utils import timezone

# Create your models here.
class Trinkets(models.Model):
    author = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    city = models.CharField(max_length=30)
    year = models.DateField()
#    picture = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='imgs', height_field=None, width_field=None,
                                   max_length=50)
    coords = models.CharField(max_length = 20)



