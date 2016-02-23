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

class UserProfile(models.Model):
	addressline1 = models.CharField(max_length=30)
	addressline2 = models.CharField(max_length=30)
	addresscity = models.CharField(max_length=30)
	addresszip = models.CharField(max_length=15)
	addresscountry = models.TextField(max_length=30)
	user = models.ForeignKey(User)

#MAKE SURE TO ADD THESE TO ADMIN! SO THAT THEY APPEAR IN THE ADMIN WEBPAGE, HOWEVER YOU DO THAT AGAIN