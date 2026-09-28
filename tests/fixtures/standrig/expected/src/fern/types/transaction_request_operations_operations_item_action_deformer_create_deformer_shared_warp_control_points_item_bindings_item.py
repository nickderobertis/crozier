

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_curve import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemCurve,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_interpolation import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolation,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_keys_item import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemKeysItem,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_property import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemProperty,
)


class TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItem(
    UniversalBaseModel
):
    parameter: str
    property: TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemProperty
    keys: typing.List[
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemKeysItem
    ]
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolation
    ] = None
    curve: typing.Optional[
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemCurve
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
