from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView


# Create your views here.


def signup(request):
    if request.method=='POST':
        
        form=UserCreationForm(request.POST)

        if form.is_valid():
            user=form.save()
            messages.add_message(request,messages.INFO,f"Hey {user.username} your account has been succefully created")
            
            return redirect("/diary")

    else:
        form=UserCreationForm()

    
    return render(request,'usermanagement/signup.html',{"form":form})


def login_view(request):
    if not(request.user.is_authenticated):
        return LoginView.as_view(template_name='usermanagement/login.html')(request)

    else:
        return redirect("/diary")