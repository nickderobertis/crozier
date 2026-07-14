

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_notification_data import BaseNotificationData
from .vuln_update_notification_payload import VulnUpdateNotificationPayload


class VulnUpdateNotificationData(BaseNotificationData):
    notification_payload: typing.Optional[VulnUpdateNotificationPayload] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
