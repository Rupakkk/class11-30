from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    views={}
    views['feedbacks']=Review.objects.all()
    # [{'name':'Ram'},{'post':''} and so on...]
    views['projects']=Project.objects.all()
    views['brands']=Brand.objects.all()
    
    return render(request,'index.html',views) #we are returning views to the index page as well

def about(request):
    views={}
    views['feedbacks']=Review.objects.all()
    return render(request,'about.html',views)

def bloghome(request):
    return render(request,'blog-home.html')

def blogsingle(request):
    return render(request,'blog-single.html')

def contact(request):
    if request.method=="POST":
        
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        data=Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        data.save()
        views={}
        views["message"]={"The form is submitted"}
        return render(request,'contact.html',views)
    return render(request,'contact.html')

def elements(request):
    return render(request,'elements.html')

def portfolio(request):
    return render(request,'portfolio.html')

def price(request):
    return render(request,'price.html')

def services(request):
    return render(request,'services.html')
