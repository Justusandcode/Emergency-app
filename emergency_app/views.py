from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django import forms
from .forms import RegistrationForm,UserLoginForm,NewMessageForm
from .models import Neighbour,Message
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
import requests
POST_URL = 'http://api.sandbox.africastalking.com/version1/messaging'
API_KEY = "cf2f27b5f3911aa4e2bdcf93438a2f0fda0596925bdcdb5db9e9a3fd5c4fe9b4"
USERNAME="sandbox"


@login_required
def send_messsages(request):
    success = None
    form = NewMessageForm()
    if request.method == 'POST':
        
        msg = request.POST['message']
        to = "+" + request.POST['recipients']
        
        headers ={
            'Apikey':API_KEY
        }

        data = {
            'username':'sandbox',
            'to':to,
            'message':msg,
        }
        r = requests.post(POST_URL,data=data,headers=headers)
        if r.status_code == 200 or r.status_code == 201:
            success = 'Message Sent'
        else: return HttpResponse('An error occured ')
        return render(request,'send_messages.html',{'form':form,'success':success,'recipient':to})

    
    return render(request,'send_messages.html',{'form':form})

def message_list(request):
    
    # messages = Message.objects.filter(sender=request.user)
    messages = Message.objects.all()
    # print(messages[0].recipient.all())
    
    return render(request,'message_list.html',{'messages':messages})









def index(request):
    
    if not str(request.user) == 'AnonymousUser':
        neighbours = Neighbour.objects.filter(user=request.user)
        return render(request,'index.html',{'neighbours':neighbours})

    return render(request,'index.html')
    
    

def user_login(request):
    err = False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next = request.GET.get('next')
        

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                if not next: next = '/'
                return HttpResponseRedirect(next)
            else:
                err = 'Account not active ! '
        else:
            err = 'Invalid Login Details supplied'
        return render(request,'login.html',{'err':err})
    else:
        return render(request,'login.html')



def register(request):
    err = False
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data
            username = user['username']
            email =  user['email']
            password =  user['password']
            if (User.objects.filter(username=username).exists() or 
                User.objects.filter(email=email).exists()
                ):
                err = 'Sorry , it looks like a user with that email or username exists already . '
                print(err)
            else:
                User.objects.create_user(username,email,password)
                user = authenticate(username=username,password=password)
                login(request,user)
                return HttpResponseRedirect('/')
        else:
            err = 'An error occured . Please check your details '
            print(err)
        return render(request,'registration.html',{'form':form,'err':err})   
    else:
        form = RegistrationForm()
    return render(request,'registration.html',{'form':form})



@login_required()
def add_neighbours(request):
    if request.method == 'POST':
        name = request.POST.get('neighbour_name')
        phone = request.POST.get('phone')
        neighbour = Neighbour.objects.create(user=request.user,name=name,phone_number=phone)
        neighbour.save()

    neighbour = Neighbour.objects.filter(user = request.user)
    return render(request,'add_neighbour.html',{'neighbours':neighbour})
