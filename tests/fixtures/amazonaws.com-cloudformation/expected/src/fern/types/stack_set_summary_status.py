

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StackSetSummaryStatus(enum.StrEnum):
    """
    The status of the stack set.
    """

    ACTIVE = "ACTIVE"
    DELETED = "DELETED"

    def visit(self, active: typing.Callable[[], T_Result], deleted: typing.Callable[[], T_Result]) -> T_Result:
        if self is StackSetSummaryStatus.ACTIVE:
            return active()
        if self is StackSetSummaryStatus.DELETED:
            return deleted()
