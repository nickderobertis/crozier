

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .birdee_investment_portfolio_balance import BirdeeInvestmentPortfolioBalance
from .birdee_investment_portfolio_goal import BirdeeInvestmentPortfolioGoal
from .birdee_portfolio_allocation import BirdeePortfolioAllocation


class BirdeeInvestmentPortfolio(UniversalBaseModel):
    allocations: typing.Optional[typing.List[BirdeePortfolioAllocation]] = pydantic.Field(default=None)
    """
    The allocations of the investment portfolio.
    """

    balance: typing.Optional[BirdeeInvestmentPortfolioBalance] = pydantic.Field(default=None)
    """
    The investment portfolio balance.
    """

    goal: typing.Optional[BirdeeInvestmentPortfolioGoal] = pydantic.Field(default=None)
    """
    The investment goal.
    """

    investment_theme: typing.Optional[str] = pydantic.Field(default=None)
    """
    The investment theme.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name associated with the investment portfolio.
    """

    number_of_strategy_change_annual_maximum: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum number of strategy changes in a year.
    """

    number_of_strategy_change_annual_used: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum number of strategy changes used.
    """

    risk_profile_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of risk profile associated with the portfolio.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Status of the portfolio.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
