

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AnalysisArchiveAddResultStatus(enum.StrEnum):
    """
    The status of the archive add operation. Typically either 'archived' or 'error'
    """

    ARCHIVED = "archived"
    ARCHIVING = "archiving"
    ERROR = "error"

    def visit(
        self,
        archived: typing.Callable[[], T_Result],
        archiving: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AnalysisArchiveAddResultStatus.ARCHIVED:
            return archived()
        if self is AnalysisArchiveAddResultStatus.ARCHIVING:
            return archiving()
        if self is AnalysisArchiveAddResultStatus.ERROR:
            return error()
