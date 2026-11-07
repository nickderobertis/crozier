

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ChunkPin(UniversalBaseModel):
    """
    a JSON object containing the results of pinning the Unchained Index
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    the version string hashed into the chunk data
    """

    chain: typing.Optional[str] = pydantic.Field(default=None)
    """
    the chain to which this manifest belongs
    """

    timestamp_hash: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="timestampHash"),
        pydantic.Field(alias="timestampHash", description="IPFS cid of file containing timestamps"),
    ] = None
    """
    IPFS cid of file containing timestamps
    """

    spec_hash: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="specHash"),
        pydantic.Field(alias="specHash", description="IPFS cid of the specification"),
    ] = None
    """
    IPFS cid of the specification
    """

    manifest_hash: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="manifestHash"),
        pydantic.Field(alias="manifestHash", description="IPFS cid of file containing CIDs for the various chunks"),
    ] = None
    """
    IPFS cid of file containing CIDs for the various chunks
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
