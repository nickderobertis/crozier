

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .modeling_operation_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_curve import (
    ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemCurve,
)
from .modeling_operation_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_interpolation import (
    ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolation,
)
from .modeling_operation_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_keyforms_item import (
    ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemKeyformsItem,
)
from .modeling_operation_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_property import (
    ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemProperty,
)


class ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItem(UniversalBaseModel):
    parameters: typing.List[typing.Any]
    property: ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemProperty
    keyforms: typing.List[ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemKeyformsItem]
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[
        ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolation
    ] = None
    curve: typing.Optional[ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
