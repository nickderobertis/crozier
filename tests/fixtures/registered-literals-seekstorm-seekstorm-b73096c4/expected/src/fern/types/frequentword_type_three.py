

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FrequentwordTypeThree(enum.StrEnum):
    """
    French frequent words
    """

    FRENCH = "French"

    def visit(self, french: typing.Callable[[], T_Result]) -> T_Result:
        if self is FrequentwordTypeThree.FRENCH:
            return french()
