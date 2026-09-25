

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .lead_submit_response_data_appointment_status import LeadSubmitResponseDataAppointmentStatus


class LeadSubmitResponseDataAppointment(UniversalBaseModel):
    """
    Present iff the request included an `appointment` block AND the dealer is acknowledging it (whether confirming, proposing alternatives, leaving it as requested for staff follow-up, or rejecting).
    """

    appointment_id: str = pydantic.Field()
    """
    Dealer-assigned identifier for this appointment.
    """

    status: LeadSubmitResponseDataAppointmentStatus = pydantic.Field()
    """
    Appointment status. `requested` = received but not yet scheduled (staff will follow up). `proposed` = dealer cannot honor the requested time but is offering alternatives in `proposed_times`. `confirmed` = dealer scheduled the appointment for `confirmed_at`. `rejected` = dealer cannot host this appointment (e.g. service unavailable).
    """

    confirmed_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Present iff `status` is `confirmed`. The scheduled start time as an ISO 8601 / RFC 3339 timestamp with timezone offset.
    """

    proposed_times: typing.Optional[typing.List[dt.datetime]] = pydantic.Field(default=None)
    """
    Present iff `status` is `proposed`. Alternative start times the dealer offers, each an ISO 8601 / RFC 3339 timestamp with timezone offset.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
