

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ZoneTriggerTransition(enum.StrEnum):
    """
    Zone monitoring type ('In' for monitoring entering zone and 'Out' for monitoring leaving zone),
    """

    IN = "In"
    OUT = "Out"

    def visit(self, in_: typing.Callable[[], T_Result], out: typing.Callable[[], T_Result]) -> T_Result:
        if self is ZoneTriggerTransition.IN:
            return in_()
        if self is ZoneTriggerTransition.OUT:
            return out()
