

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StackResourceDriftStatus(enum.StrEnum):
    IN_SYNC = "IN_SYNC"
    MODIFIED = "MODIFIED"
    DELETED = "DELETED"
    NOT_CHECKED = "NOT_CHECKED"

    def visit(
        self,
        in_sync: typing.Callable[[], T_Result],
        modified: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
        not_checked: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StackResourceDriftStatus.IN_SYNC:
            return in_sync()
        if self is StackResourceDriftStatus.MODIFIED:
            return modified()
        if self is StackResourceDriftStatus.DELETED:
            return deleted()
        if self is StackResourceDriftStatus.NOT_CHECKED:
            return not_checked()
