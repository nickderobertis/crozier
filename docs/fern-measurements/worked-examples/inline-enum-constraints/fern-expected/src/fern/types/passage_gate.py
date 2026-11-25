

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PassageGate(enum.StrEnum):
    """
    Its own `not` rejects the first member.
    """

    UPPER = "upper"
    LOWER = "lower"

    def visit(self, upper: typing.Callable[[], T_Result], lower: typing.Callable[[], T_Result]) -> T_Result:
        if self is PassageGate.UPPER:
            return upper()
        if self is PassageGate.LOWER:
            return lower()
