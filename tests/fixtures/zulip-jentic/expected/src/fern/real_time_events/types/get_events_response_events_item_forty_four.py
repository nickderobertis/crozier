

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_forty_four_data import GetEventsResponseEventsItemFortyFourData
from .get_events_response_events_item_forty_four_op import GetEventsResponseEventsItemFortyFourOp
from .get_events_response_events_item_forty_four_type import GetEventsResponseEventsItemFortyFourType


class GetEventsResponseEventsItemFortyFour(UniversalBaseModel):
    """
    Event sent to all users in a Zulip organization
    when a property of a user group is changed.

    For group deactivation, this event is only sent
    if `include_deactivated_groups` client capability
    is set to `true`.

    This event is also sent when deactivating or reactivating
    a user for settings set to anonymous user groups which the
    user is direct member of. When deactivating the user, event
    is only sent to users who cannot access the deactivated user.

    **Changes**: Starting with Zulip 10.0 (feature level 303), this
    event can also be sent when deactivating or reactivating a user.

    Prior to Zulip 10.0 (feature level 294), this event was sent to
    all clients when a user group was deactivated.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemFortyFourType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemFortyFourOp] = None
    group_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the user group whose details have changed.
    """

    data: typing.Optional[GetEventsResponseEventsItemFortyFourData] = pydantic.Field(default=None)
    """
    Dictionary containing the changed details of the user group.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
