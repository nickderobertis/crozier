

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LlmConfigCompatibilityType(enum.StrEnum):
    GGUF = "gguf"
    MLX = "mlx"

    def visit(self, gguf: typing.Callable[[], T_Result], mlx: typing.Callable[[], T_Result]) -> T_Result:
        if self is LlmConfigCompatibilityType.GGUF:
            return gguf()
        if self is LlmConfigCompatibilityType.MLX:
            return mlx()
