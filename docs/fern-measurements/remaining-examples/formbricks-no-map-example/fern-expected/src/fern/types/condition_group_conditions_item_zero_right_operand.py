

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .condition_group_conditions_item_zero_right_operand_hidden_field import (
    ConditionGroupConditionsItemZeroRightOperandHiddenField,
)
from .condition_group_conditions_item_zero_right_operand_static_value import (
    ConditionGroupConditionsItemZeroRightOperandStaticValue,
)


class ConditionGroupConditionsItemZeroRightOperand_Static(UniversalBaseModel):
    type: typing.Literal["static"] = "static"
    value: ConditionGroupConditionsItemZeroRightOperandStaticValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ConditionGroupConditionsItemZeroRightOperand_HiddenField(UniversalBaseModel):
    value: ConditionGroupConditionsItemZeroRightOperandHiddenField
    type: typing.Literal["hiddenField"] = "hiddenField"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True


ConditionGroupConditionsItemZeroRightOperand = typing_extensions.Annotated[
    typing.Union[
        ConditionGroupConditionsItemZeroRightOperand_Static, ConditionGroupConditionsItemZeroRightOperand_HiddenField
    ],
    pydantic.Field(discriminator="type"),
]
