

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostContinueUpdateRollbackRequestAction(enum.StrEnum):
    CONTINUE_UPDATE_ROLLBACK = "ContinueUpdateRollback"

    def visit(self, continue_update_rollback: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostContinueUpdateRollbackRequestAction.CONTINUE_UPDATE_ROLLBACK:
            return continue_update_rollback()
