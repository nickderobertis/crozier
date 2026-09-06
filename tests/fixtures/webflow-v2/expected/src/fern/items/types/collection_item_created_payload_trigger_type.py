

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CollectionItemCreatedPayloadTriggerType(enum.StrEnum):
    """
    The type of event that triggered the request
    """

    COLLECTION_ITEM_CREATED = "collection_item_created"

    def visit(self, collection_item_created: typing.Callable[[], T_Result]) -> T_Result:
        if self is CollectionItemCreatedPayloadTriggerType.COLLECTION_ITEM_CREATED:
            return collection_item_created()
