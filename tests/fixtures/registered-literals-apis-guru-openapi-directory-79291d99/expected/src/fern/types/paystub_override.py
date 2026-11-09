

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .income_breakdown import IncomeBreakdown
from .pay_period_details import PayPeriodDetails
from .paystub_override_employee import PaystubOverrideEmployee
from .paystub_override_employer import PaystubOverrideEmployer


class PaystubOverride(UniversalBaseModel):
    """
    An object representing data from a paystub.
    """

    employee: typing.Optional[PaystubOverrideEmployee] = None
    employer: typing.Optional[PaystubOverrideEmployer] = None
    income_breakdown: typing.Optional[typing.List[IncomeBreakdown]] = None
    pay_period_details: typing.Optional[PayPeriodDetails] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
