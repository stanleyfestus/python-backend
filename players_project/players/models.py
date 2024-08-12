from django.db import models

# Create your models here.

class Player(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  age = models.IntegerField(default=0)
  country = models.CharField(max_length=255)
  position = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.first_name} {self.last_name}"