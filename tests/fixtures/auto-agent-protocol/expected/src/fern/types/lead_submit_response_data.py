

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .lead_submit_response_data_appointment import LeadSubmitResponseDataAppointment
from .lead_submit_response_data_dealer import LeadSubmitResponseDataDealer
from .lead_submit_response_data_status import LeadSubmitResponseDataStatus


class LeadSubmitResponseData(UniversalBaseModel):
    lead_id: str = pydantic.Field()
    """
    Dealer-assigned identifier for this lead.
    """

    status: LeadSubmitResponseDataStatus = pydantic.Field()
    """
    Overall lead status. `duplicate` indicates the dealer recognized the same buyer/vehicle combination from a recent prior submission and merged it. `rejected` indicates the dealer did not accept the lead (e.g. consent invalid, vehicle no longer available, dealer not serving the buyer's region).
    """

    appointment: typing.Optional[LeadSubmitResponseDataAppointment] = pydantic.Field(default=None)
    """
    Present iff the request included an `appointment` block AND the dealer is acknowledging it (whether confirming, proposing alternatives, leaving it as requested for staff follow-up, or rejecting).
    """

    dealer: typing.Optional[LeadSubmitResponseDataDealer] = pydantic.Field(default=None)
    """
    Convenience contact summary for the buyer agent to surface follow-up details to the user.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
