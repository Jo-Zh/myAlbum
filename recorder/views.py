from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def recorder(req):
    if req.user.is_authenticated:
        return render(req, 'recorder/recording.html')
    else:
        messages.info(req, 'Please Login or Sign Up!')
        return redirect("/")
        
    