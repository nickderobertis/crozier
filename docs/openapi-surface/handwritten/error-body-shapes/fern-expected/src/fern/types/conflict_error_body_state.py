

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConflictErrorBodyState(enum.StrEnum):
    SCHEDULED = "scheduled"
    ACTIVE = "active"

    def visit(self, scheduled: typing.Callable[[], T_Result], active: typing.Callable[[], T_Result]) -> T_Result:
        if self is ConflictErrorBodyState.SCHEDULED:
            return scheduled()
        if self is ConflictErrorBodyState.ACTIVE:
            return active()
