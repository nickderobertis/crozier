

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostCompleteSignupRedirectResponseErrorsItemErrorCode(enum.StrEnum):
    INVALID_TRANSACTION = "invalid_transaction"
    INVALID_TRANSACTION_ID = "invalid_transaction_id"
    VERIFICATION_INCOMPLETE = "verification_incomplete"

    def visit(
        self,
        invalid_transaction: typing.Callable[[], T_Result],
        invalid_transaction_id: typing.Callable[[], T_Result],
        verification_incomplete: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostCompleteSignupRedirectResponseErrorsItemErrorCode.INVALID_TRANSACTION:
            return invalid_transaction()
        if self is PostCompleteSignupRedirectResponseErrorsItemErrorCode.INVALID_TRANSACTION_ID:
            return invalid_transaction_id()
        if self is PostCompleteSignupRedirectResponseErrorsItemErrorCode.VERIFICATION_INCOMPLETE:
            return verification_incomplete()
