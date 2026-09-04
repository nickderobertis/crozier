

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .managed_risk_balance_block_released_notification_request_environment import (
    ManagedRiskBalanceBlockReleasedNotificationRequestEnvironment,
)
from .managed_risk_balance_block_released_notification_request_type import (
    ManagedRiskBalanceBlockReleasedNotificationRequestType,
)
from .release_blocked_balance_notification_data import ReleaseBlockedBalanceNotificationData


class ManagedRiskBalanceBlockReleasedNotificationRequest(UniversalBaseModel):
    data: ReleaseBlockedBalanceNotificationData = pydantic.Field()
    """
    Contains event details.
    """

    environment: ManagedRiskBalanceBlockReleasedNotificationRequestEnvironment = pydantic.Field()
    """
    The environment from which the webhook originated.
    
    Possible values: **test**, **live**.
    """

    timestamp: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the event was queued.
    """

    type: ManagedRiskBalanceBlockReleasedNotificationRequestType = pydantic.Field()
    """
    Type of webhook.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
