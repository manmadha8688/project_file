# Generated by Django 5.1.3 on 2025-01-26 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_reviews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='img',
        ),
    ]
