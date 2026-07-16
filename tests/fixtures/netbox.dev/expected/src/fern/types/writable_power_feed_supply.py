

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WritablePowerFeedSupply(str, enum.Enum):
    AC = "ac"
    DC = "dc"

    def visit(self, ac: typing.Callable[[], T_Result], dc: typing.Callable[[], T_Result]) -> T_Result:
        if self is WritablePowerFeedSupply.AC:
            return ac()
        if self is WritablePowerFeedSupply.DC:
            return dc()
