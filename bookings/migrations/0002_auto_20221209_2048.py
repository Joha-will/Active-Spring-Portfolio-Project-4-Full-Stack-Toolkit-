# Generated by Django 3.2.16 on 2022-12-09 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='booking_time',
            new_name='booking_date_time',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='booking_date',
        ),
    ]
