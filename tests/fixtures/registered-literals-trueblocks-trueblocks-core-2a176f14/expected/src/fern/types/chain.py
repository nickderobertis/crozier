

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Chain(UniversalBaseModel):
    """
    a configuration item carrying information about a single chain
    """

    chain: typing.Optional[str] = pydantic.Field(default=None)
    """
    the common name of the chain
    """

    chain_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="chainId"),
        pydantic.Field(alias="chainId", description="the chain id as reported by the RPC"),
    ] = None
    """
    the chain id as reported by the RPC
    """

    symbol: typing.Optional[str] = pydantic.Field(default=None)
    """
    the symbol of the base currency on the chain
    """

    rpc_provider: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="rpcProvider"),
        pydantic.Field(alias="rpcProvider", description="a valid RPC provider for the chain"),
    ] = None
    """
    a valid RPC provider for the chain
    """

    remote_explorer: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="remoteExplorer"),
        pydantic.Field(alias="remoteExplorer", description="a remote explorer for the chain such as Etherscan"),
    ] = None
    """
    a remote explorer for the chain such as Etherscan
    """

    local_explorer: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="localExplorer"),
        pydantic.Field(
            alias="localExplorer", description="the local explorer for the chain (typically TrueBlocks Explorer)"
        ),
    ] = None
    """
    the local explorer for the chain (typically TrueBlocks Explorer)
    """

    ipfs_gateway: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ipfsGateway"),
        pydantic.Field(alias="ipfsGateway", description="an IPFS gateway for pinning the index if enabled"),
    ] = None
    """
    an IPFS gateway for pinning the index if enabled
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
