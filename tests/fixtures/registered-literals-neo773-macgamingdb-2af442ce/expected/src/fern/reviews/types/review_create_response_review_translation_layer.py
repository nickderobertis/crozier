

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ReviewCreateResponseReviewTranslationLayer(enum.StrEnum):
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
        if self is ReviewCreateResponseReviewTranslationLayer.DXVK:
            return dxvk()
        if self is ReviewCreateResponseReviewTranslationLayer.DXMT:
            return dxmt()
        if self is ReviewCreateResponseReviewTranslationLayer.D3D_METAL:
            return d3d_metal()
        if self is ReviewCreateResponseReviewTranslationLayer.NONE:
            return none()
