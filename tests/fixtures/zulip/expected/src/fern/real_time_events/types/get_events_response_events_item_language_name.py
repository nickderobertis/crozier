

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_language_name_op import GetEventsResponseEventsItemLanguageNameOp
from .get_events_response_events_item_language_name_type import GetEventsResponseEventsItemLanguageNameType
from .get_events_response_events_item_language_name_value import GetEventsResponseEventsItemLanguageNameValue


class GetEventsResponseEventsItemLanguageName(UniversalBaseModel):
    """
    Event sent to a user's clients when that user's settings have changed.

    **Changes**: In Zulip 12.0 (feature level 439), the deprecated, legacy
    `update_display_settings` and `update_global_notifications` event types
    were removed entirely. All clients should be using this event type for
    updates to a user's settings.

    New in Zulip 5.0 (feature level 89), replaced and deprecated the
    `update_display_settings` and `update_global_notifications` event types.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemLanguageNameType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemLanguageNameOp] = None
    property: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the changed setting.
    """

    value: typing.Optional[GetEventsResponseEventsItemLanguageNameValue] = pydantic.Field(default=None)
    """
    New value of the changed setting.
    """

    language_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present only if the setting to be changed is
    `default_language`. Contains the name of the
    new default language in English.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
