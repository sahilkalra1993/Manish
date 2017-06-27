from django.contrib import admin
from .models import Wish, Image, Image_url
# Register your models here.
admin.site.register(Wish)
admin.site.register(Image)
admin.site.register(Image_url)