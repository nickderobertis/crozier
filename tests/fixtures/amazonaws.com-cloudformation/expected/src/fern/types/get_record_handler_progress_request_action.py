

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetRecordHandlerProgressRequestAction(str, enum.Enum):
    RECORD_HANDLER_PROGRESS = "RecordHandlerProgress"

    def visit(self, record_handler_progress: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetRecordHandlerProgressRequestAction.RECORD_HANDLER_PROGRESS:
            return record_handler_progress()
