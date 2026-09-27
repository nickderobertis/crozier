

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .modeling_operation_action_deformer_binding_key_curve import ModelingOperationActionDeformerBindingKeyCurve
from .modeling_operation_action_deformer_binding_key_interpolation import (
    ModelingOperationActionDeformerBindingKeyInterpolation,
)
from .modeling_operation_action_deformer_binding_key_property import ModelingOperationActionDeformerBindingKeyProperty


class ModelingOperationActionDeformerBindingKey(UniversalBaseModel):
    deformer_id: typing_extensions.Annotated[str, FieldMetadata(alias="deformerId"), pydantic.Field(alias="deformerId")]
    parameter: str
    property: ModelingOperationActionDeformerBindingKeyProperty
    input: float
    value: float
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[ModelingOperationActionDeformerBindingKeyInterpolation] = None
    curve: typing.Optional[ModelingOperationActionDeformerBindingKeyCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
