from django.db import models
from django.urls import reverse
from django.forms import ModelForm

class Widget(models.Model):
  description = models.CharField(max_length=1000)
  quantity = models.IntegerField()

def __str__(self):
    return (f'{self.description}| {self.quantity}')