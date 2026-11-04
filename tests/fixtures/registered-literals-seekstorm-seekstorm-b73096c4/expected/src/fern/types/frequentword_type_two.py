

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FrequentwordTypeTwo(enum.StrEnum):
    """
    German frequent words
    """

    GERMAN = "German"

    def visit(self, german: typing.Callable[[], T_Result]) -> T_Result:
        if self is FrequentwordTypeTwo.GERMAN:
            return german()
