from django.shortcuts import render,redirect
from .forms import PostForm
from .models import post
# Create your views here.
def home(request):
    

    if request.method=="POST":
       form= PostForm(request.POST)
       if(form.is_valid()):
           form.save()
           return redirect("home")
    else:
       data=post.objects.all()
       form=PostForm()  

    cotext={"type":"add",
        "form":form,
            "data":data}   
    return render(request ,"home.html",cotext)     

def update(request,id):
    data=post.objects.get(id=id)
    if request.method=="POST":
       print(request.POST)
       form= PostForm(request.POST,instance=data)
       if(form.is_valid()):
          
        #    form.save()
        #    data.n_update+=1
        #    data.save()
           data.text=form.cleaned_data["text"]
           data.n_update+=1
           data.save()


           return redirect("home")
    form= PostForm(instance=data)   
    cotext={"type":"update","form1":form}     
    return render(request ,"home.html",cotext)    

def delete(request,id):
   post.objects.get(id=id).delete()
   return redirect("home")