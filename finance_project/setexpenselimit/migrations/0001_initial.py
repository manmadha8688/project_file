# Generated by Django 5.1.5 on 2025-02-26 19:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('all_transactions', '0003_alter_transaction_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpensesLimits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limit', models.IntegerField()),
                ('spent', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('remaining', models.DecimalField(decimal_places=2, default=models.IntegerField(), max_digits=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='all_transactions.category')),
            ],
        ),
    ]
