from django.db import models

from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField

from django.core.validators import MaxValueValidator, MinValueValidator

import datetime

pool_timings = (
    ('08:00', '08:00'),
    ('09:00', '09:00'),
    ('10:00', '10:00'),
    ('11:00', '11:00'),
    ('12:00', '12:00'),
    ('13:00', '13:00'),
    ('14:00', '14:00'),
    ('15:00', '15:00'),
    ('16:00', '16:00'),
    ('17:00', '17:00'),
    ('18:00', '18:00'),
)
pool_status = (

    ('Pending', 'Pending'),

    ('Confirmed', 'Confirmed'),

    (
        'Rejected, try booking on a different hour',
        'Rejected, try booking on a different hour',
    ),
)


class Booking(models.Model):
    "The booking model"

    booking_id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=200, blank=False, default="")

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='customer', null=True)

    email = models.EmailField(max_length=254)

    no_of_persons = models.IntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])

    booking_date = models.DateField()

    booking_time = models.CharField(
        max_length=10, default='08:00', choices=pool_timings)

    phone_number = PhoneNumberField(blank=True, null=True)

    booking_status = models.CharField(
        max_length=50, choices=pool_status, default="Pending")

    booked_on = models.DateTimeField(auto_now_add=True)

    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-booked_on']

    def __str__(self):
        return str(self.name)
