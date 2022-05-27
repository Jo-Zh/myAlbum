from django.shortcuts import render, HttpResponse

# Create your views here.
def recorder(req):
    if req.user.is_authenticated:
        return render(req, 'recorder/recording.html')
    else:
        return HttpResponse('need loggin first!')
    