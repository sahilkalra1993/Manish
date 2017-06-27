from django.conf.urls import url
from . import views

app_name = 'home'

urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    
  #  url(r'^register$', views.UserFormView.as_view(), name='register'),
    
    url(r'^wish$', views.create_wish, name='create_wish'),
    
    url(r'^image$', views.create_image, name='create_image'),
    
    url(r'^image_url$', views.create_image_url, name='create_image_url'),
    ]