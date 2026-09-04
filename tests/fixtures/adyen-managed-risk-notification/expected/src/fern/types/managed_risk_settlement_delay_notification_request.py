

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .managed_risk_settlement_delay_notification_request_environment import (
    ManagedRiskSettlementDelayNotificationRequestEnvironment,
)
from .managed_risk_settlement_delay_notification_request_type import ManagedRiskSettlementDelayNotificationRequestType
from .settlement_delay_notification_resource import SettlementDelayNotificationResource


class ManagedRiskSettlementDelayNotificationRequest(UniversalBaseModel):
    data: SettlementDelayNotificationResource = pydantic.Field()
    """
    Contains event details.
    """

    environment: ManagedRiskSettlementDelayNotificationRequestEnvironment = pydantic.Field()
    """
    The environment from which the webhook originated.
    
    Possible values: **test**, **live**.
    """

    timestamp: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the event was queued.
    """

    type: ManagedRiskSettlementDelayNotificationRequestType = pydantic.Field()
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
