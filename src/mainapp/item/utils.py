from typing import Optional, Any

from .dao import ItemDAO


class ItemUtil:
    @staticmethod
    # def product_data(item_id: int) -> Optional[list[dict[str, Any]]] or None:
    def product_data(item_id: int):
        qs_item = ItemDAO.get_item_by_id(item_id)

        if not qs_item:
            return None

        list_item = []

        for field in qs_item:
            list_item.append(
                {
                    'title': field.name,
                    'description': field.description,
                    'price_rub': field.price_rub,
                    'price_usd': field.price_usd,
                }
            )
        return list_item
