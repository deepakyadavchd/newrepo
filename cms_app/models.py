from django.db import models

# Create your models here.

class Students(models.Model):
  rollno = models.IntegerField()
  name = models.CharField(max_length=100)
  marks = models.IntegerField()
  result = models.CharField(max_length=100)
  
