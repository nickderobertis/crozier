

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataShapePreservationZero(
    enum.StrEnum
):
    RIGID = "rigid"

    def visit(self, rigid: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataShapePreservationZero.RIGID
        ):
            return rigid()
