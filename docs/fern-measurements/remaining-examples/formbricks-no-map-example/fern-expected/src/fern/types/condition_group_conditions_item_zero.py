

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .condition_group_conditions_item_zero_left_operand import ConditionGroupConditionsItemZeroLeftOperand
from .condition_group_conditions_item_zero_operator import ConditionGroupConditionsItemZeroOperator
from .condition_group_conditions_item_zero_right_operand import ConditionGroupConditionsItemZeroRightOperand


class ConditionGroupConditionsItemZero(UniversalBaseModel):
    id: str
    left_operand: typing_extensions.Annotated[
        ConditionGroupConditionsItemZeroLeftOperand,
        FieldMetadata(alias="leftOperand"),
        pydantic.Field(alias="leftOperand"),
    ]
    operator: ConditionGroupConditionsItemZeroOperator
    right_operand: typing_extensions.Annotated[
        typing.Optional[ConditionGroupConditionsItemZeroRightOperand],
        FieldMetadata(alias="rightOperand"),
        pydantic.Field(alias="rightOperand"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
