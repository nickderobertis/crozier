

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetAuthorizationGenerateLinkCodeResponseErrorsItemErrorCode(enum.StrEnum):
    INVALID_TRANSACTION_ID = "invalid_transaction_id"
    LINK_CODE_GEN_FAILED = "link_code_gen_failed"
    INVALID_TRANSACTION = "invalid_transaction"

    def visit(
        self,
        invalid_transaction_id: typing.Callable[[], T_Result],
        link_code_gen_failed: typing.Callable[[], T_Result],
        invalid_transaction: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetAuthorizationGenerateLinkCodeResponseErrorsItemErrorCode.INVALID_TRANSACTION_ID:
            return invalid_transaction_id()
        if self is GetAuthorizationGenerateLinkCodeResponseErrorsItemErrorCode.LINK_CODE_GEN_FAILED:
            return link_code_gen_failed()
        if self is GetAuthorizationGenerateLinkCodeResponseErrorsItemErrorCode.INVALID_TRANSACTION:
            return invalid_transaction()
