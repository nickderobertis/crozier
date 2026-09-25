

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_realm_id_op import GetEventsResponseEventsItemRealmIdOp
from .get_events_response_events_item_realm_id_type import GetEventsResponseEventsItemRealmIdType


class GetEventsResponseEventsItemRealmId(UniversalBaseModel):
    """
    Event sent to all users in a Zulip organization when the
    organization (realm) is deactivated. Its main purpose is to
    flush active longpolling connections so clients can immediately
    show the organization as deactivated.

    Clients cannot rely on receiving this event, because they will
    no longer be able to authenticate to the Zulip API due to the
    deactivation, and thus can miss it if they did not have an active
    longpolling connection at the moment of deactivation.

    Correct handling of realm deactivations requires that clients
    parse authentication errors from GET /events; if that is done
    correctly, the client can ignore this event type and rely on its
    handling of the `GET /events` request it will do immediately
    after processing this batch of events.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemRealmIdType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemRealmIdOp] = None
    realm_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the deactivated realm.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
