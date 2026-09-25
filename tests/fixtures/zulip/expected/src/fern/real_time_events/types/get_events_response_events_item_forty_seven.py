

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_forty_seven_op import GetEventsResponseEventsItemFortySevenOp
from .get_events_response_events_item_forty_seven_type import GetEventsResponseEventsItemFortySevenType


class GetEventsResponseEventsItemFortySeven(UniversalBaseModel):
    """
    Event sent to all users when users have been removed from
    a user group.

    This event is also sent when deactivating a user, for all
    the user groups the deactivated user is a member of, but only
    to the users who cannot access the deactivated user.

    **Changes**: Starting with Zulip 10.0 (feature level 303),
    this event can also be sent when deactivating a user.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemFortySevenType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemFortySevenOp] = None
    group_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the user group whose details have changed.
    """

    user_ids: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    Array containing the IDs of the users who have been removed
    from the user group.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
