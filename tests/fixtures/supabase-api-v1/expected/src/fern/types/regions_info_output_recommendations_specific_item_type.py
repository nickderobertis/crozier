

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RegionsInfoOutputRecommendationsSpecificItemType(enum.StrEnum):
    SPECIFIC = "specific"

    def visit(self, specific: typing.Callable[[], T_Result]) -> T_Result:
        if self is RegionsInfoOutputRecommendationsSpecificItemType.SPECIFIC:
            return specific()
