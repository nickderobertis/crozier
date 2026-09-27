

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataParentCompositionZero(
    enum.StrEnum
):
    PARENT_FIRST = "parent-first"

    def visit(self, parent_first: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataParentCompositionZero.PARENT_FIRST
        ):
            return parent_first()
