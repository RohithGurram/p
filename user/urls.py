from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',HomeView,name='home'),
    path('contact/',ContactView,name='contact'),
    path('project/',ProjectView.as_view(),name='project'),
    path('project/<int:pk>/',ProjectDetailView.as_view(),name='detail'),
]