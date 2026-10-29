

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .column_id import ColumnId
from .temporal_sampler import TemporalSampler


class UniversalSelect_ConceptColumn(UniversalBaseModel):
    """
    Selects that can be used both on Concept and Connector level.
    """

    type: typing.Literal["CONCEPT_COLUMN"] = "CONCEPT_COLUMN"
    as_ids: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="asIds"), pydantic.Field(alias="asIds")
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


class UniversalSelect_CountQuarters(UniversalBaseModel):
    """
    Selects that can be used both on Concept and Connector level.
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


class UniversalSelect_EventDateUnion(UniversalBaseModel):
    """
    Selects that can be used both on Concept and Connector level.
    """

    type: typing.Literal["EVENT_DATE_UNION"] = "EVENT_DATE_UNION"
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


class UniversalSelect_EventDurationSum(UniversalBaseModel):
    """
    Selects that can be used both on Concept and Connector level.
    """

    type: typing.Literal["EVENT_DURATION_SUM"] = "EVENT_DURATION_SUM"
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


class UniversalSelect_Exists(UniversalBaseModel):
    """
    Selects that can be used both on Concept and Connector level.
    """

    type: typing.Literal["EXISTS"] = "EXISTS"
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


class UniversalSelect_Quarter(UniversalBaseModel):
    """
    Selects that can be used both on Concept and Connector level.
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


UniversalSelect = typing_extensions.Annotated[
    typing.Union[
        UniversalSelect_ConceptColumn,
        UniversalSelect_CountQuarters,
        UniversalSelect_EventDateUnion,
        UniversalSelect_EventDurationSum,
        UniversalSelect_Exists,
        UniversalSelect_Quarter,
    ],
    pydantic.Field(discriminator="type"),
]
