

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .notification_base import NotificationBase
from .policy_eval_notification_data import PolicyEvalNotificationData


class PolicyEvalNotification(NotificationBase):
    data: typing.Optional[PolicyEvalNotificationData] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
