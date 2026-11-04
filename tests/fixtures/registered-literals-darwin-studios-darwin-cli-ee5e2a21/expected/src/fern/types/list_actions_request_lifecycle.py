

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListActionsRequestLifecycle(enum.StrEnum):
    CURRENT = "current"
    ENDED = "ended"
    ALL = "all"

    def visit(
        self,
        current: typing.Callable[[], T_Result],
        ended: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListActionsRequestLifecycle.CURRENT:
            return current()
        if self is ListActionsRequestLifecycle.ENDED:
            return ended()
        if self is ListActionsRequestLifecycle.ALL:
            return all_()
