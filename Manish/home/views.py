from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.generic.edit import CreateView
from .models import Wish, Image, Image_url


def home(request):
    all_wish = Wish.objects.all()
    all_image = Image.objects.all()
    all_image_url = Image_url.objects.all()
    return render(request, 'home/home.html', {'all_wish' : all_wish, 'all_image' : all_image, 'all_image_url':all_image_url})
   # return render(request, 'home/index.html')


#def wish(request):
    
#    return render(request, 'home/enter_wish.html')

class wish(CreateView):
    model = Wish
    fields = ['wish_text']
    
class image(CreateView):
    model = Image
    fields = ['wish_image']
    
class image_url(CreateView):
    model = Image_url
    fields = ['name','image_url']
