

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemCompositionOne(
    enum.StrEnum
):
    LEGACY_ADDITIVE = "legacy-additive"

    def visit(self, legacy_additive: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemCompositionOne.LEGACY_ADDITIVE
        ):
            return legacy_additive()
