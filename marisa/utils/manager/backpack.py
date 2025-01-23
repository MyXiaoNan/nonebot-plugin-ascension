from typing import Generic, TypeVar

from marisa.schemas.item import Item
from marisa.models import User, Backpack

from . import item_manager

T = TypeVar("T", bound=User)


class BackpackManager(Generic[T]):
    def __init__(self, user: T) -> None:
        self.user = user
        self.backpack: list[Backpack] = user.backpack
        self.items: list[Item] = [
            self._add_extra_fields(backpack_item) for backpack_item in self.backpack
        ]

    def _add_extra_fields(self, backpack_item: Backpack) -> Item:
        item = item_manager.get(backpack_item.item_id)

        item_dict = item.model_dump()
        item_dict.update(
            {
                "is_bundle": backpack_item.is_bundle,
                "is_equipped": backpack_item.is_equipped,
            }
        )

        return Item(**item_dict)

    filter = item_manager.filter
