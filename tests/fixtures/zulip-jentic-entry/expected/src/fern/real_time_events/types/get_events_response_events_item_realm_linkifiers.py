

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_realm_linkifiers_realm_linkifiers_item import (
    GetEventsResponseEventsItemRealmLinkifiersRealmLinkifiersItem,
)
from .get_events_response_events_item_realm_linkifiers_type import GetEventsResponseEventsItemRealmLinkifiersType


class GetEventsResponseEventsItemRealmLinkifiers(UniversalBaseModel):
    """
    Event sent to all users in a Zulip organization when the
    set of configured [linkifiers](/help/add-a-custom-linkifier)
    for the organization has changed.

    Processing this event is important for doing Markdown local echo
    correctly.

    Clients will not receive this event unless the event queue is
    registered with the client capability
    `{"linkifier_url_template": true}`.
    See [`POST /register`](/api/register-queue#parameter-client_capabilities)
    for how client capabilities can be specified.

    **Changes**: Before Zulip 7.0 (feature level 176), the
    `linkifier_url_template` client capability was not required. The
    requirement was added because linkifiers were updated to contain
    a URL template instead of a URL format string, which was not a
    backwards-compatible change.

    New in Zulip 4.0 (feature level 54), replacing the deprecated
    `realm_filters` event type.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemRealmLinkifiersType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    realm_linkifiers: typing.Optional[typing.List[GetEventsResponseEventsItemRealmLinkifiersRealmLinkifiersItem]] = (
        pydantic.Field(default=None)
    )
    """
    An ordered array of dictionaries where each dictionary contains
    details about a single linkifier.
    
    Clients should always process linkifiers in the order given;
    this is important if the realm has linkifiers with overlapping
    patterns. The order can be modified using [`PATCH
    /realm/linkifiers`](/api/reorder-linkifiers).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
