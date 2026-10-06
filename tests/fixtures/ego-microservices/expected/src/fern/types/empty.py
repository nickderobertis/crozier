

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Empty(enum.StrEnum):
    """
    An enumeration.
    """

    UNSET = "UNSET"

    def visit(self, unset: typing.Callable[[], T_Result]) -> T_Result:
        if self is Empty.UNSET:
            return unset()
