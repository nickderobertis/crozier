

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StackDriftStatus(enum.StrEnum):
    DRIFTED = "DRIFTED"
    IN_SYNC = "IN_SYNC"
    UNKNOWN = "UNKNOWN"
    NOT_CHECKED = "NOT_CHECKED"

    def visit(
        self,
        drifted: typing.Callable[[], T_Result],
        in_sync: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
        not_checked: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StackDriftStatus.DRIFTED:
            return drifted()
        if self is StackDriftStatus.IN_SYNC:
            return in_sync()
        if self is StackDriftStatus.UNKNOWN:
            return unknown()
        if self is StackDriftStatus.NOT_CHECKED:
            return not_checked()
