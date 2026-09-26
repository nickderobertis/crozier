

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PositionBaseType(enum.StrEnum):
    FEATURE = "Feature"

    def visit(self, feature: typing.Callable[[], T_Result]) -> T_Result:
        if self is PositionBaseType.FEATURE:
            return feature()
