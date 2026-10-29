

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .concept_query_type import ConceptQueryType
from .date_aggregation_mode import DateAggregationMode


class ConceptQuery(UniversalBaseModel):
    """
    The fundamental query of Conquery. Executes a query, where all fulfilling entities are included as a single line, containing the aggregated validity-dates, as well as any requested selects. The first columns are unique ids of the entity, then the event-dates column, and then in unspecified order all select results. A CONCEPT_QUERY represents a tree of logically composed query elements, where the leafs are CONCEPT nodes, describing filtering and aggregation.
    """

    root: typing.Optional["CqElement"] = None
    date_aggregation_mode: typing_extensions.Annotated[
        typing.Optional[DateAggregationMode],
        FieldMetadata(alias="dateAggregationMode"),
        pydantic.Field(alias="dateAggregationMode"),
    ] = None
    type: typing.Optional[ConceptQueryType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


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

update_forward_refs(
    ConceptQuery,
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
