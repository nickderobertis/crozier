

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class FeedStateAllResponseItemStatus(enum.StrEnum):
    ONGOING = "Ongoing"
    RESOLVED = "Resolved"

    def visit(self, ongoing: typing.Callable[[], T_Result], resolved: typing.Callable[[], T_Result]) -> T_Result:
        if self is FeedStateAllResponseItemStatus.ONGOING:
            return ongoing()
        if self is FeedStateAllResponseItemStatus.RESOLVED:
            return resolved()
