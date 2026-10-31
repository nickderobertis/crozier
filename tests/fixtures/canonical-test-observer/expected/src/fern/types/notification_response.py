

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .notification_type import NotificationType


class NotificationResponse(UniversalBaseModel):
    id: int
    user_id: int
    notification_type: NotificationType
    target_url: typing.Optional[str] = None
    created_at: dt.datetime
    dismissed_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
