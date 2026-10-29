

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .array_concept_query_type import ArrayConceptQueryType
from .concept_query import ConceptQuery
from .date_aggregation_mode import DateAggregationMode


class ArrayConceptQuery(UniversalBaseModel):
    """
    Building block of export-forms: evaluates all queries independently, exporting their selects.
    """

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
    type: typing.Optional[ArrayConceptQueryType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(ArrayConceptQuery)
