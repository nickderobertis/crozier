

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DescribeStackSetOutputStackSetStatus(enum.StrEnum):
    """
    The status of the stack set.
    """

    ACTIVE = "ACTIVE"
    DELETED = "DELETED"

    def visit(self, active: typing.Callable[[], T_Result], deleted: typing.Callable[[], T_Result]) -> T_Result:
        if self is DescribeStackSetOutputStackSetStatus.ACTIVE:
            return active()
        if self is DescribeStackSetOutputStackSetStatus.DELETED:
            return deleted()
