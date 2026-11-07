

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StopwordTypeFour(enum.StrEnum):
    """
    Spanish stopwords
    """

    SPANISH = "Spanish"

    def visit(self, spanish: typing.Callable[[], T_Result]) -> T_Result:
        if self is StopwordTypeFour.SPANISH:
            return spanish()
