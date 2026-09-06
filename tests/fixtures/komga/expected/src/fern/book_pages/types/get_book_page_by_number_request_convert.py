

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetBookPageByNumberRequestConvert(enum.StrEnum):
    JPEG = "jpeg"
    PNG = "png"

    def visit(self, jpeg: typing.Callable[[], T_Result], png: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetBookPageByNumberRequestConvert.JPEG:
            return jpeg()
        if self is GetBookPageByNumberRequestConvert.PNG:
            return png()
