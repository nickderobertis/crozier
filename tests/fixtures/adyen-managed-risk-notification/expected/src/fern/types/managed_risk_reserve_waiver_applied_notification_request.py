

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .managed_risk_reserve_waiver_applied_notification_request_environment import (
    ManagedRiskReserveWaiverAppliedNotificationRequestEnvironment,
)
from .managed_risk_reserve_waiver_applied_notification_request_type import (
    ManagedRiskReserveWaiverAppliedNotificationRequestType,
)
from .reserve_waiver_applied_notification_resource import ReserveWaiverAppliedNotificationResource


class ManagedRiskReserveWaiverAppliedNotificationRequest(UniversalBaseModel):
    data: ReserveWaiverAppliedNotificationResource = pydantic.Field()
    """
    Contains event details.
    """

    environment: ManagedRiskReserveWaiverAppliedNotificationRequestEnvironment = pydantic.Field()
    """
    The environment from which the webhook originated.
    
    Possible values: **test**, **live**.
    """

    timestamp: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the event was queued.
    """

    type: ManagedRiskReserveWaiverAppliedNotificationRequestType = pydantic.Field()
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
