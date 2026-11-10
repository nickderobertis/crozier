

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .paystub_pay_frequency import PaystubPayFrequency


class PaystubDetails(UniversalBaseModel):
    """
    An object representing details that can be found on the paystub.
    """

    pay_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Pay date on the paystub in the 'YYYY-MM-DD' format.
    """

    pay_frequency: typing.Optional[PaystubPayFrequency] = None
    pay_period_end_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Ending date of the pay period on the paystub in the 'YYYY-MM-DD' format.
    """

    pay_period_start_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Beginning date of the pay period on the paystub in the 'YYYY-MM-DD' format.
    """

    paystub_provider: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the payroll provider that generated the paystub, e.g. ADP
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
