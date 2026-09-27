

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionRoleReclassifyRoleFifteen(enum.StrEnum):
    SOFT_TISSUE = "soft-tissue"

    def visit(self, soft_tissue: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionRoleReclassifyRoleFifteen.SOFT_TISSUE:
            return soft_tissue()
