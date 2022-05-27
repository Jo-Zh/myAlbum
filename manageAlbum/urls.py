from django.urls import path, include
from . import views

urlpatterns=[
 path('uploadform/', views.new, name='uploadform'),
 path('signup/', views.SignUpView, name='signup'),
 path('', include('django.contrib.auth.urls'), name='login'),
]