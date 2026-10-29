

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, update_forward_refs
from ..core.serialization import FieldMetadata
from .cq_element_base import CqElementBase
from .date_range import DateRange


class CqDateRestriction(CqElementBase):
    """
    Restricts the events, downstream components receive to the specified absolute period. This node is fulfilled, if the downstream child is fulfilled.
    """

    date_range: typing_extensions.Annotated[
        typing.Optional[DateRange], FieldMetadata(alias="dateRange"), pydantic.Field(alias="dateRange")
    ] = None
    child: typing.Optional["CqElement"] = None

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
from .cq_days_before import CqDaysBefore
from .cq_days_before_or_never import CqDaysBeforeOrNever
from .cq_element import CqElement
from .cq_negation import CqNegation
from .cq_or import CqOr
from .cq_result_info_decorator import CqResultInfoDecorator
from .cq_same import CqSame
from .cq_sampled import CqSampled

update_forward_refs(
    CqDateRestriction,
    CqAnd=CqAnd,
    CqBefore=CqBefore,
    CqBeforeOrSame=CqBeforeOrSame,
    CqDaysBefore=CqDaysBefore,
    CqDaysBeforeOrNever=CqDaysBeforeOrNever,
    CqElement=CqElement,
    CqNegation=CqNegation,
    CqOr=CqOr,
    CqResultInfoDecorator=CqResultInfoDecorator,
    CqSame=CqSame,
    CqSampled=CqSampled,
)
