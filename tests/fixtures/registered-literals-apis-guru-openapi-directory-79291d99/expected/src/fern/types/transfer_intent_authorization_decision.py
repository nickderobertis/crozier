

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransferIntentAuthorizationDecision(enum.StrEnum):
    """

    A decision regarding the proposed transfer.

    `APPROVED` – The proposed transfer has received the end user's consent and has been approved for processing by Plaid. The `decision_rationale` field is set if Plaid was unable to fetch the account information. You may proceed with the transfer, but further review is recommended (i.e., use Link in update to re-authenticate your user when `decision_rationale.code` is `ITEM_LOGIN_REQUIRED`). Refer to the `code` field in the `decision_rationale` object for details.

    `DECLINED` – Plaid reviewed the proposed transfer and declined processing. Refer to the `code` field in the `decision_rationale` object for details.
    """

    APPROVED = "APPROVED"
    DECLINED = "DECLINED"

    def visit(self, approved: typing.Callable[[], T_Result], declined: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransferIntentAuthorizationDecision.APPROVED:
            return approved()
        if self is TransferIntentAuthorizationDecision.DECLINED:
            return declined()
