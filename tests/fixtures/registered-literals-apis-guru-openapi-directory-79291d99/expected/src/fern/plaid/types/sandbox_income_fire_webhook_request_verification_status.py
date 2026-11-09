

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SandboxIncomeFireWebhookRequestVerificationStatus(enum.StrEnum):
    """
    `VERIFICATION_STATUS_PROCESSING_COMPLETE`: The income verification status processing has completed. If the user uploaded multiple documents, this webhook will fire when all documents have finished processing. Call the `/income/verification/paystubs/get` endpoint and check the document metadata to see which documents were successfully parsed.

    `VERIFICATION_STATUS_PROCESSING_FAILED`: A failure occurred when attempting to process the verification documentation.

    `VERIFICATION_STATUS_PENDING_APPROVAL`: (deprecated) The income verification has been sent to the user for review.
    """

    VERIFICATION_STATUS_PROCESSING_COMPLETE = "VERIFICATION_STATUS_PROCESSING_COMPLETE"
    VERIFICATION_STATUS_PROCESSING_FAILED = "VERIFICATION_STATUS_PROCESSING_FAILED"
    VERIFICATION_STATUS_PENDING_APPROVAL = "VERIFICATION_STATUS_PENDING_APPROVAL"

    def visit(
        self,
        verification_status_processing_complete: typing.Callable[[], T_Result],
        verification_status_processing_failed: typing.Callable[[], T_Result],
        verification_status_pending_approval: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SandboxIncomeFireWebhookRequestVerificationStatus.VERIFICATION_STATUS_PROCESSING_COMPLETE:
            return verification_status_processing_complete()
        if self is SandboxIncomeFireWebhookRequestVerificationStatus.VERIFICATION_STATUS_PROCESSING_FAILED:
            return verification_status_processing_failed()
        if self is SandboxIncomeFireWebhookRequestVerificationStatus.VERIFICATION_STATUS_PENDING_APPROVAL:
            return verification_status_pending_approval()
