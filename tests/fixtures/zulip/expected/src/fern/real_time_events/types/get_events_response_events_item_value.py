

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_value_op import GetEventsResponseEventsItemValueOp
from .get_events_response_events_item_value_type import GetEventsResponseEventsItemValueType
from .get_events_response_events_item_value_value import GetEventsResponseEventsItemValueValue


class GetEventsResponseEventsItemValue(UniversalBaseModel):
    """
    Event sent to all users in a Zulip organization when the
    [default settings for new users][new-user-defaults]
    of the organization (realm) have changed.

    [new-user-defaults]: /help/configure-default-new-user-settings

    See [PATCH /realm/user_settings_defaults](/api/update-realm-user-settings-defaults)
    for details on possible properties.

    **Changes**: New in Zulip 5.0 (feature level 95).
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemValueType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemValueOp] = None
    property: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the property that was changed.
    """

    value: typing.Optional[GetEventsResponseEventsItemValueValue] = pydantic.Field(default=None)
    """
    The new value of the property.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
