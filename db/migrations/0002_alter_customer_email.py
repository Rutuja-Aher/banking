# Generated by Django 3.2.24 on 2024-03-03 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
