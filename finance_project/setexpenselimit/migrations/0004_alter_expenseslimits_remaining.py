# Generated by Django 5.1.5 on 2025-02-26 20:37

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setexpenselimit', '0003_alter_expenseslimits_limit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenseslimits',
            name='remaining',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=10),
        ),
    ]
