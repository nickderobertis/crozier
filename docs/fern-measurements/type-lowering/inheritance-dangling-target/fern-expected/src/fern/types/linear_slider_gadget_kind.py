

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LinearSliderGadgetKind(enum.StrEnum):
    SLIDER = "SLIDER"

    def visit(self, slider: typing.Callable[[], T_Result]) -> T_Result:
        if self is LinearSliderGadgetKind.SLIDER:
            return slider()
