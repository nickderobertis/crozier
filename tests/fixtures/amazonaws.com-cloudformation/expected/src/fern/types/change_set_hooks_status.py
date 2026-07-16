

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChangeSetHooksStatus(enum.StrEnum):
    PLANNING = "PLANNING"
    PLANNED = "PLANNED"
    UNAVAILABLE = "UNAVAILABLE"

    def visit(
        self,
        planning: typing.Callable[[], T_Result],
        planned: typing.Callable[[], T_Result],
        unavailable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChangeSetHooksStatus.PLANNING:
            return planning()
        if self is ChangeSetHooksStatus.PLANNED:
            return planned()
        if self is ChangeSetHooksStatus.UNAVAILABLE:
            return unavailable()
