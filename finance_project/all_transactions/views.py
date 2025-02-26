from django.shortcuts import render

from .models import *
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