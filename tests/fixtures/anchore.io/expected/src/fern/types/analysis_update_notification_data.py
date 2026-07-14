

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .analysis_update_notification_payload import AnalysisUpdateNotificationPayload
from .base_notification_data import BaseNotificationData


class AnalysisUpdateNotificationData(BaseNotificationData):
    notification_payload: typing.Optional[AnalysisUpdateNotificationPayload] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
