from django.urls import path
from .import views

urlpatterns = [
    path("user1/", views.user1, name = 'user1'),
    path("qna/", views.qna, name = 'qna'),
    path("assign/", views.assign, name = 'assign'),
    path("classs/<int:pkid>/", views.classs, name = 'classs'),
    path("profile/",views.profile,name = 'profile'),
    path("editprofile/",views.editprofile,name = 'editprofile'),
    path("changePW/",views.changePW,name = 'changePW'),
    path("make_class/",views.make_class,name = 'make_class'),
    path("join_class/",views.join_class,name = 'join_class'), 
    path("create_work/<int:pkid>",views.create_work,name="create_work")   
]