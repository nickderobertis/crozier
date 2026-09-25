

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_two_op import GetEventsResponseEventsItemTwoOp
from .get_events_response_events_item_two_person import GetEventsResponseEventsItemTwoPerson
from .get_events_response_events_item_two_type import GetEventsResponseEventsItemTwoType


class GetEventsResponseEventsItemTwo(UniversalBaseModel):
    """
    Event sent generally to all users who can access the modified
    user for changes in the set of users or those users metadata.

    **Changes**: Prior to Zulip 8.0 (feature level 228), this event
    was sent to all users in the organization.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemTwoType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemTwoOp] = None
    person: typing.Optional[GetEventsResponseEventsItemTwoPerson] = pydantic.Field(default=None)
    """
    Object containing the changed details of the user.
    It has multiple forms depending on the value changed.
    
    **Changes**: Removed `is_billing_admin` field in Zulip 10.0
    (feature level 363), as it was replaced by the
    `can_manage_billing_group` realm setting.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
