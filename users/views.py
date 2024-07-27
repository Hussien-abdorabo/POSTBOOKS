from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from httpx import Auth
from .forms import SignupForm , ProfileupdateForm , ImageupdateForm
from django.contrib import auth
from .models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.



def Sign_up(request):
    if request.method == 'POST':
      form = SignupForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('blog-index')
    else:
       form = SignupForm()
         
    return render(request,"user/sign-up.html",{
        "form": form
    })



@login_required
def logout(request):
    auth.logout(request)
    return render(request , "user/logout.html")


@login_required
def profile(request):
   if request.method == 'POST':
       u_form = ProfileupdateForm(request.POST or None, instance= request.user)
       p_form = ImageupdateForm(request.POST or None, request.FILES or  None, instance=request.user.profile)

       if u_form.is_valid() and p_form.is_valid():
          u_form.save()
          p_form.save()
          return redirect("users-profile")
   else:
       u_form = ProfileupdateForm(instance= request.user)
       p_form = ImageupdateForm(instance= request.user.profile)
       
   return render(request , "user/profile.html",{
      "u_form" : u_form,
      "p_form": p_form
   })