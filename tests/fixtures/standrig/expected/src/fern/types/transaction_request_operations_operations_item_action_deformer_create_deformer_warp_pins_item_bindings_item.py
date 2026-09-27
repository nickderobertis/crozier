

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_bindings_item_curve import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemCurve,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_bindings_item_interpolation import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolation,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_bindings_item_keys_item import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemKeysItem,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_bindings_item_property import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemProperty,
)


class TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItem(
    UniversalBaseModel
):
    parameter: str
    property: TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemProperty
    keys: typing.List[
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemKeysItem
    ]
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolation
    ] = None
    curve: typing.Optional[
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemCurve
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
