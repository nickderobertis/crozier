

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QueryOutputInterpolationOneFour(enum.StrEnum):
    """
    Use the value that is closest in time.
    """

    NEAREST = "nearest"

    def visit(self, nearest: typing.Callable[[], T_Result]) -> T_Result:
        if self is QueryOutputInterpolationOneFour.NEAREST:
            return nearest()
