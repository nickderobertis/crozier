

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .column_id import ColumnId
from .date_distance_filter_time_unit import DateDistanceFilterTimeUnit
from .template_id import TemplateId


class Filter_DateDistance(UniversalBaseModel):
    type: typing.Literal["DATE_DISTANCE"] = "DATE_DISTANCE"
    column: typing.Optional[ColumnId] = None
    time_unit: typing_extensions.Annotated[
        typing.Optional[DateDistanceFilterTimeUnit], FieldMetadata(alias="timeUnit"), pydantic.Field(alias="timeUnit")
    ] = None
    unit: typing.Optional[str] = None
    tooltip: typing.Optional[str] = None
    pattern: typing.Optional[str] = None
    allow_drop_file: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="allowDropFile"), pydantic.Field(alias="allowDropFile")
    ] = None
    default_value: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="defaultValue"),
        pydantic.Field(alias="defaultValue"),
    ] = None
    name: typing.Optional[str] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Filter_Number(UniversalBaseModel):
    type: typing.Literal["NUMBER"] = "NUMBER"
    column: typing.Optional[ColumnId] = None
    unit: typing.Optional[str] = None
    tooltip: typing.Optional[str] = None
    pattern: typing.Optional[str] = None
    allow_drop_file: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="allowDropFile"), pydantic.Field(alias="allowDropFile")
    ] = None
    default_value: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="defaultValue"),
        pydantic.Field(alias="defaultValue"),
    ] = None
    name: typing.Optional[str] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Filter_QuartersInYear(UniversalBaseModel):
    type: typing.Literal["QUARTERS_IN_YEAR"] = "QUARTERS_IN_YEAR"
    column: typing.Optional[ColumnId] = None
    unit: typing.Optional[str] = None
    tooltip: typing.Optional[str] = None
    pattern: typing.Optional[str] = None
    allow_drop_file: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="allowDropFile"), pydantic.Field(alias="allowDropFile")
    ] = None
    default_value: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="defaultValue"),
        pydantic.Field(alias="defaultValue"),
    ] = None
    name: typing.Optional[str] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Filter_DurationSum(UniversalBaseModel):
    type: typing.Literal["DURATION_SUM"] = "DURATION_SUM"
    column: typing.Optional[ColumnId] = None
    unit: typing.Optional[str] = None
    tooltip: typing.Optional[str] = None
    pattern: typing.Optional[str] = None
    allow_drop_file: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="allowDropFile"), pydantic.Field(alias="allowDropFile")
    ] = None
    default_value: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="defaultValue"),
        pydantic.Field(alias="defaultValue"),
    ] = None
    name: typing.Optional[str] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Filter_MultiSelect(UniversalBaseModel):
    type: typing.Literal["MULTI_SELECT"] = "MULTI_SELECT"
    column: typing.Optional[ColumnId] = None
    labels: typing.Optional[typing.Dict[str, str]] = None
    template: typing.Optional[TemplateId] = None
    unit: typing.Optional[str] = None
    tooltip: typing.Optional[str] = None
    pattern: typing.Optional[str] = None
    allow_drop_file: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="allowDropFile"), pydantic.Field(alias="allowDropFile")
    ] = None
    default_value: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="defaultValue"),
        pydantic.Field(alias="defaultValue"),
    ] = None
    name: typing.Optional[str] = None
    label: typing.Optional[str] = None
    search_min_suffix_length: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="searchMinSuffixLength"),
        pydantic.Field(alias="searchMinSuffixLength"),
    ] = None
    generate_search_suffixes: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="generateSearchSuffixes"),
        pydantic.Field(alias="generateSearchSuffixes"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Filter_BigMultiSelect(UniversalBaseModel):
    type: typing.Literal["BIG_MULTI_SELECT"] = "BIG_MULTI_SELECT"
    column: typing.Optional[ColumnId] = None
    labels: typing.Optional[typing.Dict[str, str]] = None
    template: typing.Optional[TemplateId] = None
    unit: typing.Optional[str] = None
    tooltip: typing.Optional[str] = None
    pattern: typing.Optional[str] = None
    allow_drop_file: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="allowDropFile"), pydantic.Field(alias="allowDropFile")
    ] = None
    default_value: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="defaultValue"),
        pydantic.Field(alias="defaultValue"),
    ] = None
    name: typing.Optional[str] = None
    label: typing.Optional[str] = None
    search_min_suffix_length: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="searchMinSuffixLength"),
        pydantic.Field(alias="searchMinSuffixLength"),
    ] = None
    generate_search_suffixes: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="generateSearchSuffixes"),
        pydantic.Field(alias="generateSearchSuffixes"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Filter_SingleSelect(UniversalBaseModel):
    type: typing.Literal["SINGLE_SELECT"] = "SINGLE_SELECT"
    column: typing.Optional[ColumnId] = None
    labels: typing.Optional[typing.Dict[str, str]] = None
    template: typing.Optional[TemplateId] = None
    unit: typing.Optional[str] = None
    tooltip: typing.Optional[str] = None
    pattern: typing.Optional[str] = None
    allow_drop_file: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="allowDropFile"), pydantic.Field(alias="allowDropFile")
    ] = None
    default_value: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="defaultValue"),
        pydantic.Field(alias="defaultValue"),
    ] = None
    name: typing.Optional[str] = None
    label: typing.Optional[str] = None
    search_min_suffix_length: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="searchMinSuffixLength"),
        pydantic.Field(alias="searchMinSuffixLength"),
    ] = None
    generate_search_suffixes: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="generateSearchSuffixes"),
        pydantic.Field(alias="generateSearchSuffixes"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Filter_Flags(UniversalBaseModel):
    type: typing.Literal["FLAGS"] = "FLAGS"
    flags: typing.Optional[typing.Dict[str, ColumnId]] = None
    unit: typing.Optional[str] = None
    tooltip: typing.Optional[str] = None
    pattern: typing.Optional[str] = None
    allow_drop_file: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="allowDropFile"), pydantic.Field(alias="allowDropFile")
    ] = None
    default_value: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="defaultValue"),
        pydantic.Field(alias="defaultValue"),
    ] = None
    name: typing.Optional[str] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Filter_Count(UniversalBaseModel):
    type: typing.Literal["COUNT"] = "COUNT"
    distinct: typing.Optional[bool] = None
    column: typing.Optional[ColumnId] = None
    distinct_by_column: typing_extensions.Annotated[
        typing.Optional[typing.List[ColumnId]],
        FieldMetadata(alias="distinctByColumn"),
        pydantic.Field(alias="distinctByColumn"),
    ] = None
    unit: typing.Optional[str] = None
    tooltip: typing.Optional[str] = None
    pattern: typing.Optional[str] = None
    allow_drop_file: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="allowDropFile"), pydantic.Field(alias="allowDropFile")
    ] = None
    default_value: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="defaultValue"),
        pydantic.Field(alias="defaultValue"),
    ] = None
    name: typing.Optional[str] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Filter_Sum(UniversalBaseModel):
    type: typing.Literal["SUM"] = "SUM"
    distinct: typing.Optional[bool] = None
    column: typing.Optional[ColumnId] = None
    subtract_column: typing_extensions.Annotated[
        typing.Optional[ColumnId], FieldMetadata(alias="subtractColumn"), pydantic.Field(alias="subtractColumn")
    ] = None
    distinct_by_column: typing_extensions.Annotated[
        typing.Optional[typing.List[ColumnId]],
        FieldMetadata(alias="distinctByColumn"),
        pydantic.Field(alias="distinctByColumn"),
    ] = None
    unit: typing.Optional[str] = None
    tooltip: typing.Optional[str] = None
    pattern: typing.Optional[str] = None
    allow_drop_file: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="allowDropFile"), pydantic.Field(alias="allowDropFile")
    ] = None
    default_value: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="defaultValue"),
        pydantic.Field(alias="defaultValue"),
    ] = None
    name: typing.Optional[str] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Filter = typing_extensions.Annotated[
    typing.Union[
        Filter_DateDistance,
        Filter_Number,
        Filter_QuartersInYear,
        Filter_DurationSum,
        Filter_MultiSelect,
        Filter_BigMultiSelect,
        Filter_SingleSelect,
        Filter_Flags,
        Filter_Count,
        Filter_Sum,
    ],
    pydantic.Field(discriminator="type"),
]
