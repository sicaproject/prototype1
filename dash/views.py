from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import classsm,classsj


# Create your views here.
def user1(request):
    if request.user.is_authenticated:
        if request.user.profile.typee == 'S':
            u = request.user
            ch = classsj.objects.filter(sid = u.id)
            # for i in ch:
            #     print(i.id)
            #     print(i.clid.tid)
            #     print(i.sid.first_name)
            context = {'data':ch}
            return render(request,'dash/classroom2.html',context)
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

def make_class(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST['name']
            section = request.POST['section']
            u = request.user
            Subject = request.POST['Subject']
            pass1 = request.POST['pass2']
            cont_obj = classsm(tid = u, section=section , password = pass1 , name = name , subject = Subject)
            cont_obj.save()
            data = classsm.objects.filter(tid = 17)
            context = {'data':data}
            return render(request,'dash/temp.html',context)
        else:
            return render(request,'dash/makecl.html')
    else:
        return redirect('/account/login')

def join_class(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            id = int(request.POST['id'])
            pass3 = request.POST['pass2']
            data = classsm.objects.filter(id = id)
            u = request.user
            if data:
                data = classsm.objects.get(id = id)
                if data.password != pass3:
                    messages.info(request,'Wrong Password #_#')
                    return render(request,'dash/joincl.html')
                print(data)
                ch = classsj.objects.filter(sid = u.id,clid = id)
                print(ch)
                if ch:
                    messages.info(request,'Already Joined ;)')
                    return render(request,'dash/joincl.html')
                else:
                    cont_obj = classsj(sid = u, clid=data)
                    cont_obj.save()
                    print("class Joined Successfully")
                    context = {'data':data}
                    return render(request,'dash/temp2.html',context)
            else:
                messages.info(request,'Class id does not exist ;)')
                return render(request,'dash/joincl.html')
        else:
            return render(request,'dash/joincl.html')
    else:
        return redirect('/account/login')