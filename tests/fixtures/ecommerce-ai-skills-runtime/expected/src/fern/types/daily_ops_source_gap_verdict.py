

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DailyOpsSourceGapVerdict(enum.StrEnum):
    APPROVED = "approved"
    REVISION_REQUIRED = "revision_required"
    REJECTED = "rejected"

    def visit(
        self,
        approved: typing.Callable[[], T_Result],
        revision_required: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DailyOpsSourceGapVerdict.APPROVED:
            return approved()
        if self is DailyOpsSourceGapVerdict.REVISION_REQUIRED:
            return revision_required()
        if self is DailyOpsSourceGapVerdict.REJECTED:
            return rejected()
