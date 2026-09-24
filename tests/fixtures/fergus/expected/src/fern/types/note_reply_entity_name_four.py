

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NoteReplyEntityNameFour(enum.StrEnum):
    SITE = "site"

    def visit(self, site: typing.Callable[[], T_Result]) -> T_Result:
        if self is NoteReplyEntityNameFour.SITE:
            return site()
