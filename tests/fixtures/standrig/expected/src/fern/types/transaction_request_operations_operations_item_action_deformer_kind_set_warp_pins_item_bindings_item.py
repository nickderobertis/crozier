

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_bindings_item_curve import (
    TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemCurve,
)
from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_bindings_item_interpolation import (
    TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemInterpolation,
)
from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_bindings_item_keys_item import (
    TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemKeysItem,
)
from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_bindings_item_property import (
    TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemProperty,
)


class TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItem(UniversalBaseModel):
    parameter: str
    property: TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemProperty
    keys: typing.List[TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemKeysItem]
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemInterpolation
    ] = None
    curve: typing.Optional[
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemCurve
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
