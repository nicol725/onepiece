from django.db import models

# Create your models here.
class Movie(models.Model):
    rank=models.IntegerField()
    title=models.CharField(max_length=20)
    link=models.CharField(max_length=100)
    rating=models.DecimalField(max_digits=3,decimal_places=1)
    participants=models.CharField(max_length=20)
    quote=models.CharField(max_length=100)