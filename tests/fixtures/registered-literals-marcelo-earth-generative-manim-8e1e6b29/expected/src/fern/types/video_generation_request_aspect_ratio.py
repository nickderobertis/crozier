

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VideoGenerationRequestAspectRatio(enum.StrEnum):
    SIXTEEN9 = "16:9"
    NINE16 = "9:16"
    ONE1 = "1:1"

    def visit(
        self,
        sixteen9: typing.Callable[[], T_Result],
        nine16: typing.Callable[[], T_Result],
        one1: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VideoGenerationRequestAspectRatio.SIXTEEN9:
            return sixteen9()
        if self is VideoGenerationRequestAspectRatio.NINE16:
            return nine16()
        if self is VideoGenerationRequestAspectRatio.ONE1:
            return one1()
