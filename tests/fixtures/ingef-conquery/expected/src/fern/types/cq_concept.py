

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .concept_element_id import ConceptElementId
from .cq_concept_tables import CqConceptTables
from .cq_concept_type import CqConceptType
from .cq_element_base import CqElementBase
from .select_id import SelectId


class CqConcept(CqElementBase):
    """
    The fundamental query-element. Contains definitions for filtering and aggregation based on concept defined filters and selects. `ids` contains a list of concept element ids of the same concept, which should be filtered for. `tables` contains one or more description of filters and selects from a specific connector. Filters can be grouped into event-filters and aggregation-filters, where event filters, filter rows, while aggregation-filters aggregate those filtered rows. Selects calculate aggregations on the filtered rows.
    The filters are logically and-ed, meaning this node is only fulfilled if all its filters are fulfilled.
    """

    ids: typing.Optional[ConceptElementId] = None
    tables: typing.Optional[CqConceptTables] = None
    selects: typing.Optional[typing.List[SelectId]] = pydantic.Field(default=None)
    """
    References to UniversalSelects to evaluate while querying.
    """

    exclude_from_secondary_id: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="excludeFromSecondaryId"),
        pydantic.Field(
            alias="excludeFromSecondaryId",
            description="If true, this node is not grouped by a secondaryId even if the referenced tables contain the secondaryId.",
        ),
    ] = None
    """
    If true, this node is not grouped by a secondaryId even if the referenced tables contain the secondaryId.
    """

    exclude_from_time_aggregation: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="excludeFromTimeAggregation"),
        pydantic.Field(alias="excludeFromTimeAggregation", description="If true, do not aggregate time for this node."),
    ] = None
    """
    If true, do not aggregate time for this node.
    """

    type: typing.Optional[CqConceptType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
