

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Biography (models.Model):
    family_member_name = models.CharField(max_length=100)

    description = models.CharField(max_length=150)
    
    photo = models.ImageField(upload_to='images/')

    location = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    
   
    date_posted = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.family_member_name

    def summary(self):
        return self.description[:50]

    def get_absolute_url(self):
        return reverse('photohome')
