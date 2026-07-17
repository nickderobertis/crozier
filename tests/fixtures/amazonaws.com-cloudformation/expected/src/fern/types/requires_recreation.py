

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RequiresRecreation(enum.StrEnum):
    NEVER = "Never"
    CONDITIONALLY = "Conditionally"
    ALWAYS = "Always"

    def visit(
        self,
        never: typing.Callable[[], T_Result],
        conditionally: typing.Callable[[], T_Result],
        always: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RequiresRecreation.NEVER:
            return never()
        if self is RequiresRecreation.CONDITIONALLY:
            return conditionally()
        if self is RequiresRecreation.ALWAYS:
            return always()
