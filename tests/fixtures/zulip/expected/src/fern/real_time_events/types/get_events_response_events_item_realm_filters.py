

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_realm_filters_realm_filters_item_item import (
    GetEventsResponseEventsItemRealmFiltersRealmFiltersItemItem,
)
from .get_events_response_events_item_realm_filters_type import GetEventsResponseEventsItemRealmFiltersType


class GetEventsResponseEventsItemRealmFilters(UniversalBaseModel):
    """
    Legacy event type that is no longer sent to clients. Previously, sent
    to all users in a Zulip organization when the set of configured
    [linkifiers](/help/add-a-custom-linkifier) for the organization was
    changed.

    **Changes**: Prior to Zulip 7.0 (feature level 176), this event type
    was sent to clients.

    **Deprecated** in Zulip 4.0 (feature level 54), and replaced by the
    `realm_linkifiers` event type, which has a clearer name and format.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemRealmFiltersType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    realm_filters: typing.Optional[
        typing.List[typing.List[GetEventsResponseEventsItemRealmFiltersRealmFiltersItemItem]]
    ] = pydantic.Field(default=None)
    """
    An array of tuples, where each tuple described a linkifier. The first
    element of the tuple was a string regex pattern which represented the
    pattern to be linkified on matching, for example `"#(?P<id>[123])"`.
    The second element was the URL format string that the pattern should be
    linkified with. A URL format string for the above example would be
    `"https://realm.com/my_realm_filter/%(id)s"`. And the third element
    was the ID of the realm filter.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
