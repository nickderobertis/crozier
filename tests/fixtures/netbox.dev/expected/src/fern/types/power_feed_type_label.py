

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PowerFeedTypeLabel(enum.StrEnum):
    PRIMARY = "Primary"
    REDUNDANT = "Redundant"

    def visit(self, primary: typing.Callable[[], T_Result], redundant: typing.Callable[[], T_Result]) -> T_Result:
        if self is PowerFeedTypeLabel.PRIMARY:
            return primary()
        if self is PowerFeedTypeLabel.REDUNDANT:
            return redundant()
