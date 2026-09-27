

import typing

from .modeling_operation_action_artmesh_multi_key_interpolation_four import (
    ModelingOperationActionArtmeshMultiKeyInterpolationFour,
)
from .modeling_operation_action_artmesh_multi_key_interpolation_one import (
    ModelingOperationActionArtmeshMultiKeyInterpolationOne,
)
from .modeling_operation_action_artmesh_multi_key_interpolation_three import (
    ModelingOperationActionArtmeshMultiKeyInterpolationThree,
)
from .modeling_operation_action_artmesh_multi_key_interpolation_two import (
    ModelingOperationActionArtmeshMultiKeyInterpolationTwo,
)
from .modeling_operation_action_artmesh_multi_key_interpolation_zero import (
    ModelingOperationActionArtmeshMultiKeyInterpolationZero,
)

ModelingOperationActionArtmeshMultiKeyInterpolation = typing.Union[
    ModelingOperationActionArtmeshMultiKeyInterpolationZero,
    ModelingOperationActionArtmeshMultiKeyInterpolationOne,
    ModelingOperationActionArtmeshMultiKeyInterpolationTwo,
    ModelingOperationActionArtmeshMultiKeyInterpolationThree,
    ModelingOperationActionArtmeshMultiKeyInterpolationFour,
]
