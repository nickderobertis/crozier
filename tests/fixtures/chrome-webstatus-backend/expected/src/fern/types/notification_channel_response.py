

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .generic_updatable_unique_model import GenericUpdatableUniqueModel
from .notification_channel import NotificationChannel
from .notification_channel_response_status import NotificationChannelResponseStatus


class NotificationChannelResponse(GenericUpdatableUniqueModel, NotificationChannel):
    status: NotificationChannelResponseStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
