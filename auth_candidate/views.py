from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.core.exceptions import PermissionDenied

# Create your views here.
def SignUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Account created for {username}")
            return redirect('ghor')
    else:
        form = SignUpForm()
    return render(request,'auth/signup.html',{'form':form})

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('stexam')
        else:
            messages.error(request,'Username or Password is incorrect')
    return render(request,'auth/login.html')


def Logout(request):
    logout(request)
    return render(request,'home.html')

def permission_denied_view(request, exception):
    return render(request, 'error.html', status=403)