

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VideoRenderingRequestAspectRatio(enum.StrEnum):
    SIXTEEN9 = "16:9"
    NINE16 = "9:16"
    ONE1 = "1:1"

    def visit(
        self,
        sixteen9: typing.Callable[[], T_Result],
        nine16: typing.Callable[[], T_Result],
        one1: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VideoRenderingRequestAspectRatio.SIXTEEN9:
            return sixteen9()
        if self is VideoRenderingRequestAspectRatio.NINE16:
            return nine16()
        if self is VideoRenderingRequestAspectRatio.ONE1:
            return one1()
