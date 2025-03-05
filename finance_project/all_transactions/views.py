from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from datetime import date,datetime
from setexpenselimit.models import ExpensesLimits
from decimal import Decimal
# Create your views here.
def home(request):
    
    categories = Category.objects.all()
    transactions = Transaction.objects.all()
    if request.method == "POST":
        start_date = request.POST.get("start-date")
        end_date = request.POST.get("end-date")
        category = request.POST.get("category")
        type = request.POST.get("type")

        # Apply filters
        if start_date:
            transactions = transactions.filter(date__gte=start_date)
        if end_date:
            transactions = transactions.filter(date__lte=end_date)
        if category:
            try:
                categorys= Category.objects.get(name=category)
                if categorys:
                    transactions = transactions.filter(category=categorys)  
            except Category.DoesNotExist:
                pass

        # Apply type filter
        if type:
            type1 = PaymentMethod.objects.get(name=type)
            if type1:
                transactions = transactions.filter(type=type1)

   

    return render(request,'transactions.html',{'all_transactions':transactions,'categories':categories})

def update_expenselimits_ondelete(filtered_objects):

    for object in filtered_objects:
        try:
            limit_object= ExpensesLimits.objects.get(category=object.category) 
            limit_object.spent -= object.amount
            limit_object.save()
        except:
            pass
    
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

        if type=='expense':
            try:
                category_limit = ExpensesLimits.objects.get(category=category)
                
                category_limit.spent += Decimal(amount)
                category_limit.save()
            except ExpensesLimits.DoesNotExist:
                pass


    return redirect('home')



def delete_transactions(request):
    
    if request.method == "POST":
        selected_ids = request.POST.getlist('selected_transactions')

        objects = Transaction.objects.filter(id__in=selected_ids)

        type1 = PaymentMethod.objects.get(name='expense')  # Ensure 'type' is related correctly
        filtered_objects = objects.filter(type=type1)
        
        
        messages.success(request, f"Selected transactions deleted successfully.")

        if filtered_objects.exists():
            update_expenselimits_ondelete(filtered_objects)
        objects.delete()

       
        return redirect('all_transactions')

