from django.db import models
from django.core.urlresolvers import reverse

class Wish(models.Model):

    wish_text = models.CharField(max_length = 75)
        
    def get_absolute_url(self):
        return reverse('home:home')
    
    def __str__(self):
        return self.wish_text

class Image(models.Model):

    wish_image = models.FileField(null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse('home:home')
    
    
class Image_url(models.Model):
    
    name = models.CharField(max_length = 100)
    image_url =  models.CharField(max_length = 500)
    
    def get_absolute_url(self):
        return reverse('home:home')

    def __str__(self):
        return self.name