

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ReviewCreateRequestTranslationLayer(enum.StrEnum):
    DXVK = "DXVK"
    DXMT = "DXMT"
    D3D_METAL = "D3D_METAL"
    NONE = "NONE"

    def visit(
        self,
        dxvk: typing.Callable[[], T_Result],
        dxmt: typing.Callable[[], T_Result],
        d3d_metal: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ReviewCreateRequestTranslationLayer.DXVK:
            return dxvk()
        if self is ReviewCreateRequestTranslationLayer.DXMT:
            return dxmt()
        if self is ReviewCreateRequestTranslationLayer.D3D_METAL:
            return d3d_metal()
        if self is ReviewCreateRequestTranslationLayer.NONE:
            return none()
