from .models import CustomUser, Album
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
# from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model= CustomUser
        fields= ['username', 'email', 'password1', 'password2']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields=UserChangeForm.Meta.fields

# class AlbumForm(ModelForm):
#     class Meta:
#         model=Album
#         fields="__all__"