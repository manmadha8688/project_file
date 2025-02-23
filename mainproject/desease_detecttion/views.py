from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'detecttion_form.html')
def result(request):
    return render(request,'detect.html')