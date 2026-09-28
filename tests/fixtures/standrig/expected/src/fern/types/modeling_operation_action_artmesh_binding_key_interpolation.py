

import typing

from .modeling_operation_action_artmesh_binding_key_interpolation_four import (
    ModelingOperationActionArtmeshBindingKeyInterpolationFour,
)
from .modeling_operation_action_artmesh_binding_key_interpolation_one import (
    ModelingOperationActionArtmeshBindingKeyInterpolationOne,
)
from .modeling_operation_action_artmesh_binding_key_interpolation_three import (
    ModelingOperationActionArtmeshBindingKeyInterpolationThree,
)
from .modeling_operation_action_artmesh_binding_key_interpolation_two import (
    ModelingOperationActionArtmeshBindingKeyInterpolationTwo,
)
from .modeling_operation_action_artmesh_binding_key_interpolation_zero import (
    ModelingOperationActionArtmeshBindingKeyInterpolationZero,
)

ModelingOperationActionArtmeshBindingKeyInterpolation = typing.Union[
    ModelingOperationActionArtmeshBindingKeyInterpolationZero,
    ModelingOperationActionArtmeshBindingKeyInterpolationOne,
    ModelingOperationActionArtmeshBindingKeyInterpolationTwo,
    ModelingOperationActionArtmeshBindingKeyInterpolationThree,
    ModelingOperationActionArtmeshBindingKeyInterpolationFour,
]
