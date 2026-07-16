

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PowerFeedSupplyValue(str, enum.Enum):
    AC = "ac"
    DC = "dc"

    def visit(self, ac: typing.Callable[[], T_Result], dc: typing.Callable[[], T_Result]) -> T_Result:
        if self is PowerFeedSupplyValue.AC:
            return ac()
        if self is PowerFeedSupplyValue.DC:
            return dc()
