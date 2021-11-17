from django.shortcuts import render,redirect
from django.http import HttpResponse#its return single html elemnt
from django.shortcuts import render
users=[]
def home(request):
 #   return HttpResponse('<h1>hello world</h1>')
    content={
        'name':'mahesh',
        'pagetitle':'homepage',
        'users':users
    }
    return render(request,'index.html',content)


def second(request):
    content={
        'name':'chinmya',
        'pagetitle':"second"
    }
    return render(request,'second.html',content )

def adduser(request):
    username=request.GET['first_name']
    users.append(username)
    return redirect('/')

def viewform(request):
    content={
        'pagetitle':'forms'
        
    }
    return render(request,'forms.html',content)

def loginuser(request):
    content={
        'pagetitle':'loginuser'
    }
    return render(request,'login.html',content)

def submituser(request):
    username=request.GET['username']
    email=request.GET['email']
    pass1=request.GET['pass1']
    pass2=request.GET['pass2']
    gender=request.GET['gender']
    address=request.GET['address']
    print(username,email,pass1,pass2,gender,address)
    return redirect('/')