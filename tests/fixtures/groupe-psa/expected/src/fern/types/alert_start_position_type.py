

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AlertStartPositionType(enum.StrEnum):
    FEATURE = "Feature"

    def visit(self, feature: typing.Callable[[], T_Result]) -> T_Result:
        if self is AlertStartPositionType.FEATURE:
            return feature()
