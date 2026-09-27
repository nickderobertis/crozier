

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionSymmetryContractContractLinksItemKindThree(enum.StrEnum):
    PHYSICS = "physics"

    def visit(self, physics: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionSymmetryContractContractLinksItemKindThree.PHYSICS:
            return physics()
