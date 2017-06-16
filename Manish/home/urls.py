from django.conf.urls import url
from . import views

app_name = 'home'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^wish$', views.wish.as_view(), name='wish'),
    
    url(r'^image$', views.image.as_view(), name='image'),
    
    url(r'^image_url$', views.image_url.as_view(), name='image_url'),
    ]