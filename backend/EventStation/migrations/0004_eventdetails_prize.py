# Generated by Django 5.0.6 on 2024-08-09 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventStation', '0003_eventdetails_approve'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventdetails',
            name='prize',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]