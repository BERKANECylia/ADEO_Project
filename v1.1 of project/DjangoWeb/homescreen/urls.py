from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='homescreen-home-1'),
    path('about/',views.about,name='homescreen-about-1'),
]