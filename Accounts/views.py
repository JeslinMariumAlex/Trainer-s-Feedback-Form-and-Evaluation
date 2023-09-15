from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomeUserForm

# Create your views here.


def register(request):
    form=CustomeUserForm()
    if request.method=="POST":
        form=CustomeUserForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')
    return render (request,'registration/register.html',{'form':form})