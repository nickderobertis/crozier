

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ChunkAddress(UniversalBaseModel):
    """
    internal-use only data model detailing a single address record in the address table of an index chunk
    """

    address: typing.Optional[str] = pydantic.Field(default=None)
    """
    the address in this record
    """

    range: typing.Optional[str] = pydantic.Field(default=None)
    """
    the block range of the chunk from which this address record was taken
    """

    offset: typing.Optional[int] = pydantic.Field(default=None)
    """
    the offset into the appearance table of the first record for this address
    """

    count: typing.Optional[int] = pydantic.Field(default=None)
    """
    the number of records in teh appearance table for this address
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
