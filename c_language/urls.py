from django.contrib import admin
from django.urls import path,include
from c_language import views

urlpatterns = [
    path("" , views.c_index, name='C_language'),

]