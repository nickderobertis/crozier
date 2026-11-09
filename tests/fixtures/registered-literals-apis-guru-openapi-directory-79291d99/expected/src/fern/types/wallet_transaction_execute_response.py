

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId
from .wallet_transaction_status import WalletTransactionStatus


class WalletTransactionExecuteResponse(UniversalBaseModel):
    """
    WalletTransactionExecuteResponse defines the response schema for `/wallet/transaction/execute`
    """

    request_id: RequestId
    status: WalletTransactionStatus
    transaction_id: str = pydantic.Field()
    """
    A unique ID identifying the transaction
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
