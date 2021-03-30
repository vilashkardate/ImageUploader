from django import forms

from .models import ImageUp

class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageUp
        fields = '__all__'
        labels = {'photo' :''}