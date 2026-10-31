

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CollectionType(enum.StrEnum):
    COLLECTION = "collection"
    TIMESERIES = "timeseries"

    def visit(self, collection: typing.Callable[[], T_Result], timeseries: typing.Callable[[], T_Result]) -> T_Result:
        if self is CollectionType.COLLECTION:
            return collection()
        if self is CollectionType.TIMESERIES:
            return timeseries()
