from django.shortcuts import render,redirect
from .models import Loan
import math
# Create your views here.

def home(request):
    if request.method == "POST":
        
        lendername = request.POST["lenderName"]
        amount = float(request.POST["amount"])
        interestrate = float(request.POST["interestrate"])
        duedate = request.POST["duedate"]
        loandate = request.POST["loandate"]
        paidamount = float(request.POST["paidamount"])
        loanterm = int(request.POST["loanterm"])

        monthlyinterestrate = interestrate / 100 / 12
        if monthlyinterestrate > 0:
            monthlyPayment = (amount * monthlyinterestrate) / (1 - math.pow(1 + monthlyinterestrate, -loanterm))
        else:
            monthlyPayment = amount / loanterm  # For 0% interest loans
        total_interest = (monthlyPayment * loanterm) - amount
        totalpayable = amount + total_interest
        remainingAmount = totalpayable - paidamount

        
        progress = (paidamount / totalpayable) * 100
        remaining_months = remainingAmount / monthlyPayment
        remaining_months = int(math.ceil(remaining_months)) 

        object = Loan.objects.create(lender_name=lendername,amount=amount,interest_rate=interestrate,paid_amount=paidamount,loan_term=loanterm,loan_date=loandate,due_date=duedate,monthly_payment=monthlyPayment,remaining_months=remaining_months,progress=progress,total_payable=totalpayable,remaining_balance=remainingAmount,interest_amount=total_interest)
        object.save()

        return redirect('loans')

    loans = Loan.objects.all()
        
    return render(request,'loans.html',{'loans':loans})
