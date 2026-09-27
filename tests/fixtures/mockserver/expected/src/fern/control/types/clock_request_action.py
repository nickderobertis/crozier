

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ClockRequestAction(enum.StrEnum):
    """
    freeze: freeze the clock at the given instant (or current time if instant is omitted); advance: advance the frozen clock by durationMillis (freezes first if not already frozen); reset: reset the clock to real wall-clock time
    """

    FREEZE = "freeze"
    ADVANCE = "advance"
    RESET = "reset"

    def visit(
        self,
        freeze: typing.Callable[[], T_Result],
        advance: typing.Callable[[], T_Result],
        reset: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ClockRequestAction.FREEZE:
            return freeze()
        if self is ClockRequestAction.ADVANCE:
            return advance()
        if self is ClockRequestAction.RESET:
            return reset()
