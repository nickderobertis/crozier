

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .condition_group_connector import ConditionGroupConnector


class ConditionGroup(UniversalBaseModel):
    id: str
    connector: ConditionGroupConnector
    conditions: typing.List["ConditionGroupConditionsItem"]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .condition_group_conditions_item import ConditionGroupConditionsItem

update_forward_refs(ConditionGroup, ConditionGroupConditionsItem=ConditionGroupConditionsItem)
