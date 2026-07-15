

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .created_at import CreatedAt
from .delivery_url import DeliveryUrl
from .description import Description
from .execute_base_url import ExecuteBaseUrl
from .status import Status
from .unified_api_id import UnifiedApiId
from .updated_at import UpdatedAt
from .webhook_disabled_reason import WebhookDisabledReason
from .webhook_event_type import WebhookEventType


class Webhook(UniversalBaseModel):
    created_at: typing.Optional[CreatedAt] = None
    delivery_url: DeliveryUrl
    description: typing.Optional[Description] = None
    disabled_reason: typing.Optional[WebhookDisabledReason] = pydantic.Field(default=None)
    """
    Indicates if the webhook has has been disabled as it reached its retry limit or if account is over the usage allocated by it's plan.
    """

    events: typing.List[WebhookEventType] = pydantic.Field()
    """
    The list of subscribed events for this webhook. [`*`] indicates that all events are enabled.
    """

    execute_base_url: typing.Optional[ExecuteBaseUrl] = None
    id: typing.Optional[str] = None
    status: Status
    unified_api: UnifiedApiId
    updated_at: typing.Optional[UpdatedAt] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
