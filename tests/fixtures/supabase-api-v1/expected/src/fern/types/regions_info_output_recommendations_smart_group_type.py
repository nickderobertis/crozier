

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RegionsInfoOutputRecommendationsSmartGroupType(enum.StrEnum):
    SMART_GROUP = "smartGroup"

    def visit(self, smart_group: typing.Callable[[], T_Result]) -> T_Result:
        if self is RegionsInfoOutputRecommendationsSmartGroupType.SMART_GROUP:
            return smart_group()
