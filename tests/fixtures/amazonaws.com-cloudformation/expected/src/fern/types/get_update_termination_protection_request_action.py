

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetUpdateTerminationProtectionRequestAction(str, enum.Enum):
    UPDATE_TERMINATION_PROTECTION = "UpdateTerminationProtection"

    def visit(self, update_termination_protection: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetUpdateTerminationProtectionRequestAction.UPDATE_TERMINATION_PROTECTION:
            return update_termination_protection()
