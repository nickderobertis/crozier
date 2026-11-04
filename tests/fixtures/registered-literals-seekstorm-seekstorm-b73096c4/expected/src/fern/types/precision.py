

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Precision(enum.StrEnum):
    """
    Vector precision
    """

    NONE = "None"
    F32 = "F32"
    I8 = "I8"

    def visit(
        self, none: typing.Callable[[], T_Result], f32: typing.Callable[[], T_Result], i8: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is Precision.NONE:
            return none()
        if self is Precision.F32:
            return f32()
        if self is Precision.I8:
            return i8()
