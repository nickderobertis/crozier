

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.transaction_history import TransactionHistory
from ...types.transactions_history_link import TransactionsHistoryLink


class ListTransactionsV21Response(UniversalBaseModel):
    items: typing.Optional[typing.List[TransactionHistory]] = pydantic.Field(default=None)
    """
    Transactions in the current result page.
    """

    links: typing.Optional[typing.List[TransactionsHistoryLink]] = pydantic.Field(default=None)
    """
    Pagination links for navigating the transaction history.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
