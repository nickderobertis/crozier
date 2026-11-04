

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ChunkIndex(UniversalBaseModel):
    """
    internal-use only data model detailing a single index chunk file
    """

    range: typing.Optional[str] = pydantic.Field(default=None)
    """
    the block range (inclusive) covered by this chunk
    """

    magic: typing.Optional[str] = pydantic.Field(default=None)
    """
    an internal use only magic number to indicate file format
    """

    hash: typing.Optional[str] = pydantic.Field(default=None)
    """
    the hash of the specification under which this chunk was generated
    """

    n_addresses: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="nAddresses"),
        pydantic.Field(alias="nAddresses", description="the number of addresses in this chunk"),
    ] = None
    """
    the number of addresses in this chunk
    """

    n_appearances: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="nAppearances"),
        pydantic.Field(alias="nAppearances", description="the number of appearances in this chunk"),
    ] = None
    """
    the number of appearances in this chunk
    """

    file_size: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="fileSize"),
        pydantic.Field(alias="fileSize", description="the file size on disc in bytes of this bloom file"),
    ] = None
    """
    the file size on disc in bytes of this bloom file
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
