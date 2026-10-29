

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, update_forward_refs
from ..core.serialization import FieldMetadata
from .cq_element_base import CqElementBase


class CqAnd(CqElementBase):
    """
    Logically ands its downstream children: If all downstream element are fulfilled, this node is fulfilled.
    """

    children: typing.Optional[typing.List["CqElement"]] = None
    create_exists: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="createExists"),
        pydantic.Field(
            alias="createExists",
            description="Allows the creation of a virtual select that reflects if this node is fulfilled or not. Useful for the creation of more complex concepts.",
        ),
    ] = None
    """
    Allows the creation of a virtual select that reflects if this node is fulfilled or not. Useful for the creation of more complex concepts.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


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
    CqAnd,
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
