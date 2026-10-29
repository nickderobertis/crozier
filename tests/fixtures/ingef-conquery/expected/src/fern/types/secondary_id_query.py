

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .date_aggregation_mode import DateAggregationMode
from .secondary_id_id import SecondaryIdId
from .secondary_id_query_type import SecondaryIdQueryType


class SecondaryIdQuery(UniversalBaseModel):
    """
    Executes concept-queries grouped by a secondary key - in addition to entities. Therefore, multiple columns are emitted per entity. The secondary-ids are put into a column named after its label, tagged with SECONDARY_ID Semantics.
    """

    root: typing.Optional["CqElement"] = None
    secondary_id: typing_extensions.Annotated[
        typing.Optional[SecondaryIdId], FieldMetadata(alias="secondaryId"), pydantic.Field(alias="secondaryId")
    ] = None
    date_aggregation_mode: typing_extensions.Annotated[
        typing.Optional[DateAggregationMode],
        FieldMetadata(alias="dateAggregationMode"),
        pydantic.Field(alias="dateAggregationMode"),
    ] = None
    type: typing.Optional[SecondaryIdQueryType] = None

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
    SecondaryIdQuery,
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
