from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView,LoginView


from portal.views.dashboard import UserDashboardView
from portal.views import(
    SignUp,
    UserDashboardEditView, 
    UserInfoCreateView,
    UserInfoDashboardEditView,
    UserAddressEditView,

    
    )
app_name = 'portal'

urlpatterns = [

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', SignUp.as_view(), name='register'),
    path('user_info_create/',UserInfoCreateView.as_view(), name='user-info-create'),
    path('dashboard/',UserDashboardView.as_view(), name='dashboard'),
    
    ]
