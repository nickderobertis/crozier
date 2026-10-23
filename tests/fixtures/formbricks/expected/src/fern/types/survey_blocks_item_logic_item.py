

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .survey_blocks_item_logic_item_actions_item import SurveyBlocksItemLogicItemActionsItem


class SurveyBlocksItemLogicItem(UniversalBaseModel):
    id: str
    conditions: "ConditionGroup"
    actions: typing.List[SurveyBlocksItemLogicItemActionsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .condition_group import ConditionGroup
from .condition_group_conditions_item import ConditionGroupConditionsItem

update_forward_refs(
    SurveyBlocksItemLogicItem, ConditionGroup=ConditionGroup, ConditionGroupConditionsItem=ConditionGroupConditionsItem
)
