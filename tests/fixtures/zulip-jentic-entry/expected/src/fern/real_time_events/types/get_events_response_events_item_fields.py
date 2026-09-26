

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.custom_profile_field import CustomProfileField
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_fields_type import GetEventsResponseEventsItemFieldsType


class GetEventsResponseEventsItemFields(UniversalBaseModel):
    """
    Event sent to all users in a Zulip organization when new custom
    profile field types are configured for that Zulip organization.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemFieldsType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    fields: typing.Optional[typing.List[CustomProfileField]] = pydantic.Field(default=None)
    """
    An array of dictionaries where each dictionary contains
    details of a single new custom profile field for the Zulip
    organization.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
