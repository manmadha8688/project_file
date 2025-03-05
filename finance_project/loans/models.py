from django.db import models

# Create your models here.
class Loan(models.Model):

    lender_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    interest_rate = models.FloatField()
    paid_amount = models.DecimalField(max_digits=12, decimal_places=2,default=0.00)
    loan_term = models.IntegerField()
    loan_date = models.DateField()
    due_date = models.DateField()
    interest_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)  # Total Interest
    total_payable = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)  # Principal + Interest
    remaining_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    monthly_payment = models.DecimalField(max_digits=12, decimal_places=2,default=0.00)
    remaining_months = models.IntegerField(default=0)
    progress= models.DecimalField(max_digits=12, decimal_places=2,default=100)
    

    def __str__(self):
        return (self.leader_name+" -- "+self.amount)
    