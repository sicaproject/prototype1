from django.urls import path
from .import views

urlpatterns = [
    path("", views.start2.as_view()),    
]