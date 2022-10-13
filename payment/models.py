from uuid import uuid4
from django.db import models
from clickuz import ClickUz

from mainapp.models import Travel


class Order(models.Model):
    uid = models.CharField(max_length=50, default=str(uuid4()), editable=False)

    is_approved = models.BooleanField(default=False, verbose_name='Tasdiqlangan holati: ')
    is_payed = models.BooleanField(default=False, verbose_name="To'lanish holati: ")

    place = models.ForeignKey(Travel, on_delete=models.CASCADE, verbose_name='Sayohat')

    customer_full_name = models.CharField(max_length=255)
    customer_phone_number = models.CharField(max_length=255)

    def __str__(self):
        return f'Order {self.uid}'

    def mark_as_payed(self):
        self.is_payed = True
        self.save()

    def get_payment_url(self, return_url: str) -> str:
        if self.is_payed:
            return '#'
        if not self.is_approved:
            return '#'
        return ClickUz.generate_url(self.id, self.place.narxi, return_url)
