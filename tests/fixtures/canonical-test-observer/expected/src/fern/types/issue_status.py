

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IssueStatus(enum.StrEnum):
    UNKNOWN = "unknown"
    OPEN = "open"
    CLOSED = "closed"

    def visit(
        self,
        unknown: typing.Callable[[], T_Result],
        open: typing.Callable[[], T_Result],
        closed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IssueStatus.UNKNOWN:
            return unknown()
        if self is IssueStatus.OPEN:
            return open()
        if self is IssueStatus.CLOSED:
            return closed()
