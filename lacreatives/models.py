from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=30)
    phonenumber = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    messages = models.TextField()



    def __str__(self):
        return self.name