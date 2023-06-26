from django.db import models


class studentreg(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    address1=models.CharField(max_length=200)
    address2=models.CharField(max_length=200)
    password=models.CharField(max_length=200)