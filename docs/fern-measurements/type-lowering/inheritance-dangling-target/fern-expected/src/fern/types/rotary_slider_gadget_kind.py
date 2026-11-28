

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RotarySliderGadgetKind(enum.StrEnum):
    SLIDER = "SLIDER"

    def visit(self, slider: typing.Callable[[], T_Result]) -> T_Result:
        if self is RotarySliderGadgetKind.SLIDER:
            return slider()
