

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .delivery_method import DeliveryMethod
from .message_subscription_webhook_v2beta import MessageSubscriptionWebhookV2Beta


class BenchlingAppManifestSubscriptions(UniversalBaseModel):
    """
    Subscriptions allow an app to receive notifications when certain actions and changes occur in Benchling.
    """

    delivery_method: typing_extensions.Annotated[
        DeliveryMethod, FieldMetadata(alias="deliveryMethod"), pydantic.Field(alias="deliveryMethod")
    ]
    messages: typing.List[MessageSubscriptionWebhookV2Beta]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
