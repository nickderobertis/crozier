

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .payroll_income_rate_of_pay import PayrollIncomeRateOfPay


class PayrollIncomeAccountData(UniversalBaseModel):
    """
    An object containing account level data.
    """

    account_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the payroll provider account.
    """

    pay_frequency: typing.Optional[str] = pydantic.Field(default=None)
    """
    The frequency at which an individual is paid.
    """

    rate_of_pay: PayrollIncomeRateOfPay

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
