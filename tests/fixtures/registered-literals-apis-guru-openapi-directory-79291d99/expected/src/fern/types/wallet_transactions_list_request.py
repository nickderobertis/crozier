

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .api_client_id import ApiClientId
from .api_secret import ApiSecret
from .wallet_transaction_list_request_options import WalletTransactionListRequestOptions


class WalletTransactionsListRequest(UniversalBaseModel):
    """
    WalletTransactionListRequest defines the request schema for `/wallet/transaction/list`
    """

    client_id: typing.Optional[ApiClientId] = None
    count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of transactions to fetch
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    A base64 value representing the latest transaction that has already been requested. Set this to `next_cursor` received from the previous `/wallet/transaction/list` request. If provided, the response will only contain transactions created before that transaction. If omitted, the response will contain transactions starting from the most recent, and in descending order by the `created_at` time.
    """

    options: typing.Optional[WalletTransactionListRequestOptions] = None
    secret: typing.Optional[ApiSecret] = None
    wallet_id: str = pydantic.Field()
    """
    The ID of the e-wallet to fetch transactions from
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
