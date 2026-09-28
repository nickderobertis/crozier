

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .modeling_operation_action_deformer_create_deformer_bindings_item_composition import (
    ModelingOperationActionDeformerCreateDeformerBindingsItemComposition,
)
from .modeling_operation_action_deformer_create_deformer_bindings_item_curve import (
    ModelingOperationActionDeformerCreateDeformerBindingsItemCurve,
)
from .modeling_operation_action_deformer_create_deformer_bindings_item_interpolation import (
    ModelingOperationActionDeformerCreateDeformerBindingsItemInterpolation,
)
from .modeling_operation_action_deformer_create_deformer_bindings_item_keys_item import (
    ModelingOperationActionDeformerCreateDeformerBindingsItemKeysItem,
)
from .modeling_operation_action_deformer_create_deformer_bindings_item_property import (
    ModelingOperationActionDeformerCreateDeformerBindingsItemProperty,
)


class ModelingOperationActionDeformerCreateDeformerBindingsItem(UniversalBaseModel):
    parameter: str
    property: ModelingOperationActionDeformerCreateDeformerBindingsItemProperty
    keys: typing.List[ModelingOperationActionDeformerCreateDeformerBindingsItemKeysItem]
    additive: typing.Optional[bool] = None
    composition: typing.Optional[ModelingOperationActionDeformerCreateDeformerBindingsItemComposition] = None
    interpolation: typing.Optional[ModelingOperationActionDeformerCreateDeformerBindingsItemInterpolation] = None
    curve: typing.Optional[ModelingOperationActionDeformerCreateDeformerBindingsItemCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
