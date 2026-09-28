

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_multi_bindings_item_curve import (
    TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemCurve,
)
from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_multi_bindings_item_interpolation import (
    TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolation,
)
from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_multi_bindings_item_keyforms_item import (
    TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemKeyformsItem,
)
from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_multi_bindings_item_property import (
    TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemProperty,
)


class TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItem(UniversalBaseModel):
    parameters: typing.List[typing.Any]
    property: TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemProperty
    keyforms: typing.List[
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemKeyformsItem
    ]
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolation
    ] = None
    curve: typing.Optional[
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemCurve
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
