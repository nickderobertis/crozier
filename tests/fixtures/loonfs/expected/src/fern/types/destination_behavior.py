

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DestinationBehavior(enum.StrEnum):
    """
    What a path put, move, or copy does when the destination already exists.
    """

    NO_REPLACE = "no_replace"
    REPLACE = "replace"

    def visit(self, no_replace: typing.Callable[[], T_Result], replace: typing.Callable[[], T_Result]) -> T_Result:
        if self is DestinationBehavior.NO_REPLACE:
            return no_replace()
        if self is DestinationBehavior.REPLACE:
            return replace()
