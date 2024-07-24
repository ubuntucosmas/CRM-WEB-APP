from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class record(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)


    def __str__(self):
        return self.first_name + " " + self.last_name
    




