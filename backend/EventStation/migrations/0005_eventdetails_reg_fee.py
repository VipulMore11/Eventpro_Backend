# Generated by Django 5.0.6 on 2024-08-11 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventStation', '0004_eventdetails_prize'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventdetails',
            name='reg_fee',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]