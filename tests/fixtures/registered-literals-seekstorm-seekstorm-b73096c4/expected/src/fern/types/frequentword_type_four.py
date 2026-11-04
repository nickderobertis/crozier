

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FrequentwordTypeFour(enum.StrEnum):
    """
    Spanish frequent words
    """

    SPANISH = "Spanish"

    def visit(self, spanish: typing.Callable[[], T_Result]) -> T_Result:
        if self is FrequentwordTypeFour.SPANISH:
            return spanish()
