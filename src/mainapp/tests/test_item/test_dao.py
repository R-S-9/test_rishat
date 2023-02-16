from django.test import TestCase

from ...models import Item
from ...item.dao import ItemDAO


class ItemDAOTest(TestCase):
    def setUp(self) -> None:
        self.item = Item.objects.create(
            name="Тест товара",
            description="Описание товара",
            price_rub=1234.99,
            price_usd=123.99,
        )

        assert self.item

    def test_get_item_by_id(self):
        assert ItemDAO.get_item_by_id(self.item.id)[0] == self.item
