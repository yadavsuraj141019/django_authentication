from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

# REGISTRATION VIEW FUNCTION

def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'ACCOUNT CREATED SUCCESSFULLY !!!')
            fm.save()
    else:
        fm = SignUpForm()
    return render(request, 'accounts/signup.html', {'form':fm})



# LOGIN VIEW FUNCTION

def user_login(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully !!!')
                return HttpResponseRedirect('/profile/')
    else:
        fm = AuthenticationForm()
    return render(request, 'accounts/userlogin.html', {'form':fm})


# USER PROFILE VIEW FUNCTION

def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'accounts/profile.html', {'name': request.user})
    else:
        return HttpResponseRedirect('/login/')


# LOGOUT VIEW FUNCTION
 
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
