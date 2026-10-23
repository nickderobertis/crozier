

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurveyStylingBackgroundBgType(enum.StrEnum):
    ANIMATION = "animation"
    COLOR = "color"
    IMAGE = "image"
    UPLOAD = "upload"

    def visit(
        self,
        animation: typing.Callable[[], T_Result],
        color: typing.Callable[[], T_Result],
        image: typing.Callable[[], T_Result],
        upload: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SurveyStylingBackgroundBgType.ANIMATION:
            return animation()
        if self is SurveyStylingBackgroundBgType.COLOR:
            return color()
        if self is SurveyStylingBackgroundBgType.IMAGE:
            return image()
        if self is SurveyStylingBackgroundBgType.UPLOAD:
            return upload()
