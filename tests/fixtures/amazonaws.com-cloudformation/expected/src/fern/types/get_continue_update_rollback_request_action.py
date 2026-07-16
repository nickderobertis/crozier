

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetContinueUpdateRollbackRequestAction(str, enum.Enum):
    CONTINUE_UPDATE_ROLLBACK = "ContinueUpdateRollback"

    def visit(self, continue_update_rollback: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetContinueUpdateRollbackRequestAction.CONTINUE_UPDATE_ROLLBACK:
            return continue_update_rollback()
