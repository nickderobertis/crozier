

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataAngleUnit(enum.StrEnum):
    DEG = "deg"

    def visit(self, deg: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataAngleUnit.DEG:
            return deg()
