

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_sixty_six_op import GetEventsResponseEventsItemSixtySixOp
from .get_events_response_events_item_sixty_six_type import GetEventsResponseEventsItemSixtySixType
from .get_events_response_events_item_sixty_six_value import GetEventsResponseEventsItemSixtySixValue


class GetEventsResponseEventsItemSixtySix(UniversalBaseModel):
    """
    The simpler of two possible event types sent to all users
    in a Zulip organization when the configuration of the
    organization (realm) has changed.

    Often individual settings are migrated from this format to
    the [realm/update_dict](#realm-update_dict) event format when additional realm
    settings are added whose values are coupled to each other
    in some way. The specific values supported by this event
    type are documented in the [realm/update_dict](#realm-update_dict)
    documentation.

    A correct client implementation should convert these
    events into the corresponding [realm/update_dict](#realm-update_dict)
    event and then process that.

    **Changes**: Removed the `rendered_description` property in
    Zulip 12.0 (feature level 464). It had been briefly present only
    since feature level 462 and can be safely ignored by all clients.

    Removed `extra_data` optional property in Zulip 10.0 (feature level 306).
    The `extra_data` used to include an `upload_quota` field when changed
    property was `plan_type`. The server now sends a standard
    `realm/update_dict` event for plan changes.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemSixtySixType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemSixtySixOp] = None
    property: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the property that was changed.
    """

    value: typing.Optional[GetEventsResponseEventsItemSixtySixValue] = pydantic.Field(default=None)
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
