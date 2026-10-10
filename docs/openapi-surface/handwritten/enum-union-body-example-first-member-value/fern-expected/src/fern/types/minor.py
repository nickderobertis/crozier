

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Minor(enum.StrEnum):
    CAMBRIDGE = "cambridge"
    OXFORD = "oxford"

    def visit(self, cambridge: typing.Callable[[], T_Result], oxford: typing.Callable[[], T_Result]) -> T_Result:
        if self is Minor.CAMBRIDGE:
            return cambridge()
        if self is Minor.OXFORD:
            return oxford()
