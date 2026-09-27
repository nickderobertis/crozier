

import typing

from .modeling_operation_action_warp_pin_binding_key_interpolation_four import (
    ModelingOperationActionWarpPinBindingKeyInterpolationFour,
)
from .modeling_operation_action_warp_pin_binding_key_interpolation_one import (
    ModelingOperationActionWarpPinBindingKeyInterpolationOne,
)
from .modeling_operation_action_warp_pin_binding_key_interpolation_three import (
    ModelingOperationActionWarpPinBindingKeyInterpolationThree,
)
from .modeling_operation_action_warp_pin_binding_key_interpolation_two import (
    ModelingOperationActionWarpPinBindingKeyInterpolationTwo,
)
from .modeling_operation_action_warp_pin_binding_key_interpolation_zero import (
    ModelingOperationActionWarpPinBindingKeyInterpolationZero,
)

ModelingOperationActionWarpPinBindingKeyInterpolation = typing.Union[
    ModelingOperationActionWarpPinBindingKeyInterpolationZero,
    ModelingOperationActionWarpPinBindingKeyInterpolationOne,
    ModelingOperationActionWarpPinBindingKeyInterpolationTwo,
    ModelingOperationActionWarpPinBindingKeyInterpolationThree,
    ModelingOperationActionWarpPinBindingKeyInterpolationFour,
]
