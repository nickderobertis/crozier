

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_base import AccountBase
from .item import Item
from .request_id import RequestId
from .transaction import Transaction


class TransactionsGetResponse(UniversalBaseModel):
    """
    TransactionsGetResponse defines the response schema for `/transactions/get`
    """

    accounts: typing.List[AccountBase] = pydantic.Field()
    """
    An array containing the `accounts` associated with the Item for which transactions are being returned. Each transaction can be mapped to its corresponding account via the `account_id` field.
    """

    item: Item
    request_id: RequestId
    total_transactions: int = pydantic.Field()
    """
    The total number of transactions available within the date range specified. If `total_transactions` is larger than the size of the `transactions` array, more transactions are available and can be fetched via manipulating the `offset` parameter.
    """

    transactions: typing.List[Transaction] = pydantic.Field()
    """
    An array containing transactions from the account. Transactions are returned in reverse chronological order, with the most recent at the beginning of the array. The maximum number of transactions returned is determined by the `count` parameter.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
