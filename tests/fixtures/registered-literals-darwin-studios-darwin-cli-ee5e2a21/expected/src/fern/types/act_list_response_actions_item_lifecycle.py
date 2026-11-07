

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActListResponseActionsItemLifecycle(enum.StrEnum):
    ACTIVE = "active"
    ENDING = "ending"
    ENDED = "ended"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        ending: typing.Callable[[], T_Result],
        ended: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ActListResponseActionsItemLifecycle.ACTIVE:
            return active()
        if self is ActListResponseActionsItemLifecycle.ENDING:
            return ending()
        if self is ActListResponseActionsItemLifecycle.ENDED:
            return ended()
