

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .variable_value import VariableValue
from .variable_values_notification_op import VariableValuesNotificationOp


class VariableValuesNotification(UniversalBaseModel):
    """
    Current variable values.

        Attributes:
            variables: Variables with current values and types.
    """

    op: VariableValuesNotificationOp
    variables: typing.List[VariableValue]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
