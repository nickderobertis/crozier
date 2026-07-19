

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FlowVideoEssenceParametersInterlaceMode(enum.StrEnum):
    """
    Interlaced video mode for frames in this Flow
    """

    PROGRESSIVE = "progressive"
    INTERLACED_TFF = "interlaced_tff"
    INTERLACED_BFF = "interlaced_bff"
    INTERLACED_PSF = "interlaced_psf"

    def visit(
        self,
        progressive: typing.Callable[[], T_Result],
        interlaced_tff: typing.Callable[[], T_Result],
        interlaced_bff: typing.Callable[[], T_Result],
        interlaced_psf: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FlowVideoEssenceParametersInterlaceMode.PROGRESSIVE:
            return progressive()
        if self is FlowVideoEssenceParametersInterlaceMode.INTERLACED_TFF:
            return interlaced_tff()
        if self is FlowVideoEssenceParametersInterlaceMode.INTERLACED_BFF:
            return interlaced_bff()
        if self is FlowVideoEssenceParametersInterlaceMode.INTERLACED_PSF:
            return interlaced_psf()
