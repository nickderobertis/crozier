

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .time_stat_data_dto_measure_desc import TimeStatDataDtoMeasureDesc


class TimeStatDataDto(UniversalBaseModel):
    """
    Timing statistics data with automatic unit selection for optimal readability
    """

    num_calls: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="numCalls"),
        pydantic.Field(alias="numCalls", description="Number of timing measurements recorded"),
    ] = None
    """
    Number of timing measurements recorded
    """

    total: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total cumulative execution time across all operations, converted to seconds for readability
    """

    last: typing.Optional[int] = pydantic.Field(default=None)
    """
    Most recent execution time in nanoseconds
    """

    min: typing.Optional[int] = pydantic.Field(default=None)
    """
    Minimum execution time in nanoseconds
    """

    max: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum execution time in nanoseconds
    """

    avg: typing.Optional[int] = pydantic.Field(default=None)
    """
    Average execution time in nanoseconds
    """

    measure: typing.Optional[int] = pydantic.Field(default=None)
    """
    Suggested conversion factor from nanoseconds to the recommended display unit. Divide nanosecond values by this to get values in the suggested unit.
    """

    measure_desc: typing_extensions.Annotated[
        typing.Optional[TimeStatDataDtoMeasureDesc],
        FieldMetadata(alias="measureDesc"),
        pydantic.Field(
            alias="measureDesc",
            description="Suggested unit abbreviation for displaying timing values based on magnitude analysis",
        ),
    ] = None
    """
    Suggested unit abbreviation for displaying timing values based on magnitude analysis
    """

    from0to100micros: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="from0To100Micros"), pydantic.Field(alias="from0To100Micros")
    ] = None
    from100micros_to1millis: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="from100MicrosTo1Millis"),
        pydantic.Field(alias="from100MicrosTo1Millis"),
    ] = None
    from1to10millis: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="from1To10Millis"),
        pydantic.Field(alias="from1To10Millis"),
    ] = None
    from10to100millis: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="from10To100Millis"),
        pydantic.Field(alias="from10To100Millis"),
    ] = None
    from100millis_to1second: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="from100MillisTo1Second"),
        pydantic.Field(alias="from100MillisTo1Second"),
    ] = None
    from1to10seconds: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="from1To10Seconds"),
        pydantic.Field(alias="from1To10Seconds"),
    ] = None
    from10seconds: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="from10Seconds"), pydantic.Field(alias="from10Seconds")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
