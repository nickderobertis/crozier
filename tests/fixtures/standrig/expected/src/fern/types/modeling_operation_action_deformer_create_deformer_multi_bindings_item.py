

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .modeling_operation_action_deformer_create_deformer_multi_bindings_item_composition import (
    ModelingOperationActionDeformerCreateDeformerMultiBindingsItemComposition,
)
from .modeling_operation_action_deformer_create_deformer_multi_bindings_item_curve import (
    ModelingOperationActionDeformerCreateDeformerMultiBindingsItemCurve,
)
from .modeling_operation_action_deformer_create_deformer_multi_bindings_item_interpolation import (
    ModelingOperationActionDeformerCreateDeformerMultiBindingsItemInterpolation,
)
from .modeling_operation_action_deformer_create_deformer_multi_bindings_item_keyforms_item import (
    ModelingOperationActionDeformerCreateDeformerMultiBindingsItemKeyformsItem,
)
from .modeling_operation_action_deformer_create_deformer_multi_bindings_item_property import (
    ModelingOperationActionDeformerCreateDeformerMultiBindingsItemProperty,
)


class ModelingOperationActionDeformerCreateDeformerMultiBindingsItem(UniversalBaseModel):
    parameters: typing.List[typing.Any]
    composition: typing.Optional[ModelingOperationActionDeformerCreateDeformerMultiBindingsItemComposition] = None
    property: ModelingOperationActionDeformerCreateDeformerMultiBindingsItemProperty
    keyforms: typing.List[ModelingOperationActionDeformerCreateDeformerMultiBindingsItemKeyformsItem]
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[ModelingOperationActionDeformerCreateDeformerMultiBindingsItemInterpolation] = None
    curve: typing.Optional[ModelingOperationActionDeformerCreateDeformerMultiBindingsItemCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
