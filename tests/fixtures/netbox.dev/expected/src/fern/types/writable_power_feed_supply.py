

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WritablePowerFeedSupply(enum.StrEnum):
    AC = "ac"
    DC = "dc"

    def visit(self, ac: typing.Callable[[], T_Result], dc: typing.Callable[[], T_Result]) -> T_Result:
        if self is WritablePowerFeedSupply.AC:
            return ac()
        if self is WritablePowerFeedSupply.DC:
            return dc()
