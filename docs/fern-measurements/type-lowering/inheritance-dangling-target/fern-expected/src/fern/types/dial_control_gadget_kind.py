

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DialControlGadgetKind(enum.StrEnum):
    DIAL = "DIAL"

    def visit(self, dial: typing.Callable[[], T_Result]) -> T_Result:
        if self is DialControlGadgetKind.DIAL:
            return dial()
