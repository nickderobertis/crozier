

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FlowVideoEssenceParametersComponentType(enum.StrEnum):
    """
    Picture component representation.
    """

    Y_CB_CR = "YCbCr"
    RGB = "RGB"

    def visit(self, y_cb_cr: typing.Callable[[], T_Result], rgb: typing.Callable[[], T_Result]) -> T_Result:
        if self is FlowVideoEssenceParametersComponentType.Y_CB_CR:
            return y_cb_cr()
        if self is FlowVideoEssenceParametersComponentType.RGB:
            return rgb()
