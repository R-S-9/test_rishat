from django.test import TestCase

from ...models import Item
from ...payment.utils import PaymentUtil


class PaymentUtilTest(TestCase):
    def setUp(self) -> None:
        self.item = Item.objects.create(
            name="Тест товара",
            description="Описание товара",
            price_rub=1234.99,
            price_usd=123.99,
        )

        assert self.item

    def test_create_session_stripe_success(self):
        response = PaymentUtil().create_session_stripe(
            self.item.id, 'usd'
        )

        assert len(response) == 66
        assert type(response) is str

    @staticmethod
    def test_create_session_stripe_error():
        response = PaymentUtil().create_session_stripe(
            9999, 'usd'
        )

        assert type(response) is dict
        assert response['data'] is None
