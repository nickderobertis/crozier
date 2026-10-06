

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Weave(enum.StrEnum):
    PLAIN = "plain"
    TWILL = "twill"
    SATIN = "satin"

    def visit(
        self,
        plain: typing.Callable[[], T_Result],
        twill: typing.Callable[[], T_Result],
        satin: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Weave.PLAIN:
            return plain()
        if self is Weave.TWILL:
            return twill()
        if self is Weave.SATIN:
            return satin()
