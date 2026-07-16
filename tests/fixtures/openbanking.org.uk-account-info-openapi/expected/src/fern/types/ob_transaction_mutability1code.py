

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObTransactionMutability1Code(enum.StrEnum):
    """
    Specifies the Mutability of the Transaction record.
    """

    MUTABLE = "Mutable"
    IMMUTABLE = "Immutable"

    def visit(self, mutable: typing.Callable[[], T_Result], immutable: typing.Callable[[], T_Result]) -> T_Result:
        if self is ObTransactionMutability1Code.MUTABLE:
            return mutable()
        if self is ObTransactionMutability1Code.IMMUTABLE:
            return immutable()
