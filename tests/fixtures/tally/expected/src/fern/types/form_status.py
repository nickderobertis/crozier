

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FormStatus(enum.StrEnum):
    BLANK = "BLANK"
    DRAFT = "DRAFT"
    PUBLISHED = "PUBLISHED"
    DELETED = "DELETED"

    def visit(
        self,
        blank: typing.Callable[[], T_Result],
        draft: typing.Callable[[], T_Result],
        published: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FormStatus.BLANK:
            return blank()
        if self is FormStatus.DRAFT:
            return draft()
        if self is FormStatus.PUBLISHED:
            return published()
        if self is FormStatus.DELETED:
            return deleted()
