# Generated by Django 4.2 on 2023-05-16 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_draft_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='pic',
            field=models.FileField(blank=True, upload_to='Profiles/'),
        ),
    ]
