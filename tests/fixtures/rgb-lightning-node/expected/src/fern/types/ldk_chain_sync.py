

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ldk_chain_sync_block_sync_config import LdkChainSyncBlockSyncConfig
from .ldk_chain_sync_transaction_sync_config import LdkChainSyncTransactionSyncConfig


class LdkChainSync_BlockSync(UniversalBaseModel):
    mode: typing.Literal["BlockSync"] = "BlockSync"
    config: LdkChainSyncBlockSyncConfig

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class LdkChainSync_TransactionSync(UniversalBaseModel):
    mode: typing.Literal["TransactionSync"] = "TransactionSync"
    config: LdkChainSyncTransactionSyncConfig

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


LdkChainSync = typing_extensions.Annotated[
    typing.Union[LdkChainSync_BlockSync, LdkChainSync_TransactionSync], pydantic.Field(discriminator="mode")
]
