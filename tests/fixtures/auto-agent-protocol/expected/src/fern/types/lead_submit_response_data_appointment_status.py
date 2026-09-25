

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LeadSubmitResponseDataAppointmentStatus(enum.StrEnum):
    """
    Appointment status. `requested` = received but not yet scheduled (staff will follow up). `proposed` = dealer cannot honor the requested time but is offering alternatives in `proposed_times`. `confirmed` = dealer scheduled the appointment for `confirmed_at`. `rejected` = dealer cannot host this appointment (e.g. service unavailable).
    """

    REQUESTED = "requested"
    PROPOSED = "proposed"
    CONFIRMED = "confirmed"
    REJECTED = "rejected"

    def visit(
        self,
        requested: typing.Callable[[], T_Result],
        proposed: typing.Callable[[], T_Result],
        confirmed: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LeadSubmitResponseDataAppointmentStatus.REQUESTED:
            return requested()
        if self is LeadSubmitResponseDataAppointmentStatus.PROPOSED:
            return proposed()
        if self is LeadSubmitResponseDataAppointmentStatus.CONFIRMED:
            return confirmed()
        if self is LeadSubmitResponseDataAppointmentStatus.REJECTED:
            return rejected()
