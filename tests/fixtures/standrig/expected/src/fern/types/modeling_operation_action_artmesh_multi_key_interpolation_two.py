

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionArtmeshMultiKeyInterpolationTwo(enum.StrEnum):
    SMOOTHSTEP = "smoothstep"

    def visit(self, smoothstep: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionArtmeshMultiKeyInterpolationTwo.SMOOTHSTEP:
            return smoothstep()
