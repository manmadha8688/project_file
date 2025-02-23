from django.urls import path
from . import views
app_name = "desease_detecttion"

urlpatterns = [
    
    path('',views.home,name='desease_home'),
    path('result',views.result,name='detect_result'),
   
]
