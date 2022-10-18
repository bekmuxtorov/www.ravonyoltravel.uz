from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User
from clickuz import ClickUz

from mainapp.models import Travel


class Order(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Foydalanuvchi identifikatsiya raqami'
    )

    is_approved = models.BooleanField(default=False, verbose_name='Tasdiqlangan holati: ')
    is_payed = models.BooleanField(default=False, verbose_name="To'lanish holati: ")

    place = models.ForeignKey(Travel, on_delete=models.CASCADE, verbose_name='Sayohat')

    customer_full_name = models.CharField(max_length=255)
    customer_phone_number = models.CharField(max_length=255)

    def __str__(self):
        return f'Order {self.place.qayerdan} -> {self.place.qayerga} | {self.pk}'

    def mark_as_payed(self):
        self.is_payed = True
        self.save()

    def get_payment_url(self, return_url: str = '') -> str:
        if self.is_payed:
            return 'ALREADY_PAYED'
        if not self.is_approved:
            return 'NOT_APPROVED'
        return ClickUz.generate_url(self.id, self.place.narxi, return_url)
