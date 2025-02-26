from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
class PaymentMethod(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    #transacion entered date details
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp when created
    updated_at = models.DateTimeField(auto_now=True)  # Auto update timestamp
    

    # transaction data
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    type = models.ForeignKey(PaymentMethod,on_delete=models.CASCADE)

    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    payment_method = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(default=date.today())  # Transaction date (default to current)
    
   

    def __str__(self):
        return f"{self.user} - {self.type} - ${self.amount} - {self.date.strftime('%Y-%m-%d')}"


