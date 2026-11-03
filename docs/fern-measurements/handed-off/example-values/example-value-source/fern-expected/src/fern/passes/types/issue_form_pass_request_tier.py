

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class IssueFormPassRequestTier(enum.StrEnum):
    STANDARD = "standard"
    PRIORITY = "priority"

    def visit(self, standard: typing.Callable[[], T_Result], priority: typing.Callable[[], T_Result]) -> T_Result:
        if self is IssueFormPassRequestTier.STANDARD:
            return standard()
        if self is IssueFormPassRequestTier.PRIORITY:
            return priority()
