

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from ...types.user_group import UserGroup
from .get_events_response_events_item_group_op import GetEventsResponseEventsItemGroupOp
from .get_events_response_events_item_group_type import GetEventsResponseEventsItemGroupType


class GetEventsResponseEventsItemGroup(UniversalBaseModel):
    """
    Event sent to users in an organization when a [user group](/help/user-groups) is created.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemGroupType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemGroupOp] = None
    group: typing.Optional[UserGroup] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
