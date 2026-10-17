

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Relation(enum.StrEnum):
    """
    How a reading is weighed against the threshold.
    """

    BELOW = "<"
    """
    The reading is under the threshold.
    """

    DIFFERS = "!="
    """
    The reading is anything but the threshold.
    """

    def visit(self, below: typing.Callable[[], T_Result], differs: typing.Callable[[], T_Result]) -> T_Result:
        if self is Relation.BELOW:
            return below()
        if self is Relation.DIFFERS:
            return differs()
