from django.shortcuts import render, redirect
from ..forms import RegisterForm
from ..models.bloguser import *
#function for register user to access dashboard
def Signuppage(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            user = form.save()
            user.refresh_from_db()  # load the profile instants ctreate by signal
            user.profile.mobile = form.cleaned_data['mobile']
            user.profile.address = form.cleaned_data['address']
            user.save()
            
            return redirect('loginpage')

    else:
        
        form = RegisterForm()
        return render(request, 'blog/signup.html', {'form': form})

