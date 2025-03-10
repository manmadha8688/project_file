from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already taken..!!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email aalready used!!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,first_name=fname,last_name = lname,email=email,password=password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password not matching..')
            return redirect('register')


    return render(request,'register.html')

def login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials!!!')
        
    return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')