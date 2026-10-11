

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Phase(enum.StrEnum):
    PREPARATION = "preparation"
    RECORDING = "recording"

    def visit(self, preparation: typing.Callable[[], T_Result], recording: typing.Callable[[], T_Result]) -> T_Result:
        if self is Phase.PREPARATION:
            return preparation()
        if self is Phase.RECORDING:
            return recording()
