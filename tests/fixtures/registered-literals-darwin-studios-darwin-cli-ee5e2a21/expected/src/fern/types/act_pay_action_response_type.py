

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActPayActionResponseType(enum.StrEnum):
    PAY = "pay"

    def visit(self, pay: typing.Callable[[], T_Result]) -> T_Result:
        if self is ActPayActionResponseType.PAY:
            return pay()
