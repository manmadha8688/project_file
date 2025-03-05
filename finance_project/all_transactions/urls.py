from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='all_transactions'),
    
    path('add_transaction/',views.add_transaction,name='add_transaction'),
    path('delete_transactions/',views.delete_transactions,name='delete_transactions'),
]