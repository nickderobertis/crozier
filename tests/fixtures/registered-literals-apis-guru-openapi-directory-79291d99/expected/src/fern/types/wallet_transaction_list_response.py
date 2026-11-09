

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId
from .wallet_transaction import WalletTransaction


class WalletTransactionListResponse(UniversalBaseModel):
    """
    WalletTransactionListResponse defines the response schema for `/wallet/transaction/list`
    """

    next_cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    Cursor used for fetching transactions created before the latest transaction provided in this response
    """

    request_id: RequestId
    transactions: typing.List[WalletTransaction] = pydantic.Field()
    """
    An array of transactions of an e-wallet, associated with the given `wallet_id`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
