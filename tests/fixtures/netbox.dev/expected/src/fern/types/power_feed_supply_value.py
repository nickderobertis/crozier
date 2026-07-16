

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PowerFeedSupplyValue(enum.StrEnum):
    AC = "ac"
    DC = "dc"

    def visit(self, ac: typing.Callable[[], T_Result], dc: typing.Callable[[], T_Result]) -> T_Result:
        if self is PowerFeedSupplyValue.AC:
            return ac()
        if self is PowerFeedSupplyValue.DC:
            return dc()
