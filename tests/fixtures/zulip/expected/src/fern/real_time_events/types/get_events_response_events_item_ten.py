

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_ten_type import GetEventsResponseEventsItemTenType


class GetEventsResponseEventsItemTen(UniversalBaseModel):
    """
    Event sent to a user's clients when the user completes the OAuth flow for
    the [Webex integration](/help/configure-call-provider). Clients need to
    know whether initiating Webex OAuth flow is required before creating a
    Webex call.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemTenType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    value: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean specifying whether the user has a Webex access token.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
