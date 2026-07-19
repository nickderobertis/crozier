

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelCompatibilityType(enum.StrEnum):
    GGUF = "gguf"
    MLX = "mlx"

    def visit(self, gguf: typing.Callable[[], T_Result], mlx: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelCompatibilityType.GGUF:
            return gguf()
        if self is ModelCompatibilityType.MLX:
            return mlx()
