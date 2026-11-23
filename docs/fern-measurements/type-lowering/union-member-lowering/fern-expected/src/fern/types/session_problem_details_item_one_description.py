

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SessionProblemDetailsItemOneDescription(enum.StrEnum):
    THE_DOME_IS_SHUT = "The dome is shut."

    def visit(self, the_dome_is_shut: typing.Callable[[], T_Result]) -> T_Result:
        if self is SessionProblemDetailsItemOneDescription.THE_DOME_IS_SHUT:
            return the_dome_is_shut()
