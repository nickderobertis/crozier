

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionTransformOperatorOne(enum.StrEnum):
    SET = "set"

    def visit(self, set_: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionTransformOperatorOne.SET:
            return set_()
