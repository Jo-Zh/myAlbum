from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Author, Style, Album, CustomUser


class AlbumAdmin(admin.ModelAdmin):
    list_display=('id', 'title','media','created_by') 
    sortable_by=('title',)
# Register your models here
admin.site.register(CustomUser, UserAdmin)
admin.site.register(Author)
admin.site.register(Style)
admin.site.register(Album, AlbumAdmin)






