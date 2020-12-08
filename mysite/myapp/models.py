from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=200)
    roll = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=1500)

    def __str__(self):
        return f'{self.roll}  -  {self.name}' 