

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RegionsInfoOutputRecommendationsSpecificItemStatus(enum.StrEnum):
    CAPACITY = "capacity"
    OTHER = "other"

    def visit(self, capacity: typing.Callable[[], T_Result], other: typing.Callable[[], T_Result]) -> T_Result:
        if self is RegionsInfoOutputRecommendationsSpecificItemStatus.CAPACITY:
            return capacity()
        if self is RegionsInfoOutputRecommendationsSpecificItemStatus.OTHER:
            return other()
