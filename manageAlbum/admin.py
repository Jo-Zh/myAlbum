from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Author, Style, Album, CustomUser

class MyAdmin(admin.ModelAdmin):
    def save_model(self, request, instance, form, change):
        CustomUser = request.user 
        instance = form.save(commit=False)
        if not change or not instance.created_by:
            instance.created_by = CustomUser
        instance.modified_by = CustomUser
        instance.save()
        form.save_m2m()
        return instance
# Register your models here
admin.site.register(CustomUser, UserAdmin)
admin.site.register(Author)
admin.site.register(Style)
admin.site.register(Album)






