

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .notification_base import NotificationBase
from .tag_update_notification_data import TagUpdateNotificationData


class TagUpdateNotification(NotificationBase):
    data: typing.Optional[TagUpdateNotificationData] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
