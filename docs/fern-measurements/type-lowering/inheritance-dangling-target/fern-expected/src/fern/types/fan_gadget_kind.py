

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FanGadgetKind(enum.StrEnum):
    FAN = "FAN"

    def visit(self, fan: typing.Callable[[], T_Result]) -> T_Result:
        if self is FanGadgetKind.FAN:
            return fan()
