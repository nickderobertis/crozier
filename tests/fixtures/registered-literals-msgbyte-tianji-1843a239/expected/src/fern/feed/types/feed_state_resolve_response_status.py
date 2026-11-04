

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class FeedStateResolveResponseStatus(enum.StrEnum):
    ONGOING = "Ongoing"
    RESOLVED = "Resolved"

    def visit(self, ongoing: typing.Callable[[], T_Result], resolved: typing.Callable[[], T_Result]) -> T_Result:
        if self is FeedStateResolveResponseStatus.ONGOING:
            return ongoing()
        if self is FeedStateResolveResponseStatus.RESOLVED:
            return resolved()
