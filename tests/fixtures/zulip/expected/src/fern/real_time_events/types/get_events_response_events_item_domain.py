

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_domain_op import GetEventsResponseEventsItemDomainOp
from .get_events_response_events_item_domain_type import GetEventsResponseEventsItemDomainType


class GetEventsResponseEventsItemDomain(UniversalBaseModel):
    """
    Event sent to all users in a Zulip organization when a domain has been
    removed from the set of [allowed domains for account creation and email
    changes](/help/restrict-account-creation#configuring-email-domain-restrictions).
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemDomainType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemDomainOp] = None
    domain: typing.Optional[str] = pydantic.Field(default=None)
    """
    The domain to be removed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
