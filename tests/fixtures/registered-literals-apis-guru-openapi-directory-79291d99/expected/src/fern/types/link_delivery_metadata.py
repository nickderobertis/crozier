

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .link_delivery_webhook_communication_method import LinkDeliveryWebhookCommunicationMethod
from .link_delivery_webhook_delivery_status import LinkDeliveryWebhookDeliveryStatus


class LinkDeliveryMetadata(UniversalBaseModel):
    """
    Information related to the related to the delivery of the link session to users
    """

    communication_method: typing.Optional[LinkDeliveryWebhookCommunicationMethod] = None
    delivery_status: typing.Optional[LinkDeliveryWebhookDeliveryStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
