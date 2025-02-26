from django.shortcuts import render,redirect
from all_transactions.models import *
from datetime import date,datetime
# Create your views here.


def home(request):
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
    return render(request,'overview.html',{'total_income':total_income,'total_expense':total_expense,'balance':balance})

def add_transaction(request):

    if request.method =='POST':

        amount = request.POST['amount']

        type = request.POST['transactiontype']

        try:
            type1 =PaymentMethod.objects.get(name=type)
        except PaymentMethod.DoesNotExist:
            type1 =PaymentMethod.objects.create(name=type)
            type1.save()

      

        category_name= request.POST['category']
        try:

            category = Category.objects.get(name = category_name)
        except Category.DoesNotExist:
            
            category = Category.objects.create(name = category_name)
            category.save()


        
        payment_method = request.POST['payment_method']
        description = request.POST.get('discription','')     
        date_str = request.POST.get('date')  # Get date from form input

        if date_str:  
            try:
                date1 = datetime.strptime(date_str, "%Y-%m-%d").date()  # Convert string to date
            except ValueError:
                date1 = date.today()  # Fallback to today's date if format is invalid
        else:
               date1 = date.today()  # Use today's date if no input providedobject.save()

        object = Transaction.objects.create(amount=amount,type=type1,category=category,payment_method=payment_method,description=description,date=date1)
        object.save()





    return redirect('/')