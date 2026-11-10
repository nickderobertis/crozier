

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_filter import CreditFilter
from .depository_filter import DepositoryFilter
from .investment_filter import InvestmentFilter
from .loan_filter import LoanFilter


class AccountFiltersResponse(UniversalBaseModel):
    """
    The `account_filters` specified in the original call to `/link/token/create`.
    """

    credit: typing.Optional[CreditFilter] = None
    depository: typing.Optional[DepositoryFilter] = None
    investment: typing.Optional[InvestmentFilter] = None
    loan: typing.Optional[LoanFilter] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
