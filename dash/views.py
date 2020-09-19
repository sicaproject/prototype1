from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def user1(request):
    if request.user.is_authenticated:
        return render(request,'dash/classroom.html')
    else:
        return redirect('/account/login')

def qna(request):
    return render(request,'dash/qnapanel.html')

def classs(request):
    return render(request,'dash/class.html')