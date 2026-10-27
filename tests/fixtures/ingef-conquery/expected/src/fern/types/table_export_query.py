

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .cq_concept import CqConcept
from .date_range import DateRange


class TableExportQuery(UniversalBaseModel):
    """
    For all entities fulfilling the sub-query, export raw data of selected tables over the selected period. The output format is in wide format, meaning all tables are concatenated, but only single rows are emitted with only the columns of the source table filled. Columns of the same SecondaryId will be grouped and marked with SECONDARY_ID Semantics. The source column will contain the Id of the source table. The CONCEPT nodes can be used for filtering single rows.
    """

    query: typing.Optional["Query"] = None
    date_range: typing_extensions.Annotated[
        typing.Optional[DateRange], FieldMetadata(alias="dateRange"), pydantic.Field(alias="dateRange")
    ] = None
    tables: typing.Optional[typing.List[CqConcept]] = None
    raw_concept_values: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="rawConceptValues"),
        pydantic.Field(
            alias="rawConceptValues",
            description="If true, columns of concepts will be emitted as raw values. Else they will be emitted as resolved ids of the concept-elements.",
        ),
    ] = None
    """
    If true, columns of concepts will be emitted as raw values. Else they will be emitted as resolved ids of the concept-elements.
    """

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
from .relative_form_query import RelativeFormQuery

update_forward_refs(
    TableExportQuery,
    AbsoluteFormQuery=AbsoluteFormQuery,
    EntityDateQuery=EntityDateQuery,
    Query=Query,
    RelativeFormQuery=RelativeFormQuery,
)
