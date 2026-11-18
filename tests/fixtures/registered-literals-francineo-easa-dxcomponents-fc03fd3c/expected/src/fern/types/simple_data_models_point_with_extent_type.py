

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SimpleDataModelsPointWithExtentType(enum.StrEnum):
    POINT = "Point"

    def visit(self, point: typing.Callable[[], T_Result]) -> T_Result:
        if self is SimpleDataModelsPointWithExtentType.POINT:
            return point()
