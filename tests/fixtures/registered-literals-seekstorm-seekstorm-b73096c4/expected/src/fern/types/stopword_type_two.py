

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StopwordTypeTwo(enum.StrEnum):
    """
    German stopwords
    """

    GERMAN = "German"

    def visit(self, german: typing.Callable[[], T_Result]) -> T_Result:
        if self is StopwordTypeTwo.GERMAN:
            return german()
