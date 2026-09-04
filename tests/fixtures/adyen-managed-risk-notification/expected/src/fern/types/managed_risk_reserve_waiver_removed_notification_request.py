

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .managed_risk_reserve_waiver_removed_notification_request_environment import (
    ManagedRiskReserveWaiverRemovedNotificationRequestEnvironment,
)
from .managed_risk_reserve_waiver_removed_notification_request_type import (
    ManagedRiskReserveWaiverRemovedNotificationRequestType,
)
from .reserve_waiver_removed_notification_resource import ReserveWaiverRemovedNotificationResource


class ManagedRiskReserveWaiverRemovedNotificationRequest(UniversalBaseModel):
    data: ReserveWaiverRemovedNotificationResource = pydantic.Field()
    """
    Contains event details.
    """

    environment: ManagedRiskReserveWaiverRemovedNotificationRequestEnvironment = pydantic.Field()
    """
    The environment from which the webhook originated.
    
    Possible values: **test**, **live**.
    """

    timestamp: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the event was queued.
    """

    type: ManagedRiskReserveWaiverRemovedNotificationRequestType = pydantic.Field()
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
