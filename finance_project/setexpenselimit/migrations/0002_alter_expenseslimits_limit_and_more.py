# Generated by Django 5.1.5 on 2025-02-26 20:12

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setexpenselimit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenseslimits',
            name='limit',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=10),
        ),
        migrations.AlterField(
            model_name='expenseslimits',
            name='remaining',
            field=models.DecimalField(decimal_places=2, default=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=10), max_digits=10),
        ),
    ]
