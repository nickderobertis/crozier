

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FrequentwordTypeZero(enum.StrEnum):
    """
    No frequent words
    """

    NONE = "None"

    def visit(self, none: typing.Callable[[], T_Result]) -> T_Result:
        if self is FrequentwordTypeZero.NONE:
            return none()
