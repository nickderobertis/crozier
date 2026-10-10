

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Form(enum.StrEnum):
    POLAR = "polar"
    COMPLEX = "complex"

    def visit(self, polar: typing.Callable[[], T_Result], complex_: typing.Callable[[], T_Result]) -> T_Result:
        if self is Form.POLAR:
            return polar()
        if self is Form.COMPLEX:
            return complex_()
