

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .array_concept_query import ArrayConceptQuery
from .date_range import DateRange
from .resolution_and_alignment import ResolutionAndAlignment


class AbsoluteFormQuery(UniversalBaseModel):
    """
    Export a set of features over a specified period for all entities the query is fulfilled. Using resolutionsAndAlignmentMap the period can be subdivided into Years, Quarters and Months. The subdivisions can then be aligned to the years, months and quarters. Each subdivision is assigned an increasing index per resolution: The first quarter is index=1, the second quarter index=2, while the first year is index=1 and so on.
    """

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


from .entity_date_query import EntityDateQuery
from .query import Query
from .relative_form_query import RelativeFormQuery
from .table_export_query import TableExportQuery

update_forward_refs(
    AbsoluteFormQuery,
    EntityDateQuery=EntityDateQuery,
    Query=Query,
    RelativeFormQuery=RelativeFormQuery,
    TableExportQuery=TableExportQuery,
)
