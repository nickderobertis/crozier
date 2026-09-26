

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_consented_type import GetEventsResponseEventsItemConsentedType


class GetEventsResponseEventsItemConsented(UniversalBaseModel):
    """
    Event sent to administrators when the [data export
    consent][help-export-consent] status for a user changes, whether due
    to a user changing their consent preferences or a user being created
    or reactivated (since user creation/activation events do not contain
    these data).

    [help-export-consent]: /help/export-your-organization#configure-whether-administrators-can-export-your-private-data

    **Changes**: New in Zulip 10.0 (feature level 312). Previously,
    there was not event available to administrators with these data.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemConsentedType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the user whose setting was changed.
    """

    consented: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the user has consented for their private data export.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
