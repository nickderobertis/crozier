

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BillingVerificationErrorCode(enum.StrEnum):
    """
    Machine-readable billing-verification state, mirrored in the X-Billing-Verification response header.
    """

    RENEWAL_VERIFICATION_PENDING = "renewal_verification_pending"
    RENEWAL_VERIFICATION_FAILED = "renewal_verification_failed"
    ENTITLEMENT_VERIFICATION_UNAVAILABLE = "entitlement_verification_unavailable"

    def visit(
        self,
        renewal_verification_pending: typing.Callable[[], T_Result],
        renewal_verification_failed: typing.Callable[[], T_Result],
        entitlement_verification_unavailable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BillingVerificationErrorCode.RENEWAL_VERIFICATION_PENDING:
            return renewal_verification_pending()
        if self is BillingVerificationErrorCode.RENEWAL_VERIFICATION_FAILED:
            return renewal_verification_failed()
        if self is BillingVerificationErrorCode.ENTITLEMENT_VERIFICATION_UNAVAILABLE:
            return entitlement_verification_unavailable()
