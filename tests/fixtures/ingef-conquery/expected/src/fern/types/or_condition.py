

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class OrCondition(UniversalBaseModel):
    conditions: typing.Optional[typing.List["ConceptCondition"]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .and_condition import AndCondition
from .concept_condition import ConceptCondition
from .not_condition import NotCondition

update_forward_refs(
    OrCondition, AndCondition=AndCondition, ConceptCondition=ConceptCondition, NotCondition=NotCondition
)
