

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostCibaCompleteRequestResult(enum.StrEnum):
    AUTHORIZED = "AUTHORIZED"
    ACCESS_DENIED = "ACCESS_DENIED"
    TRANSACTION_FAILED = "TRANSACTION_FAILED"

    def visit(
        self,
        authorized: typing.Callable[[], T_Result],
        access_denied: typing.Callable[[], T_Result],
        transaction_failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostCibaCompleteRequestResult.AUTHORIZED:
            return authorized()
        if self is PostCibaCompleteRequestResult.ACCESS_DENIED:
            return access_denied()
        if self is PostCibaCompleteRequestResult.TRANSACTION_FAILED:
            return transaction_failed()
