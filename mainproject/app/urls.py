from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('add_review',views.add_review,name='review'),
    

]
