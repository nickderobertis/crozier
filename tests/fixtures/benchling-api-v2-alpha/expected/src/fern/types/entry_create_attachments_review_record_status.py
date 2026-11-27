

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EntryCreateAttachmentsReviewRecordStatus(enum.StrEnum):
    """
    Review Status for entry
    """

    ACCEPTED = "ACCEPTED"

    def visit(self, accepted: typing.Callable[[], T_Result]) -> T_Result:
        if self is EntryCreateAttachmentsReviewRecordStatus.ACCEPTED:
            return accepted()
