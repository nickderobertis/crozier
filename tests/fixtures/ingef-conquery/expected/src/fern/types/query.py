

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .array_concept_query import ArrayConceptQuery
from .concept_query import ConceptQuery
from .cq_concept import CqConcept
from .date_aggregation_mode import DateAggregationMode
from .date_range import DateRange
from .relative_form_query_index_placement import RelativeFormQueryIndexPlacement
from .relative_form_query_time_unit import RelativeFormQueryTimeUnit
from .resolution_and_alignment import ResolutionAndAlignment
from .temporal_sampler import TemporalSampler


class Query_ConceptQuery(UniversalBaseModel):
    type: typing.Literal["CONCEPT_QUERY"] = "CONCEPT_QUERY"
    root: typing.Optional["CqElement"] = None
    date_aggregation_mode: typing_extensions.Annotated[
        typing.Optional[DateAggregationMode],
        FieldMetadata(alias="dateAggregationMode"),
        pydantic.Field(alias="dateAggregationMode"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Query_AbsoluteFormQuery(UniversalBaseModel):
    type: typing.Literal["ABSOLUTE_FORM_QUERY"] = "ABSOLUTE_FORM_QUERY"
    query: typing.Optional["Query"] = None
    features: typing.Optional[ArrayConceptQuery] = None
    resolutions_and_alignment_map: typing_extensions.Annotated[
        typing.Optional[typing.List[ResolutionAndAlignment]],
        FieldMetadata(alias="resolutionsAndAlignmentMap"),
        pydantic.Field(alias="resolutionsAndAlignmentMap"),
    ] = None
    date_range: typing_extensions.Annotated[
        typing.Optional[DateRange], FieldMetadata(alias="dateRange"), pydantic.Field(alias="dateRange")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Query_EntityDateQuery(UniversalBaseModel):
    type: typing.Literal["ENTITY_DATE_QUERY"] = "ENTITY_DATE_QUERY"
    query: typing.Optional["Query"] = None
    features: typing.Optional[ArrayConceptQuery] = None
    resolutions_and_alignments: typing_extensions.Annotated[
        typing.Optional[typing.List[ResolutionAndAlignment]],
        FieldMetadata(alias="resolutionsAndAlignments"),
        pydantic.Field(alias="resolutionsAndAlignments"),
    ] = None
    date_range: typing_extensions.Annotated[
        typing.Optional[DateRange], FieldMetadata(alias="dateRange"), pydantic.Field(alias="dateRange")
    ] = None
    date_aggregation_mode: typing_extensions.Annotated[
        typing.Optional[DateAggregationMode],
        FieldMetadata(alias="dateAggregationMode"),
        pydantic.Field(alias="dateAggregationMode"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Query_RelativeFormQuery(UniversalBaseModel):
    type: typing.Literal["RELATIVE_FORM_QUERY"] = "RELATIVE_FORM_QUERY"
    query: typing.Optional["Query"] = None
    features: typing.Optional[ArrayConceptQuery] = None
    index_selector: typing_extensions.Annotated[
        typing.Optional[TemporalSampler], FieldMetadata(alias="indexSelector"), pydantic.Field(alias="indexSelector")
    ] = None
    index_placement: typing_extensions.Annotated[
        typing.Optional[RelativeFormQueryIndexPlacement],
        FieldMetadata(alias="indexPlacement"),
        pydantic.Field(alias="indexPlacement"),
    ] = None
    time_count_before: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="timeCountBefore"), pydantic.Field(alias="timeCountBefore")
    ] = None
    time_count_after: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="timeCountAfter"), pydantic.Field(alias="timeCountAfter")
    ] = None
    time_unit: typing_extensions.Annotated[
        typing.Optional[RelativeFormQueryTimeUnit], FieldMetadata(alias="timeUnit"), pydantic.Field(alias="timeUnit")
    ] = None
    resolutions_and_alignment_map: typing_extensions.Annotated[
        typing.Optional[typing.List[ResolutionAndAlignment]],
        FieldMetadata(alias="resolutionsAndAlignmentMap"),
        pydantic.Field(alias="resolutionsAndAlignmentMap"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Query_ArrayConceptQuery(UniversalBaseModel):
    type: typing.Literal["ARRAY_CONCEPT_QUERY"] = "ARRAY_CONCEPT_QUERY"
    child_queries: typing_extensions.Annotated[
        typing.Optional[typing.List[ConceptQuery]],
        FieldMetadata(alias="childQueries"),
        pydantic.Field(alias="childQueries"),
    ] = None
    date_aggregation_mode: typing_extensions.Annotated[
        typing.Optional[DateAggregationMode],
        FieldMetadata(alias="dateAggregationMode"),
        pydantic.Field(alias="dateAggregationMode"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Query_SecondaryIdQuery(UniversalBaseModel):
    value: typing.Any
    type: typing.Literal["SECONDARY_ID_QUERY"] = "SECONDARY_ID_QUERY"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True


class Query_TableExport(UniversalBaseModel):
    type: typing.Literal["TABLE_EXPORT"] = "TABLE_EXPORT"
    query: typing.Optional["Query"] = None
    date_range: typing_extensions.Annotated[
        typing.Optional[DateRange], FieldMetadata(alias="dateRange"), pydantic.Field(alias="dateRange")
    ] = None
    tables: typing.Optional[typing.List[CqConcept]] = None
    raw_concept_values: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="rawConceptValues"), pydantic.Field(alias="rawConceptValues")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Query = typing_extensions.Annotated[
    typing.Union[
        Query_ConceptQuery,
        Query_AbsoluteFormQuery,
        Query_EntityDateQuery,
        Query_RelativeFormQuery,
        Query_ArrayConceptQuery,
        Query_SecondaryIdQuery,
        Query_TableExport,
    ],
    pydantic.Field(discriminator="type"),
]
from .cq_and import CqAnd
from .cq_before import CqBefore
from .cq_before_or_same import CqBeforeOrSame
from .cq_date_restriction import CqDateRestriction
from .cq_days_before import CqDaysBefore
from .cq_days_before_or_never import CqDaysBeforeOrNever
from .cq_element import CqElement
from .cq_negation import CqNegation
from .cq_or import CqOr
from .cq_result_info_decorator import CqResultInfoDecorator
from .cq_same import CqSame
from .cq_sampled import CqSampled
from .entity_date_query import EntityDateQuery
from .relative_form_query import RelativeFormQuery
from .table_export_query import TableExportQuery
from .absolute_form_query import AbsoluteFormQuery

update_forward_refs(
    Query_ConceptQuery,
    CqAnd=CqAnd,
    CqBefore=CqBefore,
    CqBeforeOrSame=CqBeforeOrSame,
    CqDateRestriction=CqDateRestriction,
    CqDaysBefore=CqDaysBefore,
    CqDaysBeforeOrNever=CqDaysBeforeOrNever,
    CqElement=CqElement,
    CqNegation=CqNegation,
    CqOr=CqOr,
    CqResultInfoDecorator=CqResultInfoDecorator,
    CqSame=CqSame,
    CqSampled=CqSampled,
)
update_forward_refs(
    Query_AbsoluteFormQuery,
    EntityDateQuery=EntityDateQuery,
    Query=Query,
    RelativeFormQuery=RelativeFormQuery,
    TableExportQuery=TableExportQuery,
)
update_forward_refs(
    Query_EntityDateQuery,
    AbsoluteFormQuery=AbsoluteFormQuery,
    Query=Query,
    RelativeFormQuery=RelativeFormQuery,
    TableExportQuery=TableExportQuery,
)
update_forward_refs(
    Query_RelativeFormQuery,
    AbsoluteFormQuery=AbsoluteFormQuery,
    EntityDateQuery=EntityDateQuery,
    Query=Query,
    TableExportQuery=TableExportQuery,
)
update_forward_refs(Query_ArrayConceptQuery)
update_forward_refs(
    Query_TableExport,
    AbsoluteFormQuery=AbsoluteFormQuery,
    EntityDateQuery=EntityDateQuery,
    Query=Query,
    RelativeFormQuery=RelativeFormQuery,
)
