from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Customer, Product, Requirments
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout


def index(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            return render(request,'login.html',{'error':'No user found. Please Check your username and password'})
    cust=Customer()
    return render(request, 'login.html')


def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        if (username==password or email==password):
            return render(request, 'register.html', {'error':"Passowrd is simialr to username or email"})
        cust=Customer(username=username, password=password, email=email)
        user=User(username=username, password=password, email=email)
        cust.save()
        user.save()
        return redirect('/')
    return render(request,'register.html')



def home(request):
    return render(request, 'index.html')


def shop(request):
    products = Product.objects.all()
    context = {
        'shop': products
    }
    return render(request, 'shop.html', context)


def require(request):
    if request.method=='POST':
        name=request.POST.get('name')
        number=request.POST.get('number')
        bookname=request.POST.get('bookname')
        edition=request.POST.get('edition')
        req=Requirments(name=name, number=number, bookname=bookname, edition=edition)
        req.save()
    return render(request, 'require.html')


def purchase(request, id):
    product = get_object_or_404(Product, id=id)
    context = {
        'product': product
    }
    return render(request, 'purchase.html', context)