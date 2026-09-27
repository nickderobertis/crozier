

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionPartClipClipMaskOpacityZero(enum.StrEnum):
    RENDERED = "rendered"

    def visit(self, rendered: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionPartClipClipMaskOpacityZero.RENDERED:
            return rendered()
