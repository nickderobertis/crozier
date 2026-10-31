

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DebStage(enum.StrEnum):
    PROPOSED = "proposed"
    UPDATES = "updates"

    def visit(self, proposed: typing.Callable[[], T_Result], updates: typing.Callable[[], T_Result]) -> T_Result:
        if self is DebStage.PROPOSED:
            return proposed()
        if self is DebStage.UPDATES:
            return updates()
