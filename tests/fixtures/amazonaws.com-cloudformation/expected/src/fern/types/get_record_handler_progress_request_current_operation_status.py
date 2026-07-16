

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetRecordHandlerProgressRequestCurrentOperationStatus(str, enum.Enum):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        success: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetRecordHandlerProgressRequestCurrentOperationStatus.PENDING:
            return pending()
        if self is GetRecordHandlerProgressRequestCurrentOperationStatus.IN_PROGRESS:
            return in_progress()
        if self is GetRecordHandlerProgressRequestCurrentOperationStatus.SUCCESS:
            return success()
        if self is GetRecordHandlerProgressRequestCurrentOperationStatus.FAILED:
            return failed()
