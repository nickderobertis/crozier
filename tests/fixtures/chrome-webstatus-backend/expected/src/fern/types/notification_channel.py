

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .notification_channel_config import NotificationChannelConfig
from .notification_channel_type import NotificationChannelType


class NotificationChannel(UniversalBaseModel):
    type: NotificationChannelType
    name: str = pydantic.Field()
    """
    The name of the channel.
    """

    config: NotificationChannelConfig = pydantic.Field()
    """
    Configuration specific to the channel type.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
