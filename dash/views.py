from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.
def user1(request):
    if request.user.is_authenticated:
        return render(request,'dash/classroom.html')
    else:
        return redirect('/account/login')

def qna(request):
    if request.user.is_authenticated:
        return render(request,'dash/qnapanel.html')
    else:
        return redirect('/account/login')

def classs(request):
    if request.user.is_authenticated:
        return render(request,'dash/class.html')
    else:
        return redirect('/account/login')


def profile(request):
    if request.user.is_authenticated:
        return render(request,'dash/profile.html')
    else:
        return redirect('/account/login')

def editprofile(request):
    if request.user.is_authenticated:
        print('OK')
        if request.method == "POST":
            #firstname = request.POST.get('firstname',False)
            #lastname = request.POST.get('lastname',False)
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            print(firstname," ",lastname)
            u = request.user
            u.first_name = firstname
            u.last_name = lastname 
            print(u.first_name," ",u.last_name)           
            u.save()
            return render(request,'dash/profile.html')
        else:
            return render(request,'dash/editprofile.html')
    else:
        return redirect('/account/login')

def changePW(request):
    if request.user.is_authenticated:
        pw = request.POST.get('pw',False)
        npw = request.POST.get('password1',False)
        if request.user.check_password(pw):
            u = request.user
            u.set_password(npw)
            u.save()
            messages.info(request,'Password changed successfully ;)')
            return redirect('/account/login')
        else:
            wp = False
            if request.method == "POST":
                wp = True
            return render(request,'dash/changePW.html',{'wp':wp})
    else:
        return redirect('/account/login')