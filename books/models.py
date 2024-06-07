from django.db import models

# Create your models here.
class Book(models.Model):
    Title = models.CharField(max_length=100)
    Author = models.CharField(max_length=50)
    Publication_year = models.IntegerField(null=True)
    Genre = models.CharField(max_length=30)
    Availibity = models.BooleanField(default=False)

