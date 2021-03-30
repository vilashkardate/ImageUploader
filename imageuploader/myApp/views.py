from django.shortcuts import render
from .models import ImageUp
from .forms import ImageForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

    form = ImageForm()
    img = ImageUp.objects.all()
    return render(request,'myApp/home.html',{'img':img,'form':form})

    