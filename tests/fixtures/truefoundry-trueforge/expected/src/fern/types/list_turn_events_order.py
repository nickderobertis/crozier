

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListTurnEventsOrder(enum.StrEnum):
    """
    Sort events by insertion order. Defaults to "asc".
    """

    ASC = "asc"
    DESC = "desc"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListTurnEventsOrder.ASC:
            return asc()
        if self is ListTurnEventsOrder.DESC:
            return desc()
