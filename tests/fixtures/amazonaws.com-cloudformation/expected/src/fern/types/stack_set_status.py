

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StackSetStatus(enum.StrEnum):
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"

    def visit(self, active: typing.Callable[[], T_Result], deleted: typing.Callable[[], T_Result]) -> T_Result:
        if self is StackSetStatus.ACTIVE:
            return active()
        if self is StackSetStatus.DELETED:
            return deleted()
