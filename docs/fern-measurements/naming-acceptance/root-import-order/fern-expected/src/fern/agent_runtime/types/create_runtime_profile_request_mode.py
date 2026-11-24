

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateRuntimeProfileRequestMode(enum.StrEnum):
    WARM = "warm"
    COLD = "cold"

    def visit(self, warm: typing.Callable[[], T_Result], cold: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateRuntimeProfileRequestMode.WARM:
            return warm()
        if self is CreateRuntimeProfileRequestMode.COLD:
            return cold()
