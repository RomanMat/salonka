from django.db import models

# Master - person, that will give any services
class Master(models.Model):
    name = models.CharField(max_length=255)
    serve = models.CharField(max_length=255)

# Product - items, which will help poeple to take care of them
class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    is_present = models.BooleanField(default=True)

# Service - favor, that masters will provide
class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.FloatField()

# User - salon administrators
class User(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)