

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WritablePowerFeedType(str, enum.Enum):
    PRIMARY = "primary"
    REDUNDANT = "redundant"

    def visit(self, primary: typing.Callable[[], T_Result], redundant: typing.Callable[[], T_Result]) -> T_Result:
        if self is WritablePowerFeedType.PRIMARY:
            return primary()
        if self is WritablePowerFeedType.REDUNDANT:
            return redundant()
