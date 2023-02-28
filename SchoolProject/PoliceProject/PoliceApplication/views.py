from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def dashboard(request):
    return render(request,'PoliceApplication/dashboard.html')
def about(request):
    return render(request,'PoliceApplication/about.html')
def contact(request):
    return render(request,'PoliceApplication/contact.html')
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
    return render(request, 'PoliceApplication/login.html', context)


def login_page(request):
    if request.method == "POST":
       username = request.POST.get('username')
       password = request.POST.get('password')
       
       user = authenticate(request, username=username, password=password)
       
       if user is not None:
           login(request, user)
           return redirect('dashboard')
       else:
           messages.info(request, "Username or password is incorrect !")
    context = {}
    return render(request, 'PoliceApplication/login.html', context)

def userLogout(request):
    logout(request)
    return redirect('login')
