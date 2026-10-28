

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MultiPointType(enum.StrEnum):
    MULTI_POINT = "MultiPoint"

    def visit(self, multi_point: typing.Callable[[], T_Result]) -> T_Result:
        if self is MultiPointType.MULTI_POINT:
            return multi_point()
