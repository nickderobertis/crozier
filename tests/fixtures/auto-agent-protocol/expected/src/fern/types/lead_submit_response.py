

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .lead_submit_response_data import LeadSubmitResponseData
from .lead_submit_response_type import LeadSubmitResponseType


class LeadSubmitResponse(UniversalBaseModel):
    """
    Dealer agent's response to a `lead.submit.request`. Carries the assigned `lead_id` and overall lead `status`, plus an optional appointment block when the request included an `appointment` (the dealer can confirm the requested time, propose alternatives, leave it as merely requested for human follow-up, or reject the appointment while still accepting the lead). Carried inside an A2A `Message.parts[].data` DataPart via `SendMessage`.
    """

    type: LeadSubmitResponseType = pydantic.Field()
    """
    AAP message type discriminator.
    """

    data: LeadSubmitResponseData
    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Contextual note from the dealer (e.g. 'A salesperson will call within 1 business hour.', 'We are unable to honor your requested time; please pick from the alternatives.').
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
