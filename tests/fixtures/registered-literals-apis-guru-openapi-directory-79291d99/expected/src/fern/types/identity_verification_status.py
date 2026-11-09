

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IdentityVerificationStatus(enum.StrEnum):
    """
    The status of this Identity Verification attempt.


    `active` - The Identity Verification attempt is incomplete. The user may have completed part of the session, but has neither failed or passed.

    `success` - The Identity Verification attempt has completed, passing all steps defined to the associated Identity Verification template

    `failed` - The user failed one or more steps in the session and was told to contact support.

    `expired` - The Identity Verification attempt was active for a long period of time without being completed and was automatically marked as expired. Note that sessions currently do not expire. Automatic expiration is expected to be enabled in the future.

    `canceled` - The Identity Verification attempt was canceled, either via the dashboard by a user, or via API. The user may have completed part of the session, but has neither failed or passed.

    `pending_review` - The Identity Verification attempt template was configured to perform a screening that had one or more hits needing review.
    """

    ACTIVE = "active"
    SUCCESS = "success"
    FAILED = "failed"
    EXPIRED = "expired"
    CANCELED = "canceled"
    PENDING_REVIEW = "pending_review"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        success: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
        pending_review: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IdentityVerificationStatus.ACTIVE:
            return active()
        if self is IdentityVerificationStatus.SUCCESS:
            return success()
        if self is IdentityVerificationStatus.FAILED:
            return failed()
        if self is IdentityVerificationStatus.EXPIRED:
            return expired()
        if self is IdentityVerificationStatus.CANCELED:
            return canceled()
        if self is IdentityVerificationStatus.PENDING_REVIEW:
            return pending_review()
