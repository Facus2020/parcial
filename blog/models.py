
from django.db import models
from django.conf import Settings
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.title
    
    