

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_twenty_three_op import GetEventsResponseEventsItemTwentyThreeOp
from .get_events_response_events_item_twenty_three_type import GetEventsResponseEventsItemTwentyThreeType


class GetEventsResponseEventsItemTwentyThree(UniversalBaseModel):
    """
    Event sent to a user's clients when they deregister a device.

    Helps clients to live-update the `devices` dictionary
    returned in [`POST /register`](/api/register-queue) response.

    **Changes**: New in Zulip 12.0 (feature level 468).
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemTwentyThreeType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemTwentyThreeOp] = None
    device_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the device which deregistered.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
