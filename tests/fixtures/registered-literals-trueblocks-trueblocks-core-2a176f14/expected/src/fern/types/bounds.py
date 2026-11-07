

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Bounds(UniversalBaseModel):
    """
    show first block and last block an address appears in along with timestamps and dates
    """

    count: typing.Optional[int] = pydantic.Field(default=None)
    """
    the number of appearances for this address
    """

    first_app: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="firstApp"),
        pydantic.Field(
            alias="firstApp", description="the block number and transaction id of the first appearance of this address"
        ),
    ] = None
    """
    the block number and transaction id of the first appearance of this address
    """

    first_ts: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="firstTs"),
        pydantic.Field(alias="firstTs", description="the timestamp of the first appearance of this address"),
    ] = None
    """
    the timestamp of the first appearance of this address
    """

    first_date: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="firstDate"),
        pydantic.Field(alias="firstDate", description="the first appearance timestamp as a date (calculated)"),
    ] = None
    """
    the first appearance timestamp as a date (calculated)
    """

    latest_app: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="latestApp"),
        pydantic.Field(
            alias="latestApp",
            description="the block number and transaction id of the latest appearance of this address",
        ),
    ] = None
    """
    the block number and transaction id of the latest appearance of this address
    """

    latest_ts: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="latestTs"),
        pydantic.Field(alias="latestTs", description="the timestamp of the latest appearance of this address"),
    ] = None
    """
    the timestamp of the latest appearance of this address
    """

    latest_date: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="latestDate"),
        pydantic.Field(alias="latestDate", description="the latest appearance timestamp as a date (calculated)"),
    ] = None
    """
    the latest appearance timestamp as a date (calculated)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
