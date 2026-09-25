

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_forty_eight_op import GetEventsResponseEventsItemFortyEightOp
from .get_events_response_events_item_forty_eight_type import GetEventsResponseEventsItemFortyEightType


class GetEventsResponseEventsItemFortyEight(UniversalBaseModel):
    """
    Event sent to all users when subgroups have been added to
    a user group.

    **Changes**: New in Zulip 6.0 (feature level 127).
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemFortyEightType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemFortyEightOp] = None
    group_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the user group whose details have changed.
    """

    direct_subgroup_ids: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    Array containing the IDs of the subgroups that have been added
    to the user group.
    
    **Changes**: New in Zulip 6.0 (feature level 131).
    Previously, this was called `subgroup_ids`, but
    clients can ignore older events as this feature level
    predates subgroups being fully implemented.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
