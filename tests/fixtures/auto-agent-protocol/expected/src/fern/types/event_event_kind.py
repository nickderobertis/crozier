

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EventEventKind(enum.StrEnum):
    """
    Concrete event kind. v1.0 defines two kinds; future versions may add more.
    """

    LEAD_STATUS_CHANGED = "lead.status_changed"
    APPOINTMENT_STATUS_CHANGED = "appointment.status_changed"

    def visit(
        self,
        lead_status_changed: typing.Callable[[], T_Result],
        appointment_status_changed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EventEventKind.LEAD_STATUS_CHANGED:
            return lead_status_changed()
        if self is EventEventKind.APPOINTMENT_STATUS_CHANGED:
            return appointment_status_changed()
