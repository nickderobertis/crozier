

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_base import AccountBase
from .investment_transaction import InvestmentTransaction
from .item import Item
from .request_id import RequestId
from .security import Security


class InvestmentsTransactionsGetResponse(UniversalBaseModel):
    """
    InvestmentsTransactionsGetResponse defines the response schema for `/investments/transactions/get`
    """

    accounts: typing.List[AccountBase] = pydantic.Field()
    """
    The accounts for which transaction history is being fetched.
    """

    investment_transactions: typing.List[InvestmentTransaction] = pydantic.Field()
    """
    The transactions being fetched
    """

    item: Item
    request_id: RequestId
    securities: typing.List[Security] = pydantic.Field()
    """
    All securities for which there is a corresponding transaction being fetched.
    """

    total_investment_transactions: int = pydantic.Field()
    """
    The total number of transactions available within the date range specified. If `total_investment_transactions` is larger than the size of the `transactions` array, more transactions are available and can be fetched via manipulating the `offset` parameter.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
