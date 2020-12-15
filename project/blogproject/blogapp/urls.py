from django.contrib import admin
from django.urls import path
from .views import login,signup,dashboard,home,postcomment

urlpatterns = [
    path('',home.Homepage,name='homepage' ),
    path('dashpage',dashboard.Postpage,name='dashpage' ),
    path('commentpage/<int:id>',postcomment.Commentpage,name='commentpage' ),
    path('dashpage/<int:id>',dashboard.Postpage,name='dashpageedit' ),
     path('postdel/<int:id>',dashboard.PostDelPage,name='postdel' ),
    path('loginpage',login.Loginpage,name='loginpage' ),
    path('signup',signup.Signuppage,name='signuppage' ),
    path('logout',login.LogoutPage,name='logoutpage' ),
    path('like/<int:id>',home.LikePage,name='likepage' ),
]