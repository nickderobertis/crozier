

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostLinkedConsentV2ResponseErrorsItemErrorCode(enum.StrEnum):
    INVALID_TRANSACTION_ID = "invalid_transaction_id"
    INVALID_TRANSACTION = "invalid_transaction"
    INVALID_ACCEPTED_CLAIM = "invalid_accepted_claim"
    INVALID_PERMITTED_SCOPE = "invalid_permitted_scope"

    def visit(
        self,
        invalid_transaction_id: typing.Callable[[], T_Result],
        invalid_transaction: typing.Callable[[], T_Result],
        invalid_accepted_claim: typing.Callable[[], T_Result],
        invalid_permitted_scope: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostLinkedConsentV2ResponseErrorsItemErrorCode.INVALID_TRANSACTION_ID:
            return invalid_transaction_id()
        if self is PostLinkedConsentV2ResponseErrorsItemErrorCode.INVALID_TRANSACTION:
            return invalid_transaction()
        if self is PostLinkedConsentV2ResponseErrorsItemErrorCode.INVALID_ACCEPTED_CLAIM:
            return invalid_accepted_claim()
        if self is PostLinkedConsentV2ResponseErrorsItemErrorCode.INVALID_PERMITTED_SCOPE:
            return invalid_permitted_scope()
