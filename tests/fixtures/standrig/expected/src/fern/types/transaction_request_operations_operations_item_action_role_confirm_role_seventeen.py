

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionRoleConfirmRoleSeventeen(enum.StrEnum):
    ACCESSORY = "accessory"

    def visit(self, accessory: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionRoleConfirmRoleSeventeen.ACCESSORY:
            return accessory()
