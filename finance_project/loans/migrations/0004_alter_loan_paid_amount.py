# Generated by Django 5.1.5 on 2025-03-02 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0003_alter_loan_monthly_payment_alter_loan_progress_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='paid_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
    ]
