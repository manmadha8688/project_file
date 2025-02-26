from django.urls import path,include
from . import views

app_name = 'goal'
urlpatterns = [
    path('',views.home,name='goals'),
]
