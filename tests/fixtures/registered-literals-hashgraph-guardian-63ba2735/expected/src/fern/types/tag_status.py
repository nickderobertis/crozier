

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TagStatus(enum.StrEnum):
    DRAFT = "Draft"
    PUBLISHED = "Published"
    HISTORY = "History"

    def visit(
        self,
        draft: typing.Callable[[], T_Result],
        published: typing.Callable[[], T_Result],
        history: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TagStatus.DRAFT:
            return draft()
        if self is TagStatus.PUBLISHED:
            return published()
        if self is TagStatus.HISTORY:
            return history()
