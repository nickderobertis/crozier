

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .deductions import Deductions
from .earnings import Earnings
from .employee import Employee
from .employment_details import EmploymentDetails
from .income_breakdown import IncomeBreakdown
from .net_pay import NetPay
from .pay_period_details import PayPeriodDetails
from .paystub_details import PaystubDetails
from .paystub_employer import PaystubEmployer
from .paystub_ytd_details import PaystubYtdDetails


class Paystub(UniversalBaseModel):
    """
    An object representing data extracted from the end user's paystub.
    """

    deductions: Deductions
    doc_id: str = pydantic.Field()
    """
    An identifier of the document referenced by the document metadata.
    """

    earnings: Earnings
    employee: Employee
    employer: PaystubEmployer
    employment_details: typing.Optional[EmploymentDetails] = None
    income_breakdown: typing.Optional[typing.List[IncomeBreakdown]] = None
    net_pay: NetPay
    pay_period_details: PayPeriodDetails
    paystub_details: typing.Optional[PaystubDetails] = None
    ytd_earnings: typing.Optional[PaystubYtdDetails] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
