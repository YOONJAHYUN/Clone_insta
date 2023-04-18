from django.db import models

# Create your models here.
class Post(models.Model):
    
    content = models.TextField()
    created_at = models.DateField(auto_now=True)
    image = models.ImageField(blank=True)

