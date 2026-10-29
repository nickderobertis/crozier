

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .column_id import ColumnId
from .date_distance_select_time_unit import DateDistanceSelectTimeUnit
from .mapping_id import MappingId
from .temporal_sampler import TemporalSampler


class Select_Count(UniversalBaseModel):
    """
    Selects allow users to add aggregations to the output. Selects can only be placed in Connectors, as opposed to UniversalSelects, which can also be placed in Concepts.
    """

    type: typing.Literal["COUNT"] = "COUNT"
    distinct: typing.Optional[bool] = None
    column: typing.Optional[ColumnId] = None
    distinct_by_column: typing_extensions.Annotated[
        typing.Optional[typing.List[ColumnId]],
        FieldMetadata(alias="distinctByColumn"),
        pydantic.Field(alias="distinctByColumn"),
    ] = None
    description: typing.Optional[str] = None
    default: typing.Optional[bool] = None
    name: typing.Optional[str] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Select_CountQuarters(UniversalBaseModel):
    """
    Selects allow users to add aggregations to the output. Selects can only be placed in Connectors, as opposed to UniversalSelects, which can also be placed in Concepts.
    """

    type: typing.Literal["COUNT_QUARTERS"] = "COUNT_QUARTERS"
    column: typing.Optional[ColumnId] = None
    description: typing.Optional[str] = None
    default: typing.Optional[bool] = None
    name: typing.Optional[str] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Select_DateDistance(UniversalBaseModel):
    """
    Selects allow users to add aggregations to the output. Selects can only be placed in Connectors, as opposed to UniversalSelects, which can also be placed in Concepts.
    """

    type: typing.Literal["DATE_DISTANCE"] = "DATE_DISTANCE"
    column: typing.Optional[ColumnId] = None
    time_unit: typing_extensions.Annotated[
        typing.Optional[DateDistanceSelectTimeUnit], FieldMetadata(alias="timeUnit"), pydantic.Field(alias="timeUnit")
    ] = None
    description: typing.Optional[str] = None
    default: typing.Optional[bool] = None
    name: typing.Optional[str] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Select_DateUnion(UniversalBaseModel):
    """
    Selects allow users to add aggregations to the output. Selects can only be placed in Connectors, as opposed to UniversalSelects, which can also be placed in Concepts.
    """

    type: typing.Literal["DATE_UNION"] = "DATE_UNION"
    column: typing.Optional[ColumnId] = None
    description: typing.Optional[str] = None
    default: typing.Optional[bool] = None
    name: typing.Optional[str] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Select_Distinct(UniversalBaseModel):
    """
    Selects allow users to add aggregations to the output. Selects can only be placed in Connectors, as opposed to UniversalSelects, which can also be placed in Concepts.
    """

    type: typing.Literal["DISTINCT"] = "DISTINCT"
    column: typing.Optional[ColumnId] = None
    mapping: typing.Optional[MappingId] = None
    description: typing.Optional[str] = None
    default: typing.Optional[bool] = None
    name: typing.Optional[str] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Select_DurationSum(UniversalBaseModel):
    """
    Selects allow users to add aggregations to the output. Selects can only be placed in Connectors, as opposed to UniversalSelects, which can also be placed in Concepts.
    """

    type: typing.Literal["DURATION_SUM"] = "DURATION_SUM"
    column: typing.Optional[ColumnId] = None
    description: typing.Optional[str] = None
    default: typing.Optional[bool] = None
    name: typing.Optional[str] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Select_First(UniversalBaseModel):
    """
    Selects allow users to add aggregations to the output. Selects can only be placed in Connectors, as opposed to UniversalSelects, which can also be placed in Concepts.
    """

    type: typing.Literal["FIRST"] = "FIRST"
    column: typing.Optional[ColumnId] = None
    mapping: typing.Optional[MappingId] = None
    description: typing.Optional[str] = None
    default: typing.Optional[bool] = None
    name: typing.Optional[str] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Select_Flags(UniversalBaseModel):
    """
    Selects allow users to add aggregations to the output. Selects can only be placed in Connectors, as opposed to UniversalSelects, which can also be placed in Concepts.
    """

    type: typing.Literal["FLAGS"] = "FLAGS"
    flags: typing.Optional[typing.Dict[str, ColumnId]] = None
    description: typing.Optional[str] = None
    default: typing.Optional[bool] = None
    name: typing.Optional[str] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Select_Last(UniversalBaseModel):
    """
    Selects allow users to add aggregations to the output. Selects can only be placed in Connectors, as opposed to UniversalSelects, which can also be placed in Concepts.
    """

    type: typing.Literal["LAST"] = "LAST"
    column: typing.Optional[ColumnId] = None
    mapping: typing.Optional[MappingId] = None
    description: typing.Optional[str] = None
    default: typing.Optional[bool] = None
    name: typing.Optional[str] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Select_Quarter(UniversalBaseModel):
    """
    Selects allow users to add aggregations to the output. Selects can only be placed in Connectors, as opposed to UniversalSelects, which can also be placed in Concepts.
    """

    type: typing.Literal["QUARTER"] = "QUARTER"
    sample: typing.Optional[TemporalSampler] = None
    description: typing.Optional[str] = None
    default: typing.Optional[bool] = None
    name: typing.Optional[str] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Select_QuartersInYear(UniversalBaseModel):
    """
    Selects allow users to add aggregations to the output. Selects can only be placed in Connectors, as opposed to UniversalSelects, which can also be placed in Concepts.
    """

    type: typing.Literal["QUARTERS_IN_YEAR"] = "QUARTERS_IN_YEAR"
    column: typing.Optional[ColumnId] = None
    description: typing.Optional[str] = None
    default: typing.Optional[bool] = None
    name: typing.Optional[str] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Select_Random(UniversalBaseModel):
    """
    Selects allow users to add aggregations to the output. Selects can only be placed in Connectors, as opposed to UniversalSelects, which can also be placed in Concepts.
    """

    type: typing.Literal["RANDOM"] = "RANDOM"
    column: typing.Optional[ColumnId] = None
    mapping: typing.Optional[MappingId] = None
    description: typing.Optional[str] = None
    default: typing.Optional[bool] = None
    name: typing.Optional[str] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Select_Sum(UniversalBaseModel):
    """
    Selects allow users to add aggregations to the output. Selects can only be placed in Connectors, as opposed to UniversalSelects, which can also be placed in Concepts.
    """

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
    description: typing.Optional[str] = None
    default: typing.Optional[bool] = None
    name: typing.Optional[str] = None
    label: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Select = typing_extensions.Annotated[
    typing.Union[
        Select_Count,
        Select_CountQuarters,
        Select_DateDistance,
        Select_DateUnion,
        Select_Distinct,
        Select_DurationSum,
        Select_First,
        Select_Flags,
        Select_Last,
        Select_Quarter,
        Select_QuartersInYear,
        Select_Random,
        Select_Sum,
    ],
    pydantic.Field(discriminator="type"),
]
