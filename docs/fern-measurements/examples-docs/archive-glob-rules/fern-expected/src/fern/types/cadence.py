

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Cadence(enum.StrEnum):
    """
    How often rotation runs across tier/* /hosts.
    """

    DAILY = "daily"
    WEEKLY = "weekly"

    def visit(self, daily: typing.Callable[[], T_Result], weekly: typing.Callable[[], T_Result]) -> T_Result:
        if self is Cadence.DAILY:
            return daily()
        if self is Cadence.WEEKLY:
            return weekly()
