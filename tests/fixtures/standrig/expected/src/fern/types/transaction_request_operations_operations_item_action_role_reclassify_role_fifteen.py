

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleFifteen(enum.StrEnum):
    SOFT_TISSUE = "soft-tissue"

    def visit(self, soft_tissue: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleFifteen.SOFT_TISSUE:
            return soft_tissue()
