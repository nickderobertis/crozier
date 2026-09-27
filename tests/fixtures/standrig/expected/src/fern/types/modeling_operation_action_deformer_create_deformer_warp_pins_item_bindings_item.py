

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .modeling_operation_action_deformer_create_deformer_warp_pins_item_bindings_item_curve import (
    ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemCurve,
)
from .modeling_operation_action_deformer_create_deformer_warp_pins_item_bindings_item_interpolation import (
    ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolation,
)
from .modeling_operation_action_deformer_create_deformer_warp_pins_item_bindings_item_keys_item import (
    ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemKeysItem,
)
from .modeling_operation_action_deformer_create_deformer_warp_pins_item_bindings_item_property import (
    ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemProperty,
)


class ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItem(UniversalBaseModel):
    parameter: str
    property: ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemProperty
    keys: typing.List[ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemKeysItem]
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[
        ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolation
    ] = None
    curve: typing.Optional[ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
