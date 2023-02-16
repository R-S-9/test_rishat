from django.test import TestCase, RequestFactory

from ...models import Item
from ...item.resource import ItemStripe


class ItemStripeTest(TestCase):
    def setUp(self) -> None:
        self.item = Item.objects.create(
            name="Тест товара",
            description="Описание товара",
            price_rub=1234.99,
            price_usd=123.99,
        )

        self.factory = RequestFactory()
        assert self.item

    def test_get(self):
        request = self.factory.get('')
        request.content_type = 'application/json'
        response = ItemStripe.as_view()(request, self.item.id)

        assert response.status_code == 200
