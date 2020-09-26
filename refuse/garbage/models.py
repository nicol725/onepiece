from django.db import models

# Create your models here.
class Refuse(models.Model):
    city = models.CharField(max_length=20)
    kind1 = models.CharField(max_length=20)
    kind2 = models.CharField(max_length=20)
    kind3 = models.CharField(max_length=20)
    kind4 = models.CharField(max_length=20)
    kind5 = models.CharField(max_length=20)
    kind1_note = models.CharField(max_length=200)
    kind2_note = models.CharField(max_length=200)
    kind3_note = models.CharField(max_length=200)
    kind4_note = models.CharField(max_length=200)
    kind5_note = models.CharField(max_length=200)

class City(models.Model):
    city = models.CharField(max_length=20)
    kind = models.CharField(max_length=20)
    good = models.CharField(max_length=20)

