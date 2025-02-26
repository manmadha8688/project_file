from django.db import models
from all_transactions.models import Category
from decimal import Decimal
# Create your models here.

class ExpensesLimits(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    limit = models.DecimalField(decimal_places=2,max_digits=10) 
    spent = models.DecimalField(decimal_places=2,max_digits=10,default=Decimal(0))    
    remaining = models.DecimalField(decimal_places=2,max_digits=10,default=Decimal(0))

    def __str__(self):
        return self.category.name