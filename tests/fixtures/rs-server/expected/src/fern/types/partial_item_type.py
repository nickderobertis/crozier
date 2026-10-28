

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PartialItemType(enum.StrEnum):
    FEATURE = "Feature"

    def visit(self, feature: typing.Callable[[], T_Result]) -> T_Result:
        if self is PartialItemType.FEATURE:
            return feature()
