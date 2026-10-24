

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ldk_chain_sync_block_sync_config import LdkChainSyncBlockSyncConfig


class LdkChainSyncBlockSync(UniversalBaseModel):
    config: LdkChainSyncBlockSyncConfig

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
