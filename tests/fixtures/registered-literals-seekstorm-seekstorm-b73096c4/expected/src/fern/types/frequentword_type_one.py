

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FrequentwordTypeOne(enum.StrEnum):
    """
    English frequent words
    """

    ENGLISH = "English"

    def visit(self, english: typing.Callable[[], T_Result]) -> T_Result:
        if self is FrequentwordTypeOne.ENGLISH:
            return english()
