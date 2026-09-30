

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FleetUiMessageChunkDataChildProgressDataCleanupState(enum.StrEnum):
    PENDING = "pending"
    COMPLETE = "complete"
    FAILED = "failed"
    NOT_REQUIRED = "not_required"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        complete: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        not_required: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FleetUiMessageChunkDataChildProgressDataCleanupState.PENDING:
            return pending()
        if self is FleetUiMessageChunkDataChildProgressDataCleanupState.COMPLETE:
            return complete()
        if self is FleetUiMessageChunkDataChildProgressDataCleanupState.FAILED:
            return failed()
        if self is FleetUiMessageChunkDataChildProgressDataCleanupState.NOT_REQUIRED:
            return not_required()
