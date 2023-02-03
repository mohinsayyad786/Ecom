from django.shortcuts import render,redirect
from django.http import HttpResponse
from ecomapp.models import Task
from ecomapp.form import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

# Create your views here.

def homes(request):

    return render(request,'home.html')



def product(request):

    data="hello from product page"
    return HttpResponse(data)


def index(request):

    content={}
    #content['data']=Task.objects.all()
    #print(content['data'])
    content['data']=Task.objects.filter(is_deleted='N')

    return render(request,'index.html',content)

def add_product(request):

    if request.method=='POST':
        p=request.POST['p']
        t=request.POST['t']
        ps=request.POST['ps']
        siz=request.POST['siz']
        l=request.POST['l']
        pr=request.POST['pr']

        t1=Task.objects.create(product_id=p,product_name=t,product_shape=ps,product_size=siz,product_location=l,product_price=pr,is_deleted='N')
        #print(t1)
        t1.save()
        return redirect('/')
    else:



        return render(request,'add_product.html')

def delete(request,rid):

    x=Task.objects.filter(id=rid)
    x.update(is_deleted='Y')
    return redirect('/')


def edit(request,rid):
    if request.POST=='POST':
        up=request.POST['p']
        ut=request.POST['t']
        ups=request.POST['ps']
        usiz=request.POST['siz']
        ul=request.POST['l']
        upr=request.POST['pr']
        x=Task.objects.filter(id=rid)
        x.update(product_id=up,product_name=ut,product_shape=ups,product_size=usiz,product_location=ul,product_price=upr)
        return redirect('/')
    
    else:
        content={}
        content['data']=Task.objects.filter(id=rid)
        return render(request,'edit_form.html',content)


def Register(request):

    if request.method=='POST':

        fm=RegisterForm(request.POST)

        
        if fm.is_valid():
            messages.success(request,'Account Created Successfully,please Login!!!')
            fm.save()

        return redirect('/register')
    else:  
        fm=RegisterForm()
        return render(request,'signup.html',{'form':fm})


def Login(request):
    if request.method=="POST":
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            #print(uname)
            #print(upass)
            u=authenticate(username=uname,password=upass)
            #print(u)
            if u:
                login(request,u)
                return redirect('/')

    else:
        fm=AuthenticationForm()

        return render(request,'login.html',{'form':fm})


def getlogonuserid(request):
    user_id=request.user.id
    return render(request,'getloginid.html',{'data':user_id})


def Logout(request):
    logout(request)

    return redirect('/login')