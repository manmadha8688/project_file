from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from .models import reviews

from joblib import load

# Create your views here.

model = load('./model.joblib')

def index(request):
    review =reviews.objects.all()
    return render(request,'index.html',{'reviews':review})
def add_review(request):
    if request.method == 'POST':
        ratting = request.POST['ratting']
        dis = request.POST['dis']

        review = reviews(ratting=ratting,discription=dis)
        review.save()
        return redirect('/')
    
    return render(request,'add_review.html')


