

import typing

from .modeling_operation_action_warp_pin_binding_key_property_one import (
    ModelingOperationActionWarpPinBindingKeyPropertyOne,
)
from .modeling_operation_action_warp_pin_binding_key_property_zero import (
    ModelingOperationActionWarpPinBindingKeyPropertyZero,
)

ModelingOperationActionWarpPinBindingKeyProperty = typing.Union[
    ModelingOperationActionWarpPinBindingKeyPropertyZero, ModelingOperationActionWarpPinBindingKeyPropertyOne
]
