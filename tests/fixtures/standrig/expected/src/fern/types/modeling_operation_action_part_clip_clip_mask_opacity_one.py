

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionPartClipClipMaskOpacityOne(enum.StrEnum):
    IGNORE = "ignore"

    def visit(self, ignore: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionPartClipClipMaskOpacityOne.IGNORE:
            return ignore()
