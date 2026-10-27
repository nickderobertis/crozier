

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StacPydanticCollectionCollectionOutputType(enum.StrEnum):
    COLLECTION = "Collection"

    def visit(self, collection: typing.Callable[[], T_Result]) -> T_Result:
        if self is StacPydanticCollectionCollectionOutputType.COLLECTION:
            return collection()
