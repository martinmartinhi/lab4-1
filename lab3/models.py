from django.db import models

from django.contrib import admin
    

class book(models.Model):
    ISBN = models.CharField(primary_key=True,max_length=200)
    title = models.CharField(max_length=200)
    authorid = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    publishdate = models.CharField(max_length=200)
    price = models.FloatField()


class author(models.Model):
    authorid = models.CharField(primary_key=True,max_length=200)
    name = models.CharField(max_length=200)
    age =models.IntegerField()
    country = models.CharField(max_length=200)
