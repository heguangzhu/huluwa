# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models

class Person(models.Model):
    nick_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=2)
    state = models.CharField(max_length=100)

class Dish(models.Model):
    dish_name = models.CharField(max_length=30)
    dish_type = models.CharField(max_length=30)
    caixi = models.CharField(max_length=30)
    flavor = models.CharField(max_length=30)
   
class TrainingItem(models.Model):
    nick_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=2)
    state = models.CharField(max_length=100)
    dish_name = models.CharField(max_length=30)
    dish_type = models.CharField(max_length=30)
    caixi = models.CharField(max_length=30)
    flavor = models.CharField(max_length=30) 
    rank = models.IntegerField()


