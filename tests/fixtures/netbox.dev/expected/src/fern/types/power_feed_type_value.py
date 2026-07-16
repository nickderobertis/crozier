

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PowerFeedTypeValue(str, enum.Enum):
    PRIMARY = "primary"
    REDUNDANT = "redundant"

    def visit(self, primary: typing.Callable[[], T_Result], redundant: typing.Callable[[], T_Result]) -> T_Result:
        if self is PowerFeedTypeValue.PRIMARY:
            return primary()
        if self is PowerFeedTypeValue.REDUNDANT:
            return redundant()
