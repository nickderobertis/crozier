

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_fifty_eight_op import GetEventsResponseEventsItemFiftyEightOp
from .get_events_response_events_item_fifty_eight_realm_domain import GetEventsResponseEventsItemFiftyEightRealmDomain
from .get_events_response_events_item_fifty_eight_type import GetEventsResponseEventsItemFiftyEightType


class GetEventsResponseEventsItemFiftyEight(UniversalBaseModel):
    """
    Event sent to all users in a Zulip organization when the set of
    [allowed domains for account creation and email
    changes](/help/restrict-account-creation#configuring-email-domain-restrictions)
    has changed.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemFiftyEightType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemFiftyEightOp] = None
    realm_domain: typing.Optional[GetEventsResponseEventsItemFiftyEightRealmDomain] = pydantic.Field(default=None)
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
