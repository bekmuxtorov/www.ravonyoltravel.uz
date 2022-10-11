from clickuz.views import ClickUzMerchantAPIView
from clickuz import ClickUz

from .models import Order


# Create your views here.
class OrderCheckAndPayment(ClickUz):
    def check_order(self, order_id: str, amount: str):
        order = Order.objects.filter(pk=order_id).first()

        if order is None:
            return self.ORDER_NOT_FOUND

        if order.is_payed:
            return self.ORDER_NOT_FOUND

        if order.place.narxi != amount:
            return self.INVALID_AMOUNT

        return self.ORDER_FOUND

    def successfully_payment(self, order_id: str, transaction: object):
        order = Order.objects.get(pk=order_id)
        order.mark_as_payed()


class TestView(ClickUzMerchantAPIView):
    VALIDATE_CLASS = OrderCheckAndPayment
