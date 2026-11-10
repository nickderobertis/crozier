

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId
from .wallet import Wallet


class WalletListResponse(UniversalBaseModel):
    """
    WalletListResponse defines the response schema for `/wallet/list`
    """

    next_cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    Cursor used for fetching e-wallets created before the latest e-wallet provided in this response
    """

    request_id: RequestId
    wallets: typing.List[Wallet] = pydantic.Field()
    """
    An array of e-wallets
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
