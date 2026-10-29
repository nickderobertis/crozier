

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, update_forward_refs
from .cq_element_base import CqElementBase


class CqResultInfoDecorator(CqElementBase):
    values: typing.Optional[typing.Dict[str, str]] = None
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
from .cq_date_restriction import CqDateRestriction
from .cq_days_before import CqDaysBefore
from .cq_days_before_or_never import CqDaysBeforeOrNever
from .cq_element import CqElement
from .cq_negation import CqNegation
from .cq_or import CqOr
from .cq_same import CqSame
from .cq_sampled import CqSampled

update_forward_refs(
    CqResultInfoDecorator,
    CqAnd=CqAnd,
    CqBefore=CqBefore,
    CqBeforeOrSame=CqBeforeOrSame,
    CqDateRestriction=CqDateRestriction,
    CqDaysBefore=CqDaysBefore,
    CqDaysBeforeOrNever=CqDaysBeforeOrNever,
    CqElement=CqElement,
    CqNegation=CqNegation,
    CqOr=CqOr,
    CqSame=CqSame,
    CqSampled=CqSampled,
)
