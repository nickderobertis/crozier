

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StopwordTypeOne(enum.StrEnum):
    """
    English stopwords
    """

    ENGLISH = "English"

    def visit(self, english: typing.Callable[[], T_Result]) -> T_Result:
        if self is StopwordTypeOne.ENGLISH:
            return english()
