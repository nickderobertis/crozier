

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ldk_chain_sync_transaction_sync_config import LdkChainSyncTransactionSyncConfig


class LdkChainSyncTransactionSync(UniversalBaseModel):
    config: LdkChainSyncTransactionSyncConfig

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
