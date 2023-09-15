from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Feedback
from .forms import FeedbackForm 
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
@login_required
def home(request):
    if request.method=="POST":
        if Feedback.objects.filter(student_name=request.user):
            forms=FeedbackForm()
            messages.error(request,"You have already submitted")
            return render(request,'index.html',{'forms':forms,})
        else:
            forms=FeedbackForm(request.POST)
            if forms.is_valid():
                feed=forms.save(commit=False)
                feed.student_name=request.user
                feed.save()
                messages.error(request,"Submitted Successfully")
                return redirect('/')
        
    forms=FeedbackForm()
    return render(request,'index.html',{'forms':forms})