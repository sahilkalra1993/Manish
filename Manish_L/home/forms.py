from django.contrib.auth.models import User
from django import forms
from .models import Wish,Image,Image_url

class WishForm(forms.ModelForm):

    class Meta:
        model = Wish
        fields = ['wish_text']
        
class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['wish_image']

class ImageUrlForm(forms.ModelForm):

    class Meta:
        model = Image_url
        fields = ['name', 'image_url']


class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']