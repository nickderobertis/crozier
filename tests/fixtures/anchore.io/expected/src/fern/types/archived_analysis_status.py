

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ArchivedAnalysisStatus(enum.StrEnum):
    """
    The archival status
    """

    ARCHIVING = "archiving"
    ARCHIVED = "archived"
    DELETING = "deleting"
    DELETED = "deleted"

    def visit(
        self,
        archiving: typing.Callable[[], T_Result],
        archived: typing.Callable[[], T_Result],
        deleting: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ArchivedAnalysisStatus.ARCHIVING:
            return archiving()
        if self is ArchivedAnalysisStatus.ARCHIVED:
            return archived()
        if self is ArchivedAnalysisStatus.DELETING:
            return deleting()
        if self is ArchivedAnalysisStatus.DELETED:
            return deleted()
