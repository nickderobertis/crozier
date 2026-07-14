

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .analysis_update_notification_data import AnalysisUpdateNotificationData
from .notification_base import NotificationBase


class AnalysisUpdateNotification(NotificationBase):
    data: typing.Optional[AnalysisUpdateNotificationData] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
