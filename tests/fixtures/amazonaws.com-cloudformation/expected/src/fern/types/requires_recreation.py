

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class RequiresRecreation(str, enum.Enum):
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
