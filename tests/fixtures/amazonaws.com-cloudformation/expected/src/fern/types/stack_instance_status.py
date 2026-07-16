

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StackInstanceStatus(enum.StrEnum):
    CURRENT = "CURRENT"
    OUTDATED = "OUTDATED"
    INOPERABLE = "INOPERABLE"

    def visit(
        self,
        current: typing.Callable[[], T_Result],
        outdated: typing.Callable[[], T_Result],
        inoperable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StackInstanceStatus.CURRENT:
            return current()
        if self is StackInstanceStatus.OUTDATED:
            return outdated()
        if self is StackInstanceStatus.INOPERABLE:
            return inoperable()
