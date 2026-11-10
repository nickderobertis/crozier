

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit1099 import Credit1099
from .credit_pay_stub import CreditPayStub
from .credit_w2 import CreditW2


class PayrollIncomeObject(UniversalBaseModel):
    """
    An object representing payroll data.
    """

    account_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the payroll provider account.
    """

    form1099s: typing.List[Credit1099] = pydantic.Field()
    """
    Array of tax form 1099s.
    """

    pay_stubs: typing.List[CreditPayStub] = pydantic.Field()
    """
    Array of pay stubs for the user.
    """

    w2s: typing.List[CreditW2] = pydantic.Field()
    """
    Array of tax form W-2s.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
