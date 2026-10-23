

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .condition_group_conditions_item_zero_right_operand_static_value import (
    ConditionGroupConditionsItemZeroRightOperandStaticValue,
)


class ConditionGroupConditionsItemZeroRightOperandStatic(UniversalBaseModel):
    value: ConditionGroupConditionsItemZeroRightOperandStaticValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
