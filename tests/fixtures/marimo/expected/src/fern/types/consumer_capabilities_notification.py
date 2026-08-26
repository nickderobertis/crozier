

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .consumer_capabilities import ConsumerCapabilities
from .consumer_capabilities_notification_op import ConsumerCapabilitiesNotificationOp


class ConsumerCapabilitiesNotification(UniversalBaseModel):
    """
    Notification of the frontend consumer's capabilities.
    """

    consumer_capabilities: ConsumerCapabilities
    op: ConsumerCapabilitiesNotificationOp

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
