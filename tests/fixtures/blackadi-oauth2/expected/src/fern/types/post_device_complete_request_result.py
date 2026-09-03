

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostDeviceCompleteRequestResult(enum.StrEnum):
    SUCCESS = "SUCCESS"
    ACCESS_DENIED = "ACCESS_DENIED"
    TRANSACTION_FAILED = "TRANSACTION_FAILED"

    def visit(
        self,
        success: typing.Callable[[], T_Result],
        access_denied: typing.Callable[[], T_Result],
        transaction_failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostDeviceCompleteRequestResult.SUCCESS:
            return success()
        if self is PostDeviceCompleteRequestResult.ACCESS_DENIED:
            return access_denied()
        if self is PostDeviceCompleteRequestResult.TRANSACTION_FAILED:
            return transaction_failed()
