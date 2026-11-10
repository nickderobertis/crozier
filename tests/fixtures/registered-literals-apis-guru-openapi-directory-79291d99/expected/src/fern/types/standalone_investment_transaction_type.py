

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .standalone_investment_transaction_buy_type import StandaloneInvestmentTransactionBuyType
from .standalone_investment_transaction_cash_type import StandaloneInvestmentTransactionCashType
from .standalone_investment_transaction_fee_type import StandaloneInvestmentTransactionFeeType
from .standalone_investment_transaction_sell_type import StandaloneInvestmentTransactionSellType
from .standalone_investment_transaction_transfer_type import StandaloneInvestmentTransactionTransferType


class StandaloneInvestmentTransactionType(UniversalBaseModel):
    """
    Valid values for investment transaction types and subtypes. Note that transactions representing inflow of cash will appear as negative amounts, outflow of cash will appear as positive amounts.
    """

    buy: StandaloneInvestmentTransactionBuyType
    cancel: str = pydantic.Field()
    """
    A cancellation of a pending transaction
    """

    cash: StandaloneInvestmentTransactionCashType
    fee: StandaloneInvestmentTransactionFeeType
    sell: StandaloneInvestmentTransactionSellType
    transfer: StandaloneInvestmentTransactionTransferType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
