

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_curve import (
    ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemCurve,
)
from .modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_interpolation import (
    ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolation,
)
from .modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_keys_item import (
    ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemKeysItem,
)
from .modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_property import (
    ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemProperty,
)


class ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItem(UniversalBaseModel):
    parameter: str
    property: ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemProperty
    keys: typing.List[ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemKeysItem]
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[
        ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolation
    ] = None
    curve: typing.Optional[
        ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemCurve
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
