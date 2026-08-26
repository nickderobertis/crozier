

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .direction import Direction
from .fraction import Fraction


class AccessibilityRequestRoadSectionRestriction(UniversalBaseModel):
    id: int
    direction: Direction
    fraction: Fraction

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
