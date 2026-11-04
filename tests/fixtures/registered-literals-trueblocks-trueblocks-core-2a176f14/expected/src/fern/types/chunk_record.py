

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ChunkRecord(UniversalBaseModel):
    """
    a single record in the manifest detailing the IPFS hases and file sizes for each bloom filter and index chunk
    """

    range: typing.Optional[str] = pydantic.Field(default=None)
    """
    the block range (inclusive) covered by this chunk
    """

    bloom_hash: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="bloomHash"),
        pydantic.Field(alias="bloomHash", description="the IPFS hash of the bloom filter at that range"),
    ] = None
    """
    the IPFS hash of the bloom filter at that range
    """

    index_hash: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="indexHash"),
        pydantic.Field(alias="indexHash", description="the IPFS hash of the index chunk at that range"),
    ] = None
    """
    the IPFS hash of the index chunk at that range
    """

    bloom_size: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="bloomSize"),
        pydantic.Field(alias="bloomSize", description="the size of the bloom filter in bytes"),
    ] = None
    """
    the size of the bloom filter in bytes
    """

    index_size: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="indexSize"),
        pydantic.Field(alias="indexSize", description="the size of the index portion in bytes"),
    ] = None
    """
    the size of the index portion in bytes
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
