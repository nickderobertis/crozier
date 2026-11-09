

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .request_id import RequestId
from .wallet import Wallet


class WalletGetResponse(Wallet):
    """
    WalletGetResponse defines the response schema for `/wallet/get`
    """

    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
