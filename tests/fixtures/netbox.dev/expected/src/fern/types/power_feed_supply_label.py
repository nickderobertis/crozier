

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PowerFeedSupplyLabel(str, enum.Enum):
    AC = "AC"
    DC = "DC"

    def visit(self, ac: typing.Callable[[], T_Result], dc: typing.Callable[[], T_Result]) -> T_Result:
        if self is PowerFeedSupplyLabel.AC:
            return ac()
        if self is PowerFeedSupplyLabel.DC:
            return dc()
