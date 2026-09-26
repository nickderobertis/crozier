

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostModelsLlmVersion(enum.StrEnum):
    SONNET40 = "sonnet-4.0"
    SONNET45 = "sonnet-4.5"
    QWEN3VL = "qwen3-vl"

    def visit(
        self,
        sonnet40: typing.Callable[[], T_Result],
        sonnet45: typing.Callable[[], T_Result],
        qwen3vl: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostModelsLlmVersion.SONNET40:
            return sonnet40()
        if self is PostModelsLlmVersion.SONNET45:
            return sonnet45()
        if self is PostModelsLlmVersion.QWEN3VL:
            return qwen3vl()
