

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TollfreeVerificationEnumStatus(enum.StrEnum):
    PENDING_REVIEW = "PENDING_REVIEW"
    IN_REVIEW = "IN_REVIEW"
    TWILIO_APPROVED = "TWILIO_APPROVED"
    TWILIO_REJECTED = "TWILIO_REJECTED"

    def visit(
        self,
        pending_review: typing.Callable[[], T_Result],
        in_review: typing.Callable[[], T_Result],
        twilio_approved: typing.Callable[[], T_Result],
        twilio_rejected: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TollfreeVerificationEnumStatus.PENDING_REVIEW:
            return pending_review()
        if self is TollfreeVerificationEnumStatus.IN_REVIEW:
            return in_review()
        if self is TollfreeVerificationEnumStatus.TWILIO_APPROVED:
            return twilio_approved()
        if self is TollfreeVerificationEnumStatus.TWILIO_REJECTED:
            return twilio_rejected()
