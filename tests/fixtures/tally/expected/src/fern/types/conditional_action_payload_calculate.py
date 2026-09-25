

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .conditional_action_payload_calculate_operator import ConditionalActionPayloadCalculateOperator
from .conditional_action_payload_calculate_value import ConditionalActionPayloadCalculateValue
from .field import Field


class ConditionalActionPayloadCalculate(UniversalBaseModel):
    """
    Calculation to apply when condition matches.
    """

    field: Field
    operator: ConditionalActionPayloadCalculateOperator = pydantic.Field()
    """
    Math or assignment operator.
    """

    value: ConditionalActionPayloadCalculateValue = pydantic.Field()
    """
    Value or field reference used in the calculation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
