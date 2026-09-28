

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionRoleConfirmRoleThirteen(enum.StrEnum):
    NECK = "neck"

    def visit(self, neck: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionRoleConfirmRoleThirteen.NECK:
            return neck()
