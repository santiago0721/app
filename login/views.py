from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def home(request):
    return render(request,'login/home.html')

@login_required
def menu(request):
    return render(request,'login/menu.html')

def exit(request):
    logout(request)
    return redirect('home')

def register(request):
    data = { 
        'form' : CustomUserCreationForm()
    }
    if request.method == 'POST':
        UserCreationForm = CustomUserCreationForm(data= request.POST)

        if UserCreationForm.is_valid():
            UserCreationForm.save()
            user = authenticate(username=UserCreationForm.cleaned_data['username'],password=UserCreationForm.cleaned_data['password1'])
            login(request,user)
            subject=request.POST["email"]
            email_from = settings.EMAIL_HOST_USER
            recipient_list=['requisitos1234@gmail.com']
            send_mail(subject,subject,'requisitos1234@gmail.com',recipient_list)

            return redirect('home')
       
    return render(request,'registration/register.html',data)

@login_required
def proyecto(request):
    return render(request,'login/proyecto.html')


