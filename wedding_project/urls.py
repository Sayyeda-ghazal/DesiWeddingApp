"""wedding_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from planner import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', lambda request: redirect('login'), name='root'), 
    path('home/', views.home, name = "home"),
    path('event/', views.event_selection, name='event_selection'),
    path('menus/', views.menus, name='menus'),
    path('get_quote/', views.get_quote, name='get_quote'),
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    # path('login/', views.login_view, name='login'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html', success_url='home'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    
]
