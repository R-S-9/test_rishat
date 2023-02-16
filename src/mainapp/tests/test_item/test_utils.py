from django.test import TestCase

from ...models import Item
from ...item.utils import ItemUtil


class ItemUtilTest(TestCase):
    def setUp(self) -> None:
        self.item = Item.objects.create(
            name="Тест товара",
            description="Описание товара",
            price_rub=1234.99,
            price_usd=123.99,
        )

        assert self.item

    def test_product_data_success(self):
        response = ItemUtil.product_data(self.item.id)

        assert type(response) is list
        assert response[0]['title'] == self.item.name

    @staticmethod
    def test_product_data_error():
        response = ItemUtil.product_data(999)

        assert response is None
