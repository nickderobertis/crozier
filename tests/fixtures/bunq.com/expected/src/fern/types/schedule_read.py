

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .schedule_anchor_object import ScheduleAnchorObject


class ScheduleRead(UniversalBaseModel):
    object: typing.Optional[ScheduleAnchorObject] = pydantic.Field(default=None)
    """
    The scheduled object. (Payment, PaymentBatch)
    """

    recurrence_size: typing.Optional[int] = pydantic.Field(default=None)
    """
    The schedule recurrence size. For example size 4 and unit WEEKLY means the recurrence is every 4 weeks.
    """

    recurrence_unit: typing.Optional[str] = pydantic.Field(default=None)
    """
    The schedule recurrence unit, options: ONCE, HOURLY, DAILY, WEEKLY, MONTHLY, YEARLY
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The schedule status, options: ACTIVE, FINISHED, CANCELLED.
    """

    time_end: typing.Optional[str] = pydantic.Field(default=None)
    """
    The schedule end time (UTC).
    """

    time_start: typing.Optional[str] = pydantic.Field(default=None)
    """
    The schedule start time (UTC).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(ScheduleRead)
