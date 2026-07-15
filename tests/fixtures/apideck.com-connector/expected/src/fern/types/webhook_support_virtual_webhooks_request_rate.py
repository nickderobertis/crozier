

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .webhook_support_virtual_webhooks_request_rate_unit import WebhookSupportVirtualWebhooksRequestRateUnit


class WebhookSupportVirtualWebhooksRequestRate(UniversalBaseModel):
    """
    The rate at which requests for resources will be made to downstream.
    """

    rate: int = pydantic.Field()
    """
    The number of requests per window unit.
    """

    size: int = pydantic.Field()
    """
    Size of request window.
    """

    unit: WebhookSupportVirtualWebhooksRequestRateUnit = pydantic.Field()
    """
    The window unit for the rate.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
