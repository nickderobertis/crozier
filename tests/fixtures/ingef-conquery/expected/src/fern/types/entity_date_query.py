

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .array_concept_query import ArrayConceptQuery
from .date_aggregation_mode import DateAggregationMode
from .date_range import DateRange
from .resolution_and_alignment import ResolutionAndAlignment


class EntityDateQuery(UniversalBaseModel):
    """
    Export a set of features for all entities satisfying the query, over the query's result date. See AbsoluteFormQuery for comparison.
    """

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


from .absolute_form_query import AbsoluteFormQuery
from .query import Query
from .relative_form_query import RelativeFormQuery
from .table_export_query import TableExportQuery

update_forward_refs(
    EntityDateQuery,
    AbsoluteFormQuery=AbsoluteFormQuery,
    Query=Query,
    RelativeFormQuery=RelativeFormQuery,
    TableExportQuery=TableExportQuery,
)
