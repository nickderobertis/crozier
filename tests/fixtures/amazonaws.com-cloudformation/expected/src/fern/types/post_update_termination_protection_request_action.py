

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostUpdateTerminationProtectionRequestAction(enum.StrEnum):
    UPDATE_TERMINATION_PROTECTION = "UpdateTerminationProtection"

    def visit(self, update_termination_protection: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostUpdateTerminationProtectionRequestAction.UPDATE_TERMINATION_PROTECTION:
            return update_termination_protection()
