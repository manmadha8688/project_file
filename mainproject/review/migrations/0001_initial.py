# Generated by Django 5.1.5 on 2025-02-23 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratting', models.IntegerField()),
                ('discription', models.TextField()),
            ],
        ),
    ]
