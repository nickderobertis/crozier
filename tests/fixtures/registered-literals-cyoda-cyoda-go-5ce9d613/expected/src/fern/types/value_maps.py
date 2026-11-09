

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .local_time import LocalTime
from .value_maps_type_references_value import ValueMapsTypeReferencesValue
from .value_maps_year_months_value import ValueMapsYearMonthsValue
from .value_maps_years_value import ValueMapsYearsValue


class ValueMaps(UniversalBaseModel):
    strings: typing.Optional[typing.Dict[str, str]] = None
    chars: typing.Optional[typing.Dict[str, str]] = None
    doubles: typing.Optional[typing.Dict[str, float]] = None
    floats: typing.Optional[typing.Dict[str, float]] = None
    bytes: typing.Optional[typing.Dict[str, str]] = None
    shorts: typing.Optional[typing.Dict[str, int]] = None
    longs: typing.Optional[typing.Dict[str, int]] = None
    ints: typing.Optional[typing.Dict[str, int]] = None
    local_dates: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, dt.date]],
        FieldMetadata(alias="localDates"),
        pydantic.Field(alias="localDates"),
    ] = None
    local_date_times: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, dt.datetime]],
        FieldMetadata(alias="localDateTimes"),
        pydantic.Field(alias="localDateTimes"),
    ] = None
    local_times: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, LocalTime]],
        FieldMetadata(alias="localTimes"),
        pydantic.Field(alias="localTimes"),
    ] = None
    zoned_date_times: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, dt.datetime]],
        FieldMetadata(alias="zonedDateTimes"),
        pydantic.Field(alias="zonedDateTimes"),
    ] = None
    years: typing.Optional[typing.Dict[str, ValueMapsYearsValue]] = None
    year_months: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, ValueMapsYearMonthsValue]],
        FieldMetadata(alias="yearMonths"),
        pydantic.Field(alias="yearMonths"),
    ] = None
    big_decimals: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, float]],
        FieldMetadata(alias="bigDecimals"),
        pydantic.Field(alias="bigDecimals"),
    ] = None
    unbound_decimals: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, float]],
        FieldMetadata(alias="unboundDecimals"),
        pydantic.Field(alias="unboundDecimals"),
    ] = None
    big_integers: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, int]], FieldMetadata(alias="bigIntegers"), pydantic.Field(alias="bigIntegers")
    ] = None
    unbound_integers: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, int]],
        FieldMetadata(alias="unboundIntegers"),
        pydantic.Field(alias="unboundIntegers"),
    ] = None
    booleans: typing.Optional[typing.Dict[str, bool]] = None
    uuids: typing.Optional[typing.Dict[str, str]] = None
    timeuuids: typing.Optional[typing.Dict[str, str]] = None
    byte_arrays: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]], FieldMetadata(alias="byteArrays"), pydantic.Field(alias="byteArrays")
    ] = None
    others: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]] = None
    nulls: typing.Optional[typing.Dict[str, str]] = None
    type_references: typing_extensions.Annotated[
        typing.Dict[str, ValueMapsTypeReferencesValue],
        FieldMetadata(alias="typeReferences"),
        pydantic.Field(alias="typeReferences"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
