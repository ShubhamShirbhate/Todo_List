from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError    
from django.contrib.auth import login, logout, authenticate
from .forms import Todooform
    

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'account/signupuser.html', {'form':UserCreationForm})
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.create_user (request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except  :
                return render(request, 'account/signupuser.html', {'form':UserCreationForm, 'error':'This Username already been taken choose anather one..'})

        else:
            return render(request, 'account/signupuser.html', {'form':UserCreationForm, 'error':'password must be matched..'})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'account/loginuser.html', {'form':AuthenticationForm()})
            
    else:
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request, 'account/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and Passwoord did not match'})
        else:
            login(request, user)
            return redirect('home')


def create(request):
    if request.method == 'GET':
        return render(request, 'account/create.html', {'form':Todooform()})
    else:
        try:
            form = Todooform(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('home')
        except ValueError:
             return render(request, 'account/create.html', {'form':Todooform(), 'error':'Ttle Insdex Out Of Bound '})