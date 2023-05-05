from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import signupform

def signupview(request):
    if request.method=='GET':
        form= signupform(request.GET)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = signupform()
    return render(request,'signup.html', {'form':form})

def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'next.html')
    else:
        return render(request,'login.html')

def Next(request):
    return render(request,'next.html')
