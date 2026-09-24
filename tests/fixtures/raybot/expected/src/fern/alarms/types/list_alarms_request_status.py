

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListAlarmsRequestStatus(enum.StrEnum):
    ACTIVE = "ACTIVE"
    DEACTIVE = "DEACTIVE"

    def visit(self, active: typing.Callable[[], T_Result], deactive: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListAlarmsRequestStatus.ACTIVE:
            return active()
        if self is ListAlarmsRequestStatus.DEACTIVE:
            return deactive()
