

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateTopicStatusRequestStatus(enum.StrEnum):
    CLOSED = "closed"
    PINNED = "pinned"
    PINNED_GLOBALLY = "pinned_globally"
    ARCHIVED = "archived"
    VISIBLE = "visible"

    def visit(
        self,
        closed: typing.Callable[[], T_Result],
        pinned: typing.Callable[[], T_Result],
        pinned_globally: typing.Callable[[], T_Result],
        archived: typing.Callable[[], T_Result],
        visible: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UpdateTopicStatusRequestStatus.CLOSED:
            return closed()
        if self is UpdateTopicStatusRequestStatus.PINNED:
            return pinned()
        if self is UpdateTopicStatusRequestStatus.PINNED_GLOBALLY:
            return pinned_globally()
        if self is UpdateTopicStatusRequestStatus.ARCHIVED:
            return archived()
        if self is UpdateTopicStatusRequestStatus.VISIBLE:
            return visible()
