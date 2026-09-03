

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IdentificationResponseStatus(enum.StrEnum):
    SUCCESS = "success"
    FAILED = "failed"
    PENDING = "pending"

    def visit(
        self,
        success: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IdentificationResponseStatus.SUCCESS:
            return success()
        if self is IdentificationResponseStatus.FAILED:
            return failed()
        if self is IdentificationResponseStatus.PENDING:
            return pending()
