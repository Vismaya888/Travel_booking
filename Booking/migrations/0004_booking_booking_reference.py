# Generated by Django 5.1.2 on 2024-10-27 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0003_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_reference',
            field=models.CharField(max_length=12, null=True, unique=True),
        ),
    ]
