

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .connection_webhook_disabled_reason import ConnectionWebhookDisabledReason
from .connection_webhook_events_item import ConnectionWebhookEventsItem
from .connection_webhook_status import ConnectionWebhookStatus
from .unified_api_id import UnifiedApiId


class ConnectionWebhook(UniversalBaseModel):
    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time when the object was created.
    """

    delivery_url: str = pydantic.Field()
    """
    The delivery url of the webhook endpoint.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A description of the object.
    """

    disabled_reason: typing.Optional[ConnectionWebhookDisabledReason] = pydantic.Field(default=None)
    """
    Indicates if the webhook has has been disabled as it reached its retry limit or if account is over the usage allocated by it's plan.
    """

    events: typing.List[ConnectionWebhookEventsItem] = pydantic.Field()
    """
    The list of subscribed events for this webhook. [`*`] indicates that all events are enabled.
    """

    execute_base_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Unify Base URL events from connectors will be sent to after service id is appended.
    """

    id: typing.Optional[str] = None
    status: ConnectionWebhookStatus = pydantic.Field()
    """
    The status of the webhook.
    """

    unified_api: UnifiedApiId
    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time when the object was last updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
