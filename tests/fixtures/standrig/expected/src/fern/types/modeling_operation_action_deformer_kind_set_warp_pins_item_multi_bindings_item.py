

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .modeling_operation_action_deformer_kind_set_warp_pins_item_multi_bindings_item_curve import (
    ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemCurve,
)
from .modeling_operation_action_deformer_kind_set_warp_pins_item_multi_bindings_item_interpolation import (
    ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolation,
)
from .modeling_operation_action_deformer_kind_set_warp_pins_item_multi_bindings_item_keyforms_item import (
    ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemKeyformsItem,
)
from .modeling_operation_action_deformer_kind_set_warp_pins_item_multi_bindings_item_property import (
    ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemProperty,
)


class ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItem(UniversalBaseModel):
    parameters: typing.List[typing.Any]
    property: ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemProperty
    keyforms: typing.List[ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemKeyformsItem]
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolation] = (
        None
    )
    curve: typing.Optional[ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
