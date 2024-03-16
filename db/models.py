from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255,)
    email = models.EmailField(max_length=255,unique=True)
    balance = models.IntegerField()

# create table customer(name varchar(255), email varchar(255), balance int);