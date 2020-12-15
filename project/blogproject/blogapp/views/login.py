from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

#function for user login into dashboard
def Loginpage(request):
    if not request.user.is_authenticated:
        
        if request.method == "POST":
            
            form = AuthenticationForm(request=request, data=request.POST)
            
            if form.is_valid():
                print("hello ------------------------")
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                
                if user is not None:
                    login(request, user)
                    return redirect('dashpage')
            else:
                return redirect('loginpage')      
        else:
            form = AuthenticationForm()
            return render(request, 'blog/login2.html', {'form': form})
    else:

        return redirect('dashpage')


#function for logout from dashboard
def LogoutPage(request):
    logout(request)
    return redirect('loginpage')