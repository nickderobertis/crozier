

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RangeDates(UniversalBaseModel):
    """
    shows first and last timestamps and dates for a given block range
    """

    first_ts: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="firstTs"),
        pydantic.Field(alias="firstTs", description="the timestamp of the first block in this range"),
    ] = None
    """
    the timestamp of the first block in this range
    """

    first_date: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="firstDate"),
        pydantic.Field(alias="firstDate", description="the first timestamp as a date"),
    ] = None
    """
    the first timestamp as a date
    """

    last_ts: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="lastTs"),
        pydantic.Field(alias="lastTs", description="the timestamp of the most recent block in this range"),
    ] = None
    """
    the timestamp of the most recent block in this range
    """

    last_date: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lastDate"),
        pydantic.Field(alias="lastDate", description="the last timestamp as a date"),
    ] = None
    """
    the last timestamp as a date
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
