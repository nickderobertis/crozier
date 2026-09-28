

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionSymmetryContractContractLinksItemKindZero(enum.StrEnum):
    PART = "part"

    def visit(self, part: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionSymmetryContractContractLinksItemKindZero.PART:
            return part()
