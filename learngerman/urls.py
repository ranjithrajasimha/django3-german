"""learngerman URL Configuration

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
from django.urls import path
from german import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('dictionary/', views.dictionary, name='dictionary'),
    path('aquiz/', views.artikelquiz, name='artikelquiz'),
    path('wquiz/', views.wordquiz, name='wordquiz'),


    path('germanblogs/', views.germanblogs, name='germanblogs'),
    path('createblog/', views.createblog, name='createblog'),
    path('<int:blog_id>/', views.detailblog, name='detailblog'),
    path('blog/<int:blog_id>/edit', views.editblog, name='editblog'),
    path('blog/<int:blog_id>/delete', views.deleteblog, name='deleteblog'),

    path('login', views.loginpage, name='loginpage'),
    path('logout', views.logoutuser, name='logoutuser'),

]
