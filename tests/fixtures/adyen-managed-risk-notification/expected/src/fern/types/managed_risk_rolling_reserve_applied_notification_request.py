

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .managed_risk_rolling_reserve_applied_notification_request_environment import (
    ManagedRiskRollingReserveAppliedNotificationRequestEnvironment,
)
from .managed_risk_rolling_reserve_applied_notification_request_type import (
    ManagedRiskRollingReserveAppliedNotificationRequestType,
)
from .rolling_reserve_notification_resource import RollingReserveNotificationResource


class ManagedRiskRollingReserveAppliedNotificationRequest(UniversalBaseModel):
    data: RollingReserveNotificationResource = pydantic.Field()
    """
    Contains event details.
    """

    environment: ManagedRiskRollingReserveAppliedNotificationRequestEnvironment = pydantic.Field()
    """
    The environment from which the webhook originated.
    
    Possible values: **test**, **live**.
    """

    timestamp: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the event was queued.
    """

    type: ManagedRiskRollingReserveAppliedNotificationRequestType = pydantic.Field()
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
