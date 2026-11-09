

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocumentStatus(enum.StrEnum):
    """
    An outcome status for this specific document submission. Distinct from the overall `documentary_verification.status` that summarizes the verification outcome from one or more documents.
    """

    SUCCESS = "success"
    FAILED = "failed"
    MANUALLY_APPROVED = "manually_approved"

    def visit(
        self,
        success: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        manually_approved: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocumentStatus.SUCCESS:
            return success()
        if self is DocumentStatus.FAILED:
            return failed()
        if self is DocumentStatus.MANUALLY_APPROVED:
            return manually_approved()
