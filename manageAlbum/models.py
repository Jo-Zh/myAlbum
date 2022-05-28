from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


# Create your models here.
class CustomUser(AbstractUser):
    pass



class Style(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Author(models.Model):
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    media=models.ImageField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.lastName

class Album(models.Model):
    title=models.CharField(max_length=20)
    script=models.TextField()
    media=models.FileField(upload_to='media', null=True, blank=True)
    # author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_by = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    style = models.ManyToManyField(Style, help_text='Select a style for this album')


    class Meta:
        ordering=['title']
    
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])


    def __str__(self):
        return self.title


