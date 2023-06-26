from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from  django.core.files.storage import FileSystemStorage
from django.conf import settings
from .models import *


def index(request):
    return render(request,"index.html")

def studentregistraion(request):
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address1=request.POST.get('address1')
        address2=request.POST.get('address2')
        password=request.POST.get('password')
        registration=studentreg(firstname=firstname,lastname=lastname,email=email,phone=phone,address1=address1,address2=address2,password=password)
        registration.save()
    return render(request,'studentreg.html',{'succes':'registered suucessfully'})

def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if email == 'admin@gmail.com' and password =='admin':
        request.session['logintdetail'] = email
        request.session['admin'] = 'admin'
        return render(request, 'index.html')

    elif studentreg.objects.filter(email=email,password=password).exists():
        userdetail=studentreg.objects.get(email=request.POST['email'], password=password)
        if userdetail.password == request.POST['password']:
            request.session['uid'] = userdetail.id
            request.session['uname'] = userdetail.firstname

            request.session['email'] = email

            request.session['user'] = 'user'

            return render(request,'index.html')
        
    else:
        return render(request, 'loginform.html', {'status': 'Invalid Username or Password'})
    
def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
      del request.session[key]
    return redirect(index)
    
def studentdetails(request):
    tem=request.session['uid']
    vpro=studentreg.objects.get(id=tem)
    return render(request,'details.html',{'result':vpro})