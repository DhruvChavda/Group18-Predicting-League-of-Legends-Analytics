from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages 
from .forms import SignUpForm, EditProfileForm, AccountAuthenticationForm,Subscribe

from django.conf import settings
from django.core.mail import send_mail
import random


from cryptography.fernet import Fernet
import codecs
from .field_value import field_value 


# Create your views here.

def encryptionPasswrod(password):
    key = b'4WcfG0R2eGkVD8y20GcQXoN4k6i-OkNVgPDDIir0hsw='
    cipher = Fernet(key)
    Emsg = cipher.encrypt(password.encode())
    encrypt = codecs.decode(Emsg, 'UTF-8')
    return encrypt
    #return password


def home(request):
    return render(request, 'authenticate/home.html',{})


def subscribe(request):
    sub = Subscribe()
    if request.method == 'POST':
        sub = Subscribe(request.POST)
        subject = 'Paaword Reset code'
        random_number = random.randint(100000000, 999999999)
        message = 'your account password reset code is: ' + str(random_number)
        recepient = str(sub['Email'].value())
        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'authenticate/sucess.html', {'recepient': recepient})
    return render(request, 'authenticate/forgot_password.html', {'form':sub})


def login_user(request):

    user = request.user
    if user.is_authenticated: 
        messages.success(request,('You are already logged in'))
        return redirect("home")
    
    if request.method == 'POST':
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            #password = encryptionPasswrod(password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request,('Youre logged in'))
                return redirect('home')        
    else:
        form = AccountAuthenticationForm()
    context = {}
    context['login_form'] = form
    return render(request, 'authenticate/login_new.html', context)



def logout_user(request):
    logout(request)
    messages.success(request,('You are now logged out'))
    return redirect('home')


def register_user(request):
    user = request.user
    if user.is_authenticated: 
        messages.success(request,('You are already logged in'))
        return redirect("home")

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            print(request.POST.get('email'))
            '''
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
            messages.success(request, ('Youre now registered'))
            '''
            return redirect('home')
    else:
        form = SignUpForm()
    context = {'register_form': form}
    return render(request, 'authenticate/register_new.html', context)


def edit_profile(request):
    if request.method =='POST':
        form = EditProfileForm(request.POST, instance= request.user)
        #print(form.instance.password)
        if form.is_valid():
            form.save()
            messages.success(request, ('You have edited your profile'))
            return redirect('home')
    else: 		
        form = EditProfileForm(instance= request.user) 

    context = {'form': form}
    return render(request, 'authenticate/edit_profile.html', context)

def change_password(request):
    if request.method =='POST':
        form = PasswordChangeForm(data=request.POST, user= request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, ('You have edited your password'))
            return redirect('home')
    else: 		
        form = PasswordChangeForm(user= request.user) 
        
    context = {'form': form}
    return render(request, 'authenticate/change_password.html', context)