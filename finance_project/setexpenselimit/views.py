from django.shortcuts import render,redirect
from .models import ExpensesLimits
from all_transactions.models import Transaction,Category,PaymentMethod
from decimal import Decimal
from django.db.models import Sum
from django.contrib import messages
# Create your views here.

def home(request):
    try:
        expenselimits = ExpensesLimits.objects.all()
    except ExpensesLimits.DoesNotExist:
        pass

    if request.method == "POST":
        category_limit = request.POST.get('category')
        limit_is = request.POST.get('limit')

       
        try:
            category = Category.objects.get(name=category_limit)
        except Category.DoesNotExist:
            category = Category.objects.create(name=category_limit)
            category.save()
        try:
            limit_is = limit_is.strip()
            limit = Decimal(limit_is)
        except (ValueError, TypeError):
            limit = Decimal(0)
        try:
            expenselimit = ExpensesLimits.objects.get(category=category)
            messages.info(request,category_limit+' limit is already added')
            return redirect('setexpenselimit')
        except ExpensesLimits.DoesNotExist:
            expenselimit = ExpensesLimits.objects.create(category=category,limit=limit)
            expenselimit.save()

    type= PaymentMethod.objects.get(name='expense')
    
    for object in expenselimits:

        object.remaining = object.limit - object.spent
        object.save()


    return render(request,'setexpenselimit.html',{'expenselimits':expenselimits})