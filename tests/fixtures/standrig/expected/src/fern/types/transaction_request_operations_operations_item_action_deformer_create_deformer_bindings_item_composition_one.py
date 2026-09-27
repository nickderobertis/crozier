

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemCompositionOne(enum.StrEnum):
    LEGACY_ADDITIVE = "legacy-additive"

    def visit(self, legacy_additive: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemCompositionOne.LEGACY_ADDITIVE
        ):
            return legacy_additive()
