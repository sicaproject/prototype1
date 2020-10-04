from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
import traceback 
from .models import classsm,classsj,work,classwork,submit


# Create your views here.
class my_dictionary(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value


def user1(request):
    if request.user.is_authenticated:
        if request.user.profile.typee == 'S':
            u = request.user
            ch = classsj.objects.filter(sid = u.id)
            ts = my_dictionary() 
            for i in ch:
                ts.add(i.clid.id,classsj.objects.filter(clid=i.clid.id).count())
            context = {'data':ch,'ts':ts}
            return render(request,'dash/classroom2.html',context)
        else:
            u = request.user
            ch = classsm.objects.filter(tid = u.id)
            ts = my_dictionary() 
            for i in ch:
                ts.add(i.id,classsj.objects.filter(clid=i.id).count())
            context = {'data':ch,'ts':ts}
            return render(request,'dash/classroom.html',context)
    else:
        return redirect('/account/login')

def qna(request):
    if request.user.is_authenticated:
        return render(request,'dash/qnapanel.html')
    else:
        return redirect('/account/login')

def assign(request,pkid):
    if request.user.is_authenticated:
        obj = classsm.objects.get(pk=pkid)
        objclasswork = classwork.objects.filter(clid=pkid,wtype = 2)
        context = {'data':obj,'classcontent':objclasswork}
        return render(request,'dash/assign.html',context)
    else:
        return redirect('/account/login')

def classs(request,pkid):
    if request.user.is_authenticated:
        obj = classsm.objects.get(pk=pkid)
        objclasswork = classwork.objects.filter(clid=pkid,wtype = 1)
        context = {'data':obj,'classcontent':objclasswork}
        return render(request,'dash/class.html',context)
    else:
        return redirect('/account/login')

def create_work(request,pkid):
    if request.user.is_authenticated:
        announcement = request.POST['announcement']
        obj = classsm.objects.get(pk=pkid)
        objclasswork = classwork.objects.filter(clid=pkid,wtype = 2)
        context = {'data':obj,'classcontent':objclasswork}
        if request.method == 'POST':            
            s = request.FILES['announcement_doc']
            objclass = classsm.objects.get(pk=pkid)
            obj = work.objects.get(pk=1)
            try:
                cont_obj = classwork(clid = objclass, wtype=obj , wname = announcement, filess = s)
                cont_obj.save()
            except:
                print("Failed due to exception")
            return redirect('/dash/user1/')
        return redirect('/dash/user1/')
    else:
        return redirect('/account/login')


def submits(request,pkid,aid):
    if request.user.is_authenticated:
        if request.method == 'POST':        
            stxt = request.POST['submit_text']    
            s = request.FILES['submit_doc']
            objclass = classwork.objects.get(pk=aid)
            u = request.user
            try:
                cont_obj = submit(cwid = objclass, sid = u , stext = stxt, sfile = s)
                cont_obj.save()
            except:
                print("Failed due to exception")
                traceback.print_exc()
            return redirect('/dash/user1/')
        return redirect('/dash/user1/')
    else:
        return redirect('/account/login')

def del_work(request):
    if request.user.is_authenticated:
        pkid = int(request.POST.get('announcement_id',False))
        instance = classwork.objects.get(id=pkid)
        instance.delete()
        return redirect('/dash/user1/')
    else:
        return redirect('/account/login')

def assignment(request,pkid,aid):
    if request.user.is_authenticated:
        obj = classsm.objects.get(pk=pkid)
        a_obj = classwork.objects.get(pk=aid)
        students = submit.objects.filter(cwid=aid)
        stud_c = students.count()
        t = classsj.objects.filter(clid=pkid)
        t_ctr = t.count()
        n_stud = []
        uid = request.user.id
        s_obj = submit.objects.filter(cwid = aid,sid = uid)
        context = {'data':obj,'a_obj':a_obj,'s_obj':s_obj,'stud':students,'stud_c':stud_c,'t_ctr':t_ctr,'t':n_stud}
        return render(request,'dash/assignment.html',context)
    else:
        return redirect('/account/login')

def create_a_work(request,pkid):
    if request.user.is_authenticated:
        Assignments = request.POST['Assignments']
        if request.method == 'POST':
            s = request.FILES['assignment_doc']
            objclass = classsm.objects.get(pk=pkid)
            obj = work.objects.get(pk=2)
            try:
                cont_obj = classwork(clid = objclass, wtype=obj , wname = Assignments, filess = s)
                cont_obj.save()
            except:
                print("Failed due to exception")
            return redirect('/dash/user1/')
        
        return redirect('/dash/user1/')
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
            propic = request.FILES['file']
            print(firstname," ",lastname)
            u = request.user
            u.first_name = firstname
            u.last_name = lastname 
            u.profile.profile_pic = propic
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