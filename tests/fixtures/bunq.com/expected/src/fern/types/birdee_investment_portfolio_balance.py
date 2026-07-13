

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amount import Amount


class BirdeeInvestmentPortfolioBalance(UniversalBaseModel):
    amount_available: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The current valuation of the portfolio, minus any amount pending withdrawal.
    """

    amount_deposit_pending: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The amount that's sent to Birdee, but pending investment on the portfolio.
    """

    amount_deposit_total: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The total amount deposited.
    """

    amount_fee_total: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The total fee amount.
    """

    amount_profit: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The difference between the netto deposited amount and the current valuation.
    """

    amount_withdrawal_pending: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The amount that's sent to Birdee, but pending withdrawal.
    """

    amount_withdrawal_total: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The total amount withdrawn.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
