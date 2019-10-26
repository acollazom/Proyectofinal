from django.urls import path
from .import views

urlpatterns = [
#Paths AlexCollazo
    path('',views.home, name="home"),
    path('about/',views.about, name="about"),
    path('sample/',views.sample, name="sample"),
]
