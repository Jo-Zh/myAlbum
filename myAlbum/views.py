from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from manageAlbum import models

def homepage(req):
    # num=models.Album.objects.all().filter(created_by=req.user).count()
    num=models.Album.objects.all().count()
    return render(req, "myAlbum/home.html", {'num': num, 'user':req.user})

def myAlbum(req):
    if req.user.is_authenticated:
        authorAlbum=models.Album.objects.filter(created_by=req.user)
        
        return render(req, "myAlbum/album.html",{'albums':authorAlbum, "user":req.user})
    else:
        return HttpResponse("need login firstly!")

def detail(req, id):
    album=get_object_or_404(models.Album, pk=id)
    return render(req, "myAlbum/albumdetail.html", {'album':album})

def delete_view(req, id):
    context={}
    obj=get_object_or_404(models.Album, id=id)
    if req.method == "POST":
        obj.delete()
        return redirect("/myAlbum/")
    return render(req, "myAlbum/delete_view.html", context)
    
   