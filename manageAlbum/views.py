from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser, Album
from .form import CustomUserCreationForm
from django.forms import modelform_factory 
# Create your views here.

def SignUpView(req):
    
    form=CustomUserCreationForm
    if req.method=='POST':
        regForm=CustomUserCreationForm(req.POST)
        if regForm.is_valid():
            regForm.save()
            messages.success(req, 'User has been registered!')
    return render(req, 'registration/signup.html', {'form':form})


AlbumForm=modelform_factory(Album, exclude=[])

def new(req):
    if req.method=='POST':
        form=AlbumForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            print('record saved')
            return redirect('myAlbum')
        else:
            print('not Saved!')
    else:
        form=AlbumForm()
    return render(req, 'manageAlbum/form.html', {"form":form})