

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataPivotSpaceOne(enum.StrEnum):
    NORMALIZED = "normalized"

    def visit(self, normalized: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataPivotSpaceOne.NORMALIZED
        ):
            return normalized()
