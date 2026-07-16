

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetRecordHandlerProgressRequestAction(enum.StrEnum):
    RECORD_HANDLER_PROGRESS = "RecordHandlerProgress"

    def visit(self, record_handler_progress: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetRecordHandlerProgressRequestAction.RECORD_HANDLER_PROGRESS:
            return record_handler_progress()
