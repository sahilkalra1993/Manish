from django.contrib.auth.models import Permission, User
from django.db import models
from django.core.urlresolvers import reverse

class Wish(models.Model):
    
    user = models.ForeignKey(User, default=1)
    wish_text = models.CharField(max_length = 75)
        
    def get_absolute_url(self):
        return reverse('home:home')
    
    def __str__(self):
        return self.wish_text

class Image(models.Model):
    
    user = models.ForeignKey(User, default=1)
    wish_image = models.FileField(null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse('home:home')
    
    
class Image_url(models.Model):
    
    user = models.ForeignKey(User, default=1)
    name = models.CharField(max_length = 100)
    image_url =  models.CharField(max_length = 500)
    
    def get_absolute_url(self):
        return reverse('home:home')

    def __str__(self):
        return self.name