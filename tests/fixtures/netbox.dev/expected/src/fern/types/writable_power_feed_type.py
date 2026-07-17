

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WritablePowerFeedType(enum.StrEnum):
    PRIMARY = "primary"
    REDUNDANT = "redundant"

    def visit(self, primary: typing.Callable[[], T_Result], redundant: typing.Callable[[], T_Result]) -> T_Result:
        if self is WritablePowerFeedType.PRIMARY:
            return primary()
        if self is WritablePowerFeedType.REDUNDANT:
            return redundant()
