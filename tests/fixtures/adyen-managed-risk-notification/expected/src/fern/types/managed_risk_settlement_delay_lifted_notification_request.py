

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .managed_risk_settlement_delay_lifted_notification_request_environment import (
    ManagedRiskSettlementDelayLiftedNotificationRequestEnvironment,
)
from .managed_risk_settlement_delay_lifted_notification_request_type import (
    ManagedRiskSettlementDelayLiftedNotificationRequestType,
)
from .settlement_delay_lifted_notification_resource import SettlementDelayLiftedNotificationResource


class ManagedRiskSettlementDelayLiftedNotificationRequest(UniversalBaseModel):
    data: SettlementDelayLiftedNotificationResource = pydantic.Field()
    """
    Contains event details.
    """

    environment: ManagedRiskSettlementDelayLiftedNotificationRequestEnvironment = pydantic.Field()
    """
    The environment from which the webhook originated.
    
    Possible values: **test**, **live**.
    """

    timestamp: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the event was queued.
    """

    type: ManagedRiskSettlementDelayLiftedNotificationRequestType = pydantic.Field()
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
