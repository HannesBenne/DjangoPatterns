from django.db import models

# Create your models here.
class Person(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.lastname}, {self.firstname} (phone: {self.phonenumber})'
