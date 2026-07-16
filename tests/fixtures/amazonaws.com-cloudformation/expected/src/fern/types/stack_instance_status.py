

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class StackInstanceStatus(str, enum.Enum):
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
