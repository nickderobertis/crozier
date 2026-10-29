

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .array_concept_query import ArrayConceptQuery
from .relative_form_query_index_placement import RelativeFormQueryIndexPlacement
from .relative_form_query_time_unit import RelativeFormQueryTimeUnit
from .resolution_and_alignment import ResolutionAndAlignment
from .temporal_sampler import TemporalSampler


class RelativeFormQuery(UniversalBaseModel):
    """
    Export a set of features for all included entities. The periods to export are determined relative to the resulting event-dates per entity by sampling a single day. The parameters timeCountBefore/-After determine how many consecutive periods are exported for the feature (before) and outcome (after) range. The index date either belongs to the feature range (indexPlacement BEFORE), the outcome range (AFTER) or lies in between (NEUTRAL) In the feature range, the period closest to the index date has the index=-1. Earlier periods have a decremented index in respect to their sequence. Accordingly, the period closest to the index date in the outcome range starts at index=1. Subsequent periods have an incremented index.
    """

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


from .absolute_form_query import AbsoluteFormQuery
from .entity_date_query import EntityDateQuery
from .query import Query
from .table_export_query import TableExportQuery

update_forward_refs(
    RelativeFormQuery,
    AbsoluteFormQuery=AbsoluteFormQuery,
    EntityDateQuery=EntityDateQuery,
    Query=Query,
    TableExportQuery=TableExportQuery,
)
