from django.shortcuts import render, redirect
from .forms import UserRegisterForm,ReportForm,MessageForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import criminal,Offense,Category

# Create your views here.
def law(request):
    return render(request,'PoliceApplication/law.html')
def institution(request):
    return render(request,'PoliceApplication/institution.html')

def contact(request):
    form = MessageForm()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Message sent successfully")
            return redirect("contact")
    context = {
        "form": form
    }        
    return render(request,'PoliceApplication/contact.html',context)


def dashboard(request):
    crimes= Offense.objects.all()
    return render(request,'PoliceApplication/dashboard.html',{'crimes':crimes})


def report(request):
    form = ReportForm()
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your report sent successfully")
            return redirect("login")
    context = {
        "form": form
    }        
    return render(request,'PoliceApplication/report.html',context)
def wanted(request):
     

    
        criminals=criminal.objects.all()

    

        data = {}
        data['criminals'] = criminals
    

  

  
        return render(request,'PoliceApplication/criminal.html',data)



def about(request):
    return render(request,'PoliceApplication/about.html')

def services(request):
    return render(request,'PoliceApplication/services.html')
def homepage(request):
    return render(request,"PoliceApplication/index.html") 
def register(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account created successfully")
            return redirect("login")
    context = {
        "form": form
    }        
    return render(request, 'PoliceApplication/register.html', context)


def login_page(request):
   if request.user.is_authenticated:
        return redirect('dashboard')
   else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            print("working")
            login(request,user)
            return redirect('login')
       context={}
       return render(request,'PoliceApplication/signin.html',context)
def userLogout(request):
    logout(request)
    return redirect('/')
