from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
      name = models.CharField(max_length=200)
      description = models.TextField()
      price = models.FloatField()
      def __str__(self):
      	  return self.name

class Order(models.Model):
      status = models.IntegerField()
      user = models.ForeignKey(User)
      items = models.ManyToManyField(Product)
      def __str__(self):
            return str(self.status)
