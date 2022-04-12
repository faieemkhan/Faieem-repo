from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path("" , views.index, name='home'),
    path("courses" , views.courses, name='courses'),
    path("youtube" , views.youtube, name='youtube'),
    path("privacy" , views.privacy, name='privacy'),
    path("about" , views.about, name='about us')
]