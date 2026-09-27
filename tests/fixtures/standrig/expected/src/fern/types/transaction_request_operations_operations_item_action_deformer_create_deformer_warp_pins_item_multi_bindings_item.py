

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_curve import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemCurve,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_interpolation import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolation,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_keyforms_item import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemKeyformsItem,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_property import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemProperty,
)


class TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItem(
    UniversalBaseModel
):
    parameters: typing.List[typing.Any]
    property: (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemProperty
    )
    keyforms: typing.List[
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemKeyformsItem
    ]
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolation
    ] = None
    curve: typing.Optional[
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemCurve
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
