from django.urls import path
from .import views

urlpatterns = [
    path('',views.courses,name='home-page'),
]