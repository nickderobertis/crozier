

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class DeclareIntentResponseSecurityTier(enum.StrEnum):
    ROUTINE = "routine"
    STANDARD = "standard"
    ELEVATED = "elevated"
    MAXIMUM = "maximum"

    def visit(
        self,
        routine: typing.Callable[[], T_Result],
        standard: typing.Callable[[], T_Result],
        elevated: typing.Callable[[], T_Result],
        maximum: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DeclareIntentResponseSecurityTier.ROUTINE:
            return routine()
        if self is DeclareIntentResponseSecurityTier.STANDARD:
            return standard()
        if self is DeclareIntentResponseSecurityTier.ELEVATED:
            return elevated()
        if self is DeclareIntentResponseSecurityTier.MAXIMUM:
            return maximum()
