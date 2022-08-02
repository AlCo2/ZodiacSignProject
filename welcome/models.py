from django.db import models

class user(models.Model):
    name = models.CharField(max_length=30,default='name')
    zodiac = models.CharField(max_length=30,default='zodiacsign')
