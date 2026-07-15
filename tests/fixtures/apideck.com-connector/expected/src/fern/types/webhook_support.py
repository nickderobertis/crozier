

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .webhook_support_managed_via import WebhookSupportManagedVia
from .webhook_support_mode import WebhookSupportMode
from .webhook_support_subscription_level import WebhookSupportSubscriptionLevel
from .webhook_support_virtual_webhooks import WebhookSupportVirtualWebhooks


class WebhookSupport(UniversalBaseModel):
    """
    How webhooks are supported for the connector. Sometimes the connector natively supports webhooks, other times Apideck virtualizes them based on polling.
    """

    managed_via: typing.Optional[WebhookSupportManagedVia] = pydantic.Field(default=None)
    """
    How the subscription is managed in the downstream.
    """

    mode: typing.Optional[WebhookSupportMode] = pydantic.Field(default=None)
    """
    Mode of the webhook support.
    """

    subscription_level: typing.Optional[WebhookSupportSubscriptionLevel] = pydantic.Field(default=None)
    """
    Received events are scoped to connection or across integration.
    """

    virtual_webhooks: typing.Optional[WebhookSupportVirtualWebhooks] = pydantic.Field(default=None)
    """
    Virtual webhook config for the connector.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
