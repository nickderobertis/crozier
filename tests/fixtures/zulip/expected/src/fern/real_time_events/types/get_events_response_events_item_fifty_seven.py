

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_fifty_seven_op import GetEventsResponseEventsItemFiftySevenOp
from .get_events_response_events_item_fifty_seven_realm_domain import GetEventsResponseEventsItemFiftySevenRealmDomain
from .get_events_response_events_item_fifty_seven_type import GetEventsResponseEventsItemFiftySevenType


class GetEventsResponseEventsItemFiftySeven(UniversalBaseModel):
    """
    Event sent to all users in a Zulip organization when a new domain has been
    added to the set of [allowed domains for account creation and email
    changes](/help/restrict-account-creation#configuring-email-domain-restrictions).
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemFiftySevenType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemFiftySevenOp] = None
    realm_domain: typing.Optional[GetEventsResponseEventsItemFiftySevenRealmDomain] = pydantic.Field(default=None)
    """
    Object containing details of the newly added domain.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
