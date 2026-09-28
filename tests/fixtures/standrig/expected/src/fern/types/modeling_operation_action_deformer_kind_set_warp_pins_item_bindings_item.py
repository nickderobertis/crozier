

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .modeling_operation_action_deformer_kind_set_warp_pins_item_bindings_item_curve import (
    ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemCurve,
)
from .modeling_operation_action_deformer_kind_set_warp_pins_item_bindings_item_interpolation import (
    ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemInterpolation,
)
from .modeling_operation_action_deformer_kind_set_warp_pins_item_bindings_item_keys_item import (
    ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemKeysItem,
)
from .modeling_operation_action_deformer_kind_set_warp_pins_item_bindings_item_property import (
    ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemProperty,
)


class ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItem(UniversalBaseModel):
    parameter: str
    property: ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemProperty
    keys: typing.List[ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemKeysItem]
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemInterpolation] = None
    curve: typing.Optional[ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
