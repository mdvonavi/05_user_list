from django.db import models
from django import forms

class UserList(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.PositiveIntegerField(max_length=3)
    city = models.CharField(max_length=100)

