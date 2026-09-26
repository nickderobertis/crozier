

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Interval(UniversalBaseModel):
    """
    Represents a time interval, encoded as a Timestamp start (inclusive) and a Timestamp end (exclusive).The start must be less than or equal to the end. When the start equals the end, the interval is empty (matches no time). When both start and end are unspecified, the interval matches any time.
    """

    end_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="endTime"),
        pydantic.Field(
            alias="endTime",
            description="Optional. Exclusive end of the interval.If specified, a Timestamp matching this interval will have to be before the end.",
        ),
    ] = None
    """
    Optional. Exclusive end of the interval.If specified, a Timestamp matching this interval will have to be before the end.
    """

    start_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="startTime"),
        pydantic.Field(
            alias="startTime",
            description="Optional. Inclusive start of the interval.If specified, a Timestamp matching this interval will have to be the same or after the start.",
        ),
    ] = None
    """
    Optional. Inclusive start of the interval.If specified, a Timestamp matching this interval will have to be the same or after the start.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
