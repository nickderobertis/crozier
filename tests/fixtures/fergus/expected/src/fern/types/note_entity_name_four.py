

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NoteEntityNameFour(enum.StrEnum):
    SITE = "site"

    def visit(self, site: typing.Callable[[], T_Result]) -> T_Result:
        if self is NoteEntityNameFour.SITE:
            return site()
