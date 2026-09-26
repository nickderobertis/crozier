

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_person_op import GetEventsResponseEventsItemPersonOp
from .get_events_response_events_item_person_person import GetEventsResponseEventsItemPersonPerson
from .get_events_response_events_item_person_type import GetEventsResponseEventsItemPersonType


class GetEventsResponseEventsItemPerson(UniversalBaseModel):
    """
    Event sent to guest users when they lose access to a user.

    **Changes**: As of Zulip 8.0 (feature level 228), this event is no
    longer deprecated.

    In Zulip 8.0 (feature level 222), this event was deprecated and no
    longer sent to clients. Prior to this feature level, it was sent to all
    users in a Zulip organization when a user was deactivated.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemPersonType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemPersonOp] = None
    person: typing.Optional[GetEventsResponseEventsItemPersonPerson] = pydantic.Field(default=None)
    """
    Object containing details of the deactivated user.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
