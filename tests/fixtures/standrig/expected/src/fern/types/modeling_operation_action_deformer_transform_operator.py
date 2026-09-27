

import typing

from .modeling_operation_action_deformer_transform_operator_one import (
    ModelingOperationActionDeformerTransformOperatorOne,
)
from .modeling_operation_action_deformer_transform_operator_two import (
    ModelingOperationActionDeformerTransformOperatorTwo,
)
from .modeling_operation_action_deformer_transform_operator_zero import (
    ModelingOperationActionDeformerTransformOperatorZero,
)

ModelingOperationActionDeformerTransformOperator = typing.Union[
    ModelingOperationActionDeformerTransformOperatorZero,
    ModelingOperationActionDeformerTransformOperatorOne,
    ModelingOperationActionDeformerTransformOperatorTwo,
]
