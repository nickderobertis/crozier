

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class FeedStateUpsertResponseStatus(enum.StrEnum):
    ONGOING = "Ongoing"
    RESOLVED = "Resolved"

    def visit(self, ongoing: typing.Callable[[], T_Result], resolved: typing.Callable[[], T_Result]) -> T_Result:
        if self is FeedStateUpsertResponseStatus.ONGOING:
            return ongoing()
        if self is FeedStateUpsertResponseStatus.RESOLVED:
            return resolved()
