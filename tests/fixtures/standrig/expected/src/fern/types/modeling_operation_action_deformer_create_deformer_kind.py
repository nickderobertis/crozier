

import typing

from .modeling_operation_action_deformer_create_deformer_kind_one import (
    ModelingOperationActionDeformerCreateDeformerKindOne,
)
from .modeling_operation_action_deformer_create_deformer_kind_two import (
    ModelingOperationActionDeformerCreateDeformerKindTwo,
)
from .modeling_operation_action_deformer_create_deformer_kind_zero import (
    ModelingOperationActionDeformerCreateDeformerKindZero,
)

ModelingOperationActionDeformerCreateDeformerKind = typing.Union[
    ModelingOperationActionDeformerCreateDeformerKindZero,
    ModelingOperationActionDeformerCreateDeformerKindOne,
    ModelingOperationActionDeformerCreateDeformerKindTwo,
]
