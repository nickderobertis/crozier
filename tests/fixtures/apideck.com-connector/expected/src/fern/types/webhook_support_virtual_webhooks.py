

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .webhook_support_virtual_webhooks_request_rate import WebhookSupportVirtualWebhooksRequestRate


class WebhookSupportVirtualWebhooks(UniversalBaseModel):
    """
    Virtual webhook config for the connector.
    """

    request_rate: WebhookSupportVirtualWebhooksRequestRate = pydantic.Field()
    """
    The rate at which requests for resources will be made to downstream.
    """

    resources: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The resources that will be requested from downstream.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
