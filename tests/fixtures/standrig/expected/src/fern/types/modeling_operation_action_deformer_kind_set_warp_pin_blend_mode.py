

import typing

from .modeling_operation_action_deformer_kind_set_warp_pin_blend_mode_one import (
    ModelingOperationActionDeformerKindSetWarpPinBlendModeOne,
)
from .modeling_operation_action_deformer_kind_set_warp_pin_blend_mode_zero import (
    ModelingOperationActionDeformerKindSetWarpPinBlendModeZero,
)

ModelingOperationActionDeformerKindSetWarpPinBlendMode = typing.Union[
    ModelingOperationActionDeformerKindSetWarpPinBlendModeZero,
    ModelingOperationActionDeformerKindSetWarpPinBlendModeOne,
]
