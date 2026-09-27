

import typing

from .modeling_operation_action_deformer_transform_property_five import (
    ModelingOperationActionDeformerTransformPropertyFive,
)
from .modeling_operation_action_deformer_transform_property_four import (
    ModelingOperationActionDeformerTransformPropertyFour,
)
from .modeling_operation_action_deformer_transform_property_one import (
    ModelingOperationActionDeformerTransformPropertyOne,
)
from .modeling_operation_action_deformer_transform_property_three import (
    ModelingOperationActionDeformerTransformPropertyThree,
)
from .modeling_operation_action_deformer_transform_property_two import (
    ModelingOperationActionDeformerTransformPropertyTwo,
)
from .modeling_operation_action_deformer_transform_property_zero import (
    ModelingOperationActionDeformerTransformPropertyZero,
)

ModelingOperationActionDeformerTransformProperty = typing.Union[
    ModelingOperationActionDeformerTransformPropertyZero,
    ModelingOperationActionDeformerTransformPropertyOne,
    ModelingOperationActionDeformerTransformPropertyTwo,
    ModelingOperationActionDeformerTransformPropertyThree,
    ModelingOperationActionDeformerTransformPropertyFour,
    ModelingOperationActionDeformerTransformPropertyFive,
]
