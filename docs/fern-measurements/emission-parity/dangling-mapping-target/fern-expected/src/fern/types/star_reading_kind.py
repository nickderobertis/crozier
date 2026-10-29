

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StarReadingKind(enum.StrEnum):
    STAR = "STAR"

    def visit(self, star: typing.Callable[[], T_Result]) -> T_Result:
        if self is StarReadingKind.STAR:
            return star()
