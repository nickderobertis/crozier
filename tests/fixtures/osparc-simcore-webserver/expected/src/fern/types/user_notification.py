

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .notification_category import NotificationCategory
from .user_id_int import UserIdInt
from .user_notification_product import UserNotificationProduct
from .user_notification_resource_id import UserNotificationResourceId


class UserNotification(UniversalBaseModel):
    user_id: UserIdInt
    category: NotificationCategory
    actionable_path: str
    title: str
    text: str
    date: dt.datetime
    product: typing.Optional[UserNotificationProduct] = None
    resource_id: typing.Optional[UserNotificationResourceId] = None
    user_from_id: typing.Optional[UserIdInt] = None
    id: str
    read: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
