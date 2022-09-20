from django.shortcuts import render
from clickuz.views import ClickUzMerchantAPIView
from clickuz import ClickUz

from mainapp.models import Travel
# Create your views here.
class OrderCheckAndPayment(ClickUz):
    def check_order(self, order_id: str, amount: str):
        order = Travel.objects.filter(pk=order_id).first()
        if order is None:
            return self.ORDER_NOT_FOUND
        if order.amount != amount:
            return self.INVALID_AMOUNT

        return self.ORDER_FOUND

    def successfully_payment(self, order_id: str, transaction: object):
        order = Travel.objects.get(pk=order_id)
        order.change_status(True)

class TestView(ClickUzMerchantAPIView):
    VALIDATE_CLASS = OrderCheckAndPayment