

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chunk_record import ChunkRecord


class Manifest(UniversalBaseModel):
    """
    a JSON object containing records for each bloom filter and index chunk in the Unchained Index
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    the version string hashed into the chunk data
    """

    chain: typing.Optional[str] = pydantic.Field(default=None)
    """
    the chain to which this manifest belongs
    """

    specification: typing.Optional[str] = pydantic.Field(default=None)
    """
    IPFS cid of the specification
    """

    chunks: typing.Optional[typing.List[ChunkRecord]] = pydantic.Field(default=None)
    """
    a list of the IPFS hashes of all of the chunks in the unchained index
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
