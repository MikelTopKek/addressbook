from django.db import models
from django.contrib.staticfiles import storage


class ListModelMixin:
    pass


class People(models.Model):
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    address = models.CharField(max_length=20)
    telephone = models.CharField(max_length=13)
    url = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.surname

    class Meta:
        ordering = ['name']
