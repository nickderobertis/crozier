

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PassBand(enum.StrEnum):
    S = "s"
    X = "x"
    KA = "ka"

    def visit(
        self, s: typing.Callable[[], T_Result], x: typing.Callable[[], T_Result], ka: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is PassBand.S:
            return s()
        if self is PassBand.X:
            return x()
        if self is PassBand.KA:
            return ka()
