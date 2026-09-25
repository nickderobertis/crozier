

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_ten_type import GetEventsResponseEventsItemTenType


class GetEventsResponseEventsItemTen(UniversalBaseModel):
    """
    A simple event sent when the set of invitations changes.
    This event is sent to organization administrators and the creator of
    the changed invitation; this tells clients they need to refetch
    data from `GET /invites` if they are displaying UI containing active
    invitations.

    **Changes**: Before Zulip 8.0 (feature level 209), this event was
    only sent to organization administrators.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemTenType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
