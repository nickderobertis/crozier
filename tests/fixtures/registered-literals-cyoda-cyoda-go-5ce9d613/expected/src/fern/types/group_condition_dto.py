

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, update_forward_refs
from .abstract_condition_dto import AbstractConditionDto
from .group_condition_dto_operator import GroupConditionDtoOperator


class GroupConditionDto(AbstractConditionDto):
    operator: GroupConditionDtoOperator
    conditions: typing.List["GroupConditionDtoConditionsItem"]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .group_condition_dto_conditions_item import GroupConditionDtoConditionsItem

update_forward_refs(GroupConditionDto, GroupConditionDtoConditionsItem=GroupConditionDtoConditionsItem)
