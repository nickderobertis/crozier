

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DisplayConfigCellOutput(enum.StrEnum):
    ABOVE = "above"
    BELOW = "below"

    def visit(self, above: typing.Callable[[], T_Result], below: typing.Callable[[], T_Result]) -> T_Result:
        if self is DisplayConfigCellOutput.ABOVE:
            return above()
        if self is DisplayConfigCellOutput.BELOW:
            return below()
