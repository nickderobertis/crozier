

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .distribution_breakdown import DistributionBreakdown
from .pay_period_details_pay_frequency import PayPeriodDetailsPayFrequency


class PayPeriodDetails(UniversalBaseModel):
    """
    Details about the pay period.
    """

    check_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    The amount of the paycheck.
    """

    distribution_breakdown: typing.Optional[typing.List[DistributionBreakdown]] = None
    end_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The pay period end date, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format: "yyyy-mm-dd".
    """

    gross_earnings: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total earnings before tax/deductions.
    """

    pay_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date on which the paystub was issued, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ("yyyy-mm-dd").
    """

    pay_day: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date on which the paystub was issued, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ("yyyy-mm-dd").
    """

    pay_frequency: typing.Optional[PayPeriodDetailsPayFrequency] = pydantic.Field(default=None)
    """
    The frequency at which an individual is paid.
    """

    start_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The pay period start date, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format: "yyyy-mm-dd".
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
