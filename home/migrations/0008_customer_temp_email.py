# Generated by Django 4.2 on 2023-04-15 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_customer_experience_customer_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='temp_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]