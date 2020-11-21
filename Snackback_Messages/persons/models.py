from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField(default=0)