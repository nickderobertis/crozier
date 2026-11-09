

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .alert_notifications_item_notification_type import AlertNotificationsItemNotificationType


class AlertNotificationsItem(UniversalBaseModel):
    notification_type: typing.Optional[AlertNotificationsItemNotificationType] = pydantic.Field(default=None)
    """
    The type of notification
    """

    recipients: typing.Optional[str] = pydantic.Field(default=None)
    """
    The recipients of the notification
    """

    status: typing.Optional[float] = pydantic.Field(default=None)
    """
    The status of the notification
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
