

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .authentication_notification_data import AuthenticationNotificationData
from .authentication_notification_request_type import AuthenticationNotificationRequestType


class AuthenticationNotificationRequest(UniversalBaseModel):
    data: AuthenticationNotificationData = pydantic.Field()
    """
    Contains event details.
    """

    environment: str = pydantic.Field()
    """
    The environment from which the webhook originated.
    
    Possible values: **test**, **live**.
    """

    timestamp: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the event was queued.
    """

    type: AuthenticationNotificationRequestType = pydantic.Field()
    """
    Type of notification.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
