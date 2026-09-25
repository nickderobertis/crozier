

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EngineBaseType(enum.StrEnum):
    THERMIC = "Thermic"
    ELECTRIC = "Electric"

    def visit(self, thermic: typing.Callable[[], T_Result], electric: typing.Callable[[], T_Result]) -> T_Result:
        if self is EngineBaseType.THERMIC:
            return thermic()
        if self is EngineBaseType.ELECTRIC:
            return electric()
