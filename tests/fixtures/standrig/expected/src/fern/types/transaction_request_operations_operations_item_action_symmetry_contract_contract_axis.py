

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionSymmetryContractContractAxis(enum.StrEnum):
    VERTICAL = "vertical"

    def visit(self, vertical: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionSymmetryContractContractAxis.VERTICAL:
            return vertical()
