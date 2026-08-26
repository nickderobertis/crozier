

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarimoInterruptionErrorType(enum.StrEnum):
    INTERRUPTION = "interruption"

    def visit(self, interruption: typing.Callable[[], T_Result]) -> T_Result:
        if self is MarimoInterruptionErrorType.INTERRUPTION:
            return interruption()
