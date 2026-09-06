

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.notification_settings import NotificationSettings
from .get_notifications_response_data import GetNotificationsResponseData


class GetNotificationsResponse(UniversalBaseModel):
    data: typing.Optional[GetNotificationsResponseData] = None
    settings: typing.Optional[NotificationSettings] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
