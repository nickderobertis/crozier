

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReviewerVerdictVerdict(enum.StrEnum):
    APPROVED = "approved"
    REVISION_REQUIRED = "revision_required"
    REJECTED = "rejected"

    def visit(
        self,
        approved: typing.Callable[[], T_Result],
        revision_required: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ReviewerVerdictVerdict.APPROVED:
            return approved()
        if self is ReviewerVerdictVerdict.REVISION_REQUIRED:
            return revision_required()
        if self is ReviewerVerdictVerdict.REJECTED:
            return rejected()
