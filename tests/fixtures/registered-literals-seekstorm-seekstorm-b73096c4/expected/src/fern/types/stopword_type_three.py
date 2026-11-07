

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StopwordTypeThree(enum.StrEnum):
    """
    French stopwords
    """

    FRENCH = "French"

    def visit(self, french: typing.Callable[[], T_Result]) -> T_Result:
        if self is StopwordTypeThree.FRENCH:
            return french()
