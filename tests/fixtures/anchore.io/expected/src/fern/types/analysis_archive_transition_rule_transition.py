

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AnalysisArchiveTransitionRuleTransition(enum.StrEnum):
    """
    The type of transition to make. If "archive", then archive an image from the working set and remove it from the working set. If "delete", then match against archived images and delete from the archive if match.
    """

    ARCHIVE = "archive"
    DELETE = "delete"

    def visit(self, archive: typing.Callable[[], T_Result], delete: typing.Callable[[], T_Result]) -> T_Result:
        if self is AnalysisArchiveTransitionRuleTransition.ARCHIVE:
            return archive()
        if self is AnalysisArchiveTransitionRuleTransition.DELETE:
            return delete()
