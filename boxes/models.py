from django.db import models

class Box(models.Model):
    titulo = models.CharField(max_length=100)
    color = models.CharField(max_length=20)