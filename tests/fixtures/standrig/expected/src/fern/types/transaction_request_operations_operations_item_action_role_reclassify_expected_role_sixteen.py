

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleSixteen(enum.StrEnum):
    CLOTHING = "clothing"

    def visit(self, clothing: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleSixteen.CLOTHING:
            return clothing()
