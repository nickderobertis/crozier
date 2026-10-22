

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LdkChainSyncBlockSyncConfig(UniversalBaseModel):
    bitcoind_rpc_username: str
    bitcoind_rpc_password: str
    bitcoind_rpc_host: str
    bitcoind_rpc_port: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
