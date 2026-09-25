

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1webhooks_update_webhook_subscriptions_item import V1WebhooksUpdateWebhookSubscriptionsItem


class V1WebhooksUpdateWebhook(UniversalBaseModel):
    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL to send webhook payloads to (must be HTTPS)
    """

    subscriptions: typing.Optional[typing.List[V1WebhooksUpdateWebhookSubscriptionsItem]] = pydantic.Field(default=None)
    """
    List of event types to subscribe to
    """

    secret_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    Secret token used to sign webhook payloads. The signature will be included in the X-Signature header.
    """

    active: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the webhook is active
    """

    custom_headers: typing.Optional[typing.Dict[str, typing.Optional[str]]] = pydantic.Field(default=None)
    """
    Custom HTTP headers to include in webhook requests
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
