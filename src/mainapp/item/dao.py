from typing import Optional

from ..models import Item


class ItemDAO:
    @staticmethod
    def get_item_by_id(item_id: int) -> Optional[Item] or None:
        item_data = Item.objects.filter(id=item_id)
        if item_data.exists():
            return item_data
        return None
