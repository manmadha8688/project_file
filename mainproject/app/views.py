from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from review.models import reviews
from joblib import load

# Create your views here.

model = load('./model.joblib')

def index(request):
    r =reviews.objects.all()
    return render(request,'index.html',{'reviews':r})


