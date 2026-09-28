

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionPartBlendModeModeThree(enum.StrEnum):
    ADDITIVE = "additive"

    def visit(self, additive: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionPartBlendModeModeThree.ADDITIVE:
            return additive()
