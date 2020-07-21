"""TextUtills URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from.import Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Views.index,name = 'index'),
    #path('removepunch',  Views.removepuch,   name = 'removpunch'),
    #path('capfirst',     Views.capfirst,     name = 'capfirst'),
    #path('newlineremove',Views.newlineremove,name = 'newlineremove'),
    #path('spaceremove',  Views.spaceremove,  name = 'spaceremove'),
    #path('charcount',    Views.charcount,    name = 'charcount'),
    path('analyze',Views.analyze,name= 'analyze')

]
