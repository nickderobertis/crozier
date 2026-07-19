

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FlowVideoEssenceParametersUncParametersUncType(enum.StrEnum):
    """
    Uncompressed picture packing type. If codec is `video/raw`, unc_type must be set.
    """

    PLANAR = "planar"
    YUYV = "YUYV"
    UYVY = "UYVY"
    AYUV = "AYUV"
    V210 = "v210"
    V216 = "v216"
    RGB = "RGB"
    RG_BX = "RGBx"
    X_RGB = "xRGB"
    BG_RX = "BGRx"
    X_BGR = "xBGR"
    RGBA = "RGBA"
    ARGB = "ARGB"
    BGRA = "BGRA"
    ABGR = "ABGR"
    ALPHA = "alpha"

    def visit(
        self,
        planar: typing.Callable[[], T_Result],
        yuyv: typing.Callable[[], T_Result],
        uyvy: typing.Callable[[], T_Result],
        ayuv: typing.Callable[[], T_Result],
        v210: typing.Callable[[], T_Result],
        v216: typing.Callable[[], T_Result],
        rgb: typing.Callable[[], T_Result],
        rg_bx: typing.Callable[[], T_Result],
        x_rgb: typing.Callable[[], T_Result],
        bg_rx: typing.Callable[[], T_Result],
        x_bgr: typing.Callable[[], T_Result],
        rgba: typing.Callable[[], T_Result],
        argb: typing.Callable[[], T_Result],
        bgra: typing.Callable[[], T_Result],
        abgr: typing.Callable[[], T_Result],
        alpha: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FlowVideoEssenceParametersUncParametersUncType.PLANAR:
            return planar()
        if self is FlowVideoEssenceParametersUncParametersUncType.YUYV:
            return yuyv()
        if self is FlowVideoEssenceParametersUncParametersUncType.UYVY:
            return uyvy()
        if self is FlowVideoEssenceParametersUncParametersUncType.AYUV:
            return ayuv()
        if self is FlowVideoEssenceParametersUncParametersUncType.V210:
            return v210()
        if self is FlowVideoEssenceParametersUncParametersUncType.V216:
            return v216()
        if self is FlowVideoEssenceParametersUncParametersUncType.RGB:
            return rgb()
        if self is FlowVideoEssenceParametersUncParametersUncType.RG_BX:
            return rg_bx()
        if self is FlowVideoEssenceParametersUncParametersUncType.X_RGB:
            return x_rgb()
        if self is FlowVideoEssenceParametersUncParametersUncType.BG_RX:
            return bg_rx()
        if self is FlowVideoEssenceParametersUncParametersUncType.X_BGR:
            return x_bgr()
        if self is FlowVideoEssenceParametersUncParametersUncType.RGBA:
            return rgba()
        if self is FlowVideoEssenceParametersUncParametersUncType.ARGB:
            return argb()
        if self is FlowVideoEssenceParametersUncParametersUncType.BGRA:
            return bgra()
        if self is FlowVideoEssenceParametersUncParametersUncType.ABGR:
            return abgr()
        if self is FlowVideoEssenceParametersUncParametersUncType.ALPHA:
            return alpha()
