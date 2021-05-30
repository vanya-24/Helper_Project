from django.urls import path
from . import views

urlpatterns = [
path('',views.home,name='covid-home'),
path('contact',views.contact,name='covid-contact'),
path('abts/',views.about,name='covid-about'),
path('registration/',views.registration,name='covid-reg'),
path('appointment/',views.appointment,name='covid-apt'),
path('doctors/',views.doctors,name='covid-doc'),
path('resources',views.resources,name='resources'),
path('signup',views.handleSignup,name='handleSignup'),
path('login',views.handleLogin,name='handleLogin'),
path('logout',views.handlelogout,name='handlelogout'),

]

