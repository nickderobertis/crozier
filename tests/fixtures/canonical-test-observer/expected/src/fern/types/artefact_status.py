

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ArtefactStatus(enum.StrEnum):
    APPROVED = "APPROVED"
    MARKED_AS_FAILED = "MARKED_AS_FAILED"
    UNDECIDED = "UNDECIDED"

    def visit(
        self,
        approved: typing.Callable[[], T_Result],
        marked_as_failed: typing.Callable[[], T_Result],
        undecided: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ArtefactStatus.APPROVED:
            return approved()
        if self is ArtefactStatus.MARKED_AS_FAILED:
            return marked_as_failed()
        if self is ArtefactStatus.UNDECIDED:
            return undecided()
