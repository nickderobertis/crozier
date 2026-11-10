

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LinkDeliveryVerificationStatus(enum.StrEnum):
    """
    Indicates an Item's micro-deposit-based verification status.
    """

    AUTOMATICALLY_VERIFIED = "automatically_verified"
    PENDING_AUTOMATIC_VERIFICATION = "pending_automatic_verification"
    PENDING_MANUAL_VERIFICATION = "pending_manual_verification"
    MANUALLY_VERIFIED = "manually_verified"
    VERIFICATION_EXPIRED = "verification_expired"
    VERIFICATION_FAILED = "verification_failed"

    def visit(
        self,
        automatically_verified: typing.Callable[[], T_Result],
        pending_automatic_verification: typing.Callable[[], T_Result],
        pending_manual_verification: typing.Callable[[], T_Result],
        manually_verified: typing.Callable[[], T_Result],
        verification_expired: typing.Callable[[], T_Result],
        verification_failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LinkDeliveryVerificationStatus.AUTOMATICALLY_VERIFIED:
            return automatically_verified()
        if self is LinkDeliveryVerificationStatus.PENDING_AUTOMATIC_VERIFICATION:
            return pending_automatic_verification()
        if self is LinkDeliveryVerificationStatus.PENDING_MANUAL_VERIFICATION:
            return pending_manual_verification()
        if self is LinkDeliveryVerificationStatus.MANUALLY_VERIFIED:
            return manually_verified()
        if self is LinkDeliveryVerificationStatus.VERIFICATION_EXPIRED:
            return verification_expired()
        if self is LinkDeliveryVerificationStatus.VERIFICATION_FAILED:
            return verification_failed()
