

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SessionProblemDetailsItemOneIssue(enum.StrEnum):
    DOME_SHUT = "DOME_SHUT"

    def visit(self, dome_shut: typing.Callable[[], T_Result]) -> T_Result:
        if self is SessionProblemDetailsItemOneIssue.DOME_SHUT:
            return dome_shut()
