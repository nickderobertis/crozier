

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cache_item import CacheItem
from .chain import Chain


class Status(UniversalBaseModel):
    """
    status-related data about the TrueBlocks system including the server and local binary caches
    """

    cache_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="cachePath"),
        pydantic.Field(alias="cachePath", description="the path to the local binary caches"),
    ] = None
    """
    the path to the local binary caches
    """

    caches: typing.Optional[typing.List[CacheItem]] = pydantic.Field(default=None)
    """
    a collection of information concerning the binary caches
    """

    chain: typing.Optional[str] = pydantic.Field(default=None)
    """
    the current chain
    """

    chain_config: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="chainConfig"),
        pydantic.Field(alias="chainConfig", description="the path to the chain configuration folder"),
    ] = None
    """
    the path to the chain configuration folder
    """

    client_version: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="clientVersion"),
        pydantic.Field(alias="clientVersion", description="the version string as reported by the rpcProvider"),
    ] = None
    """
    the version string as reported by the rpcProvider
    """

    chain_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="chainId"),
        pydantic.Field(alias="chainId", description="the path to config files"),
    ] = None
    """
    the path to config files
    """

    has_es_key: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasEsKey"),
        pydantic.Field(alias="hasEsKey", description="`true` if an Etherscan key is present"),
    ] = None
    """
    `true` if an Etherscan key is present
    """

    has_pin_key: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasPinKey"),
        pydantic.Field(alias="hasPinKey", description="`true` if a Pinata API key is present"),
    ] = None
    """
    `true` if a Pinata API key is present
    """

    index_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="indexPath"),
        pydantic.Field(alias="indexPath", description="the path to the local binary indexes"),
    ] = None
    """
    the path to the local binary indexes
    """

    is_api: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isApi"),
        pydantic.Field(alias="isApi", description="`true` if the server is running in API mode"),
    ] = None
    """
    `true` if the server is running in API mode
    """

    is_archive: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isArchive"),
        pydantic.Field(alias="isArchive", description="`true` if the rpcProvider is an archive node"),
    ] = None
    """
    `true` if the rpcProvider is an archive node
    """

    is_testing: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isTesting"),
        pydantic.Field(alias="isTesting", description="`true` if the server is running in test mode"),
    ] = None
    """
    `true` if the server is running in test mode
    """

    is_tracing: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isTracing"),
        pydantic.Field(alias="isTracing", description="`true` if the rpcProvider provides Parity traces"),
    ] = None
    """
    `true` if the rpcProvider provides Parity traces
    """

    is_scraping: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isScraping"),
        pydantic.Field(alias="isScraping", description="`true` if the scraper is running"),
    ] = None
    """
    `true` if the scraper is running
    """

    network_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="networkId"),
        pydantic.Field(alias="networkId", description="the network id as reported by the rpcProvider"),
    ] = None
    """
    the network id as reported by the rpcProvider
    """

    progress: typing.Optional[str] = pydantic.Field(default=None)
    """
    the progress string of the system
    """

    root_config: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="rootConfig"),
        pydantic.Field(alias="rootConfig", description="the path to the root configuration folder"),
    ] = None
    """
    the path to the root configuration folder
    """

    rpc_provider: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="rpcProvider"),
        pydantic.Field(alias="rpcProvider", description="the current rpcProvider"),
    ] = None
    """
    the current rpcProvider
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    the TrueBlocks version string
    """

    chains: typing.Optional[typing.List[Chain]] = pydantic.Field(default=None)
    """
    a list of available chains in the config file
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
