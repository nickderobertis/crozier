

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CollectionItemChangedPayloadTriggerType(enum.StrEnum):
    """
    The type of event that triggered the request
    """

    COLLECTION_ITEM_CHANGED = "collection_item_changed"

    def visit(self, collection_item_changed: typing.Callable[[], T_Result]) -> T_Result:
        if self is CollectionItemChangedPayloadTriggerType.COLLECTION_ITEM_CHANGED:
            return collection_item_changed()
