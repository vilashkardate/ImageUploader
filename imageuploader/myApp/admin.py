from django.contrib import admin
from .models import ImageUp
# Register your models here.

@admin.register(ImageUp)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id' , 'photo' ,  'date']
    