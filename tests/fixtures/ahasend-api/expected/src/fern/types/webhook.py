

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .webhook_object import WebhookObject
from .webhook_scope import WebhookScope


class Webhook(UniversalBaseModel):
    object: WebhookObject = pydantic.Field()
    """
    Object type identifier
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the webhook
    """

    created_at: dt.datetime = pydantic.Field()
    """
    When the webhook was created
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    When the webhook was last updated
    """

    name: str = pydantic.Field()
    """
    Webhook name
    """

    url: str = pydantic.Field()
    """
    Webhook URL
    """

    enabled: bool = pydantic.Field()
    """
    Whether the webhook is enabled
    """

    on_reception: bool = pydantic.Field()
    """
    Trigger on message reception
    """

    on_delivered: bool = pydantic.Field()
    """
    Trigger on message delivery
    """

    on_transient_error: bool = pydantic.Field()
    """
    Trigger on transient errors
    """

    on_failed: bool = pydantic.Field()
    """
    Trigger on permanent failures
    """

    on_bounced: bool = pydantic.Field()
    """
    Trigger on bounces
    """

    on_suppressed: bool = pydantic.Field()
    """
    Trigger on suppressions
    """

    on_opened: bool = pydantic.Field()
    """
    Trigger on opens
    """

    on_clicked: bool = pydantic.Field()
    """
    Trigger on clicks
    """

    on_suppression_created: bool = pydantic.Field()
    """
    Trigger on suppression creation
    """

    on_dns_error: bool = pydantic.Field()
    """
    Trigger on DNS errors
    """

    scope: WebhookScope = pydantic.Field()
    """
    Webhook scope
    """

    domains: typing.List[str] = pydantic.Field()
    """
    Domains this webhook applies to. Always present; global webhooks return an empty array.
    """

    success_count: int = pydantic.Field()
    """
    Number of successful calls
    """

    error_count: int = pydantic.Field()
    """
    Number of unsuccessful calls
    """

    errors_since_last_success: int = pydantic.Field()
    """
    Number of consecutive failed calls. Reset to zero by the next
    successful call.
    """

    last_request_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the webhook was last called
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
