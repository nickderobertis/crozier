

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StopwordTypeZero(enum.StrEnum):
    """
    No stopwords
    """

    NONE = "None"

    def visit(self, none: typing.Callable[[], T_Result]) -> T_Result:
        if self is StopwordTypeZero.NONE:
            return none()
