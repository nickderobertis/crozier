

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FlowVideoEssenceParametersColorspace(enum.StrEnum):
    """
    Colorspace used for the video
    """

    BT601 = "BT601"
    BT709 = "BT709"
    BT2020 = "BT2020"
    BT2100 = "BT2100"

    def visit(
        self,
        bt601: typing.Callable[[], T_Result],
        bt709: typing.Callable[[], T_Result],
        bt2020: typing.Callable[[], T_Result],
        bt2100: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FlowVideoEssenceParametersColorspace.BT601:
            return bt601()
        if self is FlowVideoEssenceParametersColorspace.BT709:
            return bt709()
        if self is FlowVideoEssenceParametersColorspace.BT2020:
            return bt2020()
        if self is FlowVideoEssenceParametersColorspace.BT2100:
            return bt2100()
