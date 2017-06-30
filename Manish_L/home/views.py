from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.db.models import Q
from django.views.generic import View
from django.views.generic.edit import CreateView
from .models import Wish, Image, Image_url
from .forms import UserForm,WishForm,ImageForm,ImageUrlForm

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def welcome(request):
    
    return render(request, 'home/welcome.html')


def create_wish(request):
    if not request.user.is_authenticated():
        return render(request, 'home/login.html')
    else:
        form = WishForm(request.POST or None)
        if form.is_valid():
            wish = form.save(commit=False)
            wish.user = request.user
            wish.save()
            
            all_wish = Wish.objects.filter(user=request.user)
            all_image = Image.objects.filter(user=request.user)
            all_image_url = Image_url.objects.filter(user=request.user)
            return render(request, 'home/home.html', {'all_wish' : all_wish, 'all_image' : all_image, 'all_image_url':all_image_url})
            #return render(request, 'home/home.html', {'wish': wish})
        context = {
            "form": form,
        }
        return render(request, 'home/create_wish.html', context)




def create_image(request):
    if not request.user.is_authenticated():
        return render(request, 'home/login.html')
    else:
        form = ImageForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.wish_image = request.FILES['wish_image']
            file_type = image.wish_image.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'image': image,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'home/create_image.html', context)
            image.save()
            
            all_wish = Wish.objects.filter(user=request.user)
            all_image = Image.objects.filter(user=request.user)
            all_image_url = Image_url.objects.filter(user=request.user)
            return render(request, 'home/home.html', {'all_wish' : all_wish, 'all_image' : all_image, 'all_image_url':all_image_url})
            #return render(request, 'home/home.html', {'image': image})
        context = {
            "form": form,
        }
        return render(request, 'home/create_image.html', context)
    
    
def create_image_url(request):
    if not request.user.is_authenticated():
        return render(request, 'home/login.html')
    else:
        form = ImageUrlForm(request.POST or None)
        if form.is_valid():
            image_url = form.save(commit=False)
            image_url.user = request.user
            image_url.save()
            all_wish = Wish.objects.filter(user=request.user)
            all_image = Image.objects.filter(user=request.user)
            all_image_url = Image_url.objects.filter(user=request.user)
            return render(request, 'home/home.html', {'all_wish' : all_wish, 'all_image' : all_image, 'all_image_url':all_image_url})
            #return render(request, 'home/home.html', {'image_url': image_url})
        context = {
            "form": form,
        }
        return render(request, 'home/create_image_url.html', context)


def home(request):
    
    if not request.user.is_authenticated():
        return render(request, 'home/welcome.html')
    else:
        user = request.user
        all_wish = Wish.objects.filter(user=request.user)
        all_image = Image.objects.filter(user=request.user)
        all_image_url = Image_url.objects.filter(user=request.user)
        return render(request, 'home/home.html', {'user': user, 'all_wish' : all_wish, 'all_image' : all_image, 'all_image_url':all_image_url})
   # return render(request, 'home/index.html')


#def wish(request):
    
#    return render(request, 'home/enter_wish.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'home/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                all_wish = Wish.objects.filter(user=request.user)
                all_image = Image.objects.filter(user=request.user)
                all_image_url = Image_url.objects.filter(user=request.user)
                return render(request, 'home/home.html', {'all_wish' : all_wish, 'all_image' : all_image, 'all_image_url':all_image_url})
            else:
                return render(request, 'home/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'home/login.html', {'error_message': 'Invalid login'})
    return render(request, 'home/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                all_wish = Wish.objects.filter(user=request.user)
                all_image = Image.objects.filter(user=request.user)
                all_image_url = Image_url.objects.filter(user=request.user)
                return render(request, 'home/home.html', {'all_wish' : all_wish, 'all_image' : all_image, 'all_image_url':all_image_url})
    context = {
        "form": form,
    }
    return render(request, 'home/register.html', context)


#===============================================================================
# class UserFormView(View):
#     form_class = UserForm
#     template_name = 'home/registration_form.html'
#     
#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, self.template_name, {'form': form})
#         
#     def post(self, request):
#         form = self.form_class(request.POST)
#         
#         if form.is_valid():
#             user = form.save(commit=False)
#             
#             
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user.set_password(password)
#             user.save()
#         
#             user = authenticate(username=username, password=password)
#         
#             if user is not None:
#             
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('home:home')
#             
#         return render(request, self.template_name, {'form': form})
#===============================================================================