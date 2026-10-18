

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RegionsInfoOutputAllSpecificItemStatus(enum.StrEnum):
    CAPACITY = "capacity"
    OTHER = "other"

    def visit(self, capacity: typing.Callable[[], T_Result], other: typing.Callable[[], T_Result]) -> T_Result:
        if self is RegionsInfoOutputAllSpecificItemStatus.CAPACITY:
            return capacity()
        if self is RegionsInfoOutputAllSpecificItemStatus.OTHER:
            return other()
