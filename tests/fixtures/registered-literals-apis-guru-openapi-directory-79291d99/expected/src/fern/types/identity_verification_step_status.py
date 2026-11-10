

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IdentityVerificationStepStatus(enum.StrEnum):
    """
    The status of a step in the identity verification process.
    """

    SUCCESS = "success"
    ACTIVE = "active"
    FAILED = "failed"
    WAITING_FOR_PREREQUISITE = "waiting_for_prerequisite"
    NOT_APPLICABLE = "not_applicable"
    SKIPPED = "skipped"
    EXPIRED = "expired"
    CANCELED = "canceled"
    PENDING_REVIEW = "pending_review"
    MANUALLY_APPROVED = "manually_approved"
    MANUALLY_REJECTED = "manually_rejected"

    def visit(
        self,
        success: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        waiting_for_prerequisite: typing.Callable[[], T_Result],
        not_applicable: typing.Callable[[], T_Result],
        skipped: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
        pending_review: typing.Callable[[], T_Result],
        manually_approved: typing.Callable[[], T_Result],
        manually_rejected: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IdentityVerificationStepStatus.SUCCESS:
            return success()
        if self is IdentityVerificationStepStatus.ACTIVE:
            return active()
        if self is IdentityVerificationStepStatus.FAILED:
            return failed()
        if self is IdentityVerificationStepStatus.WAITING_FOR_PREREQUISITE:
            return waiting_for_prerequisite()
        if self is IdentityVerificationStepStatus.NOT_APPLICABLE:
            return not_applicable()
        if self is IdentityVerificationStepStatus.SKIPPED:
            return skipped()
        if self is IdentityVerificationStepStatus.EXPIRED:
            return expired()
        if self is IdentityVerificationStepStatus.CANCELED:
            return canceled()
        if self is IdentityVerificationStepStatus.PENDING_REVIEW:
            return pending_review()
        if self is IdentityVerificationStepStatus.MANUALLY_APPROVED:
            return manually_approved()
        if self is IdentityVerificationStepStatus.MANUALLY_REJECTED:
            return manually_rejected()
