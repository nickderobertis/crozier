

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1webhook_subscriptions_item import V1WebhookSubscriptionsItem


class V1Webhook(UniversalBaseModel):
    id: int = pydantic.Field()
    """
    Unique identifier for the webhook
    """

    account_id: int = pydantic.Field()
    """
    Account ID the webhook belongs to
    """

    url: str = pydantic.Field()
    """
    URL to send webhook payloads to (must be HTTPS)
    """

    subscriptions: typing.List[V1WebhookSubscriptionsItem] = pydantic.Field()
    """
    List of event types to subscribe to
    """

    secret_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    Secret token used to sign webhook payloads for verification
    """

    active: bool = pydantic.Field()
    """
    Whether the webhook is active and will receive events
    """

    custom_headers: typing.Dict[str, str] = pydantic.Field()
    """
    Custom HTTP headers to include in webhook requests
    """

    created_at: dt.datetime = pydantic.Field()
    """
    ISO8601 timestamp of when the webhook was created
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    ISO8601 timestamp of when the webhook was last updated
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
