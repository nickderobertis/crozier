

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PayrollIncomeRateOfPay(UniversalBaseModel):
    """
    An object representing the rate at which an individual is paid.
    """

    pay_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    The amount at which an employee is paid.
    """

    pay_rate: typing.Optional[str] = pydantic.Field(default=None)
    """
    The rate at which an employee is paid.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
