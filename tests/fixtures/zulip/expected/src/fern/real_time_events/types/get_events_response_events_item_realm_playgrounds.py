

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from ...types.realm_playground import RealmPlayground
from .get_events_response_events_item_realm_playgrounds_type import GetEventsResponseEventsItemRealmPlaygroundsType


class GetEventsResponseEventsItemRealmPlaygrounds(UniversalBaseModel):
    """
    Event sent to all users in a Zulip organization when the
    set of configured [code playgrounds](/help/code-blocks#code-playgrounds)
    for the organization has changed.

    **Changes**: New in Zulip 4.0 (feature level 49).
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemRealmPlaygroundsType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    realm_playgrounds: typing.Optional[typing.List[RealmPlayground]] = pydantic.Field(default=None)
    """
    An array of dictionaries where each dictionary contains
    data about a single playground entry.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
