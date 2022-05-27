from django.urls import path
from .views import recorder

urlpatterns = [path('', recorder, name='recording')]