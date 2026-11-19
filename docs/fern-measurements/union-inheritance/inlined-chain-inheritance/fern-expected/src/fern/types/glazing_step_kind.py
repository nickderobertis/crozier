

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GlazingStepKind(enum.StrEnum):
    GLAZING = "glazing"

    def visit(self, glazing: typing.Callable[[], T_Result]) -> T_Result:
        if self is GlazingStepKind.GLAZING:
            return glazing()
