

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .id import Id
from .profit_and_loss_expenses import ProfitAndLossExpenses
from .profit_and_loss_gross_profit import ProfitAndLossGrossProfit
from .profit_and_loss_income import ProfitAndLossIncome
from .profit_and_loss_net_income import ProfitAndLossNetIncome
from .profit_and_loss_net_operating_income import ProfitAndLossNetOperatingIncome


class ProfitAndLoss(UniversalBaseModel):
    currency: str
    customer_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Customer id
    """

    end_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The start date of the report
    """

    expenses: ProfitAndLossExpenses
    gross_profit: typing.Optional[ProfitAndLossGrossProfit] = None
    id: typing.Optional[Id] = None
    income: ProfitAndLossIncome
    net_income: typing.Optional[ProfitAndLossNetIncome] = None
    net_operating_income: typing.Optional[ProfitAndLossNetOperatingIncome] = None
    report_name: str = pydantic.Field()
    """
    The name of the report
    """

    start_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The start date of the report
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(ProfitAndLoss)
