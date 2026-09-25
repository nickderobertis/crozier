

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_fifty_five_op import GetEventsResponseEventsItemFiftyFiveOp
from .get_events_response_events_item_fifty_five_realm_domain import GetEventsResponseEventsItemFiftyFiveRealmDomain
from .get_events_response_events_item_fifty_five_type import GetEventsResponseEventsItemFiftyFiveType


class GetEventsResponseEventsItemFiftyFive(UniversalBaseModel):
    """
    Event sent to all users in a Zulip organization when the set of
    [allowed domains for new users](/help/restrict-account-creation#configuring-email-domain-restrictions)
    has changed.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemFiftyFiveType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemFiftyFiveOp] = None
    realm_domain: typing.Optional[GetEventsResponseEventsItemFiftyFiveRealmDomain] = pydantic.Field(default=None)
    """
    Object containing details of the edited domain.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
