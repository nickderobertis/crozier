

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ChunkStats(UniversalBaseModel):
    """
    summary statistics about an Unchained Index bloom filter and index chunk
    """

    range: typing.Optional[str] = pydantic.Field(default=None)
    """
    the block range (inclusive) covered by this chunk
    """

    n_addrs: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="nAddrs"),
        pydantic.Field(alias="nAddrs", description="the number of addresses in the chunk"),
    ] = None
    """
    the number of addresses in the chunk
    """

    n_apps: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="nApps"),
        pydantic.Field(alias="nApps", description="the number of appearances in the chunk"),
    ] = None
    """
    the number of appearances in the chunk
    """

    n_blocks: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="nBlocks"),
        pydantic.Field(alias="nBlocks", description="the number of blocks in the chunk"),
    ] = None
    """
    the number of blocks in the chunk
    """

    n_blooms: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="nBlooms"),
        pydantic.Field(alias="nBlooms", description="the number of bloom filters in the chunk's bloom"),
    ] = None
    """
    the number of bloom filters in the chunk's bloom
    """

    rec_wid: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="recWid"),
        pydantic.Field(alias="recWid", description="the record width of a single bloom filter"),
    ] = None
    """
    the record width of a single bloom filter
    """

    bloom_sz: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="bloomSz"),
        pydantic.Field(alias="bloomSz", description="the size of the bloom filters on disc in bytes"),
    ] = None
    """
    the size of the bloom filters on disc in bytes
    """

    chunk_sz: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="chunkSz"),
        pydantic.Field(alias="chunkSz", description="the size of the chunks on disc in bytes"),
    ] = None
    """
    the size of the chunks on disc in bytes
    """

    addrs_per_block: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="addrsPerBlock"),
        pydantic.Field(alias="addrsPerBlock", description="the average number of addresses per block"),
    ] = None
    """
    the average number of addresses per block
    """

    apps_per_block: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="appsPerBlock"),
        pydantic.Field(alias="appsPerBlock", description="the average number of appearances per block"),
    ] = None
    """
    the average number of appearances per block
    """

    apps_per_addr: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="appsPerAddr"),
        pydantic.Field(alias="appsPerAddr", description="the average number of appearances per address"),
    ] = None
    """
    the average number of appearances per address
    """

    ratio: typing.Optional[float] = pydantic.Field(default=None)
    """
    the ratio of appearances to addresses
    """

    range_dates: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="rangeDates"),
        pydantic.Field(
            alias="rangeDates", description="if verbose, the block and timestamp bounds of the chunk (may be null)"
        ),
    ] = None
    """
    if verbose, the block and timestamp bounds of the chunk (may be null)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
