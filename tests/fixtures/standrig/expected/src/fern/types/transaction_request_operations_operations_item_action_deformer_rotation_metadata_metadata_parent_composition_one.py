

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataParentCompositionOne(
    enum.StrEnum
):
    CHILD_FIRST = "child-first"

    def visit(self, child_first: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataParentCompositionOne.CHILD_FIRST
        ):
            return child_first()
