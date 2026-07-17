

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AnalysisArchiveTransitionHistoryTransition(enum.StrEnum):
    ARCHIVE = "archive"
    DELETE = "delete"

    def visit(self, archive: typing.Callable[[], T_Result], delete: typing.Callable[[], T_Result]) -> T_Result:
        if self is AnalysisArchiveTransitionHistoryTransition.ARCHIVE:
            return archive()
        if self is AnalysisArchiveTransitionHistoryTransition.DELETE:
            return delete()
