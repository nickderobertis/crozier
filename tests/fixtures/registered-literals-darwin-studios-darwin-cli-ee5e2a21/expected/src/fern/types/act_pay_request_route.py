

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActPayRequestRoute(enum.StrEnum):
    DIRECT = "direct"
    DARWIN_PAY = "darwin_pay"

    def visit(self, direct: typing.Callable[[], T_Result], darwin_pay: typing.Callable[[], T_Result]) -> T_Result:
        if self is ActPayRequestRoute.DIRECT:
            return direct()
        if self is ActPayRequestRoute.DARWIN_PAY:
            return darwin_pay()
