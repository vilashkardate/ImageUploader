from django.db import models

# Create your models here.

class ImageUp(models.Model):
    photo = models.ImageField(upload_to="MyImage")
    date = models.DateTimeField(auto_now_add=True)
    