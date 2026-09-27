

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .modeling_operation_action_binding_key_curve import ModelingOperationActionBindingKeyCurve
from .modeling_operation_action_binding_key_interpolation import ModelingOperationActionBindingKeyInterpolation
from .modeling_operation_action_binding_key_property import ModelingOperationActionBindingKeyProperty


class ModelingOperationActionBindingKey(UniversalBaseModel):
    parameter: str
    property: ModelingOperationActionBindingKeyProperty
    input: float
    value: float
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[ModelingOperationActionBindingKeyInterpolation] = None
    curve: typing.Optional[ModelingOperationActionBindingKeyCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
