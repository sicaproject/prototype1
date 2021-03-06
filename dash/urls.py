from django.urls import path
from .import views

urlpatterns = [
    path("user1/", views.user1, name = 'user1'),
    path("qna/", views.qna, name = 'qna'),
    path("assign/<int:pkid>/", views.assign, name = 'assign'),
    path("classs/<int:pkid>/", views.classs, name = 'classs'),
    path("profile/",views.profile,name = 'profile'),
    path("editprofile/",views.editprofile,name = 'editprofile'),
    path("changePW/",views.changePW,name = 'changePW'),
    path("make_class/",views.make_class,name = 'make_class'),
    path("join_class/",views.join_class,name = 'join_class'), 
    path("create_work/<int:pkid>",views.create_work,name="create_work"), 
    path("create_a_work/<int:pkid>",views.create_a_work,name="create_a_work"),
    path("submits/<int:pkid>/<int:aid>",views.submits,name="submits"),
    path("assignment/<int:pkid>/<int:aid>",views.assignment,name="assignment"), 
    path("del_work",views.del_work,name="del_work"),
    path("eval_score",views.eval_score,name="eval_score"),
    path("leave_class/<int:pkid>",views.leave_class,name="leave_class"),
    path("q_ask/", views.q_ask, name = 'q_ask'),
    path("answer/", views.answer, name = 'answer')
]