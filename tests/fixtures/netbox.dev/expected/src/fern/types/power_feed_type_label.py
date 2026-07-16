

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PowerFeedTypeLabel(str, enum.Enum):
    PRIMARY = "Primary"
    REDUNDANT = "Redundant"

    def visit(self, primary: typing.Callable[[], T_Result], redundant: typing.Callable[[], T_Result]) -> T_Result:
        if self is PowerFeedTypeLabel.PRIMARY:
            return primary()
        if self is PowerFeedTypeLabel.REDUNDANT:
            return redundant()
