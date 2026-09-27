

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PendingDeletionResponseCode(enum.StrEnum):
    ACCOUNT_PENDING_DELETION = "account_pending_deletion"
    BUSINESS_PENDING_DELETION = "business_pending_deletion"

    def visit(
        self,
        account_pending_deletion: typing.Callable[[], T_Result],
        business_pending_deletion: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PendingDeletionResponseCode.ACCOUNT_PENDING_DELETION:
            return account_pending_deletion()
        if self is PendingDeletionResponseCode.BUSINESS_PENDING_DELETION:
            return business_pending_deletion()
