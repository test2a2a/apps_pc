from django.shortcuts import render,redirect
from django.contrib import messages
from .form import UserRegisterForm
# Create your views here.





def home (request):
   return render(request, "home.html")
    


def about (request):
   return render(request, "about.html")


def register (request):
    if request.method=="POST":
       form= UserRegisterForm(request.POST)
       if form.is_valid():
          
          form.save()
          usename=form.cleaned_data.get("username")
          messages.success(request ,f'account created for {usename}')
          return redirect("home")
    else:
          form=UserRegisterForm()

    
    return render(request, "user/register.html",{"form":form})

def login (request):

    form=UserRegisterForm()
    return render(request, "user/login.html" ,{"form":form})
    