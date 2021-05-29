from django.urls import path
from . import views

urlpatterns = [
path('',views.home,name='covid-home'),
path('contact',views.contact,name='covid-contact'),
path('about/',views.about,name='covid-about'),
path('resources',views.resources,name='resources')
]
