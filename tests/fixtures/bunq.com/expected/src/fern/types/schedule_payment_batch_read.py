

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .schedule import Schedule
from .schedule_payment_entry import SchedulePaymentEntry


class SchedulePaymentBatchRead(UniversalBaseModel):
    payments: typing.Optional[typing.List[SchedulePaymentEntry]] = pydantic.Field(default=None)
    """
    The payment details.
    """

    schedule: typing.Optional[Schedule] = pydantic.Field(default=None)
    """
    The schedule details.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(SchedulePaymentBatchRead)
