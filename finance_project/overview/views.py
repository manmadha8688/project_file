import json
from django.shortcuts import render,redirect
from all_transactions.models import *
from setexpenselimit.models import ExpensesLimits
# Create your views here.


def home(request):
    
    expenselimits = ExpensesLimits.objects.all()
    total_income = 0
    total_expense = 0
    income = PaymentMethod.objects.get(name='income')
    income_t = Transaction.objects.filter(type=income)
    for i in income_t:
        total_income += i.amount
    
    expense = PaymentMethod.objects.get(name='expense')
    
    expense_t = Transaction.objects.filter(type=expense)
    for i in expense_t:
        total_expense += i.amount
    balance = total_income-total_expense

    expenselimits = {
        str(i.category): {"limit": int(i.limit), "spent": int(i.spent) } for i in expenselimits
        
    }

    
    return render(request,'overview.html',{'total_income':total_income,'total_expense':total_expense,'balance':balance,'expenselimits':json.dumps(expenselimits)})

