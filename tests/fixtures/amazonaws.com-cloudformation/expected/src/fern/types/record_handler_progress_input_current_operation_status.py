

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RecordHandlerProgressInputCurrentOperationStatus(enum.StrEnum):
    """
    Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.
    """

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
        if self is RecordHandlerProgressInputCurrentOperationStatus.PENDING:
            return pending()
        if self is RecordHandlerProgressInputCurrentOperationStatus.IN_PROGRESS:
            return in_progress()
        if self is RecordHandlerProgressInputCurrentOperationStatus.SUCCESS:
            return success()
        if self is RecordHandlerProgressInputCurrentOperationStatus.FAILED:
            return failed()
