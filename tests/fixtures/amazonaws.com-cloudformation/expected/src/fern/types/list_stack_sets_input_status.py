

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListStackSetsInputStatus(enum.StrEnum):
    """
    The status of the stack sets that you want to get summary information about.
    """

    ACTIVE = "ACTIVE"
    DELETED = "DELETED"

    def visit(self, active: typing.Callable[[], T_Result], deleted: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListStackSetsInputStatus.ACTIVE:
            return active()
        if self is ListStackSetsInputStatus.DELETED:
            return deleted()
