

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transfer_schedule_interval_count import TransferScheduleIntervalCount
from .transfer_schedule_interval_unit import TransferScheduleIntervalUnit


class TransferRecurringSchedule(UniversalBaseModel):
    """
    The schedule that the recurring transfer will be executed on.
    """

    end_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    A date in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). The recurring transfer will end on the last `interval_execution_day` on or before the `end_date`.
    If the `interval_execution_day` between the start date and the end date (inclusive) is also the same day that `/transfer/recurring/create` was called, the bank *may* make a payment on that day, but it is not guaranteed to do so.
    """

    interval_count: TransferScheduleIntervalCount
    interval_execution_day: int = pydantic.Field()
    """
    The day of the interval on which to schedule the transfer.
    
    If the `interval_unit` is `week`, `interval_execution_day` should be an integer from 1 (Monday) to 5 (Friday).
    
    If the `interval_unit` is `month`, `interval_execution_day` should be an integer indicating which day of the month to make the transfer on. Integers from 1 to 28 can be used to make a transfer on that day of the month. Negative integers from -1 to -5 can be used to make a transfer relative to the end of the month. To make a transfer on the last day of the month, use -1; to make the transfer on the second-to-last day, use -2, and so on.
    
    The transfer will be originated on next available banking day if the designated day is a non banking day.
    """

    interval_unit: TransferScheduleIntervalUnit
    start_date: dt.date = pydantic.Field()
    """
    A date in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). The recurring transfer will begin on the first `interval_execution_day` on or after the `start_date`.
    
    If the first `interval_execution_day` on or after the start date is also the same day that `/transfer/recurring/create` was called, the bank *may* make the first payment on that day, but it is not guaranteed to do so.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
