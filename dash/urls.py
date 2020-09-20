from django.urls import path
from .import views

urlpatterns = [
    path("user1/", views.user1, name = 'user1'),
    path("qna/", views.qna, name = 'qna'),
    path("classs/", views.classs, name = 'classs'),
    path("profile/",views.profile,name = 'profile'),
    path("changePW/",views.changePW,name = 'changePW')
]