

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SimpleDataModelsMultiPointType(enum.StrEnum):
    MULTI_POINT = "MultiPoint"

    def visit(self, multi_point: typing.Callable[[], T_Result]) -> T_Result:
        if self is SimpleDataModelsMultiPointType.MULTI_POINT:
            return multi_point()
