

import typing

from .modeling_operation_action_artmesh_mirror_key_interpolation_four import (
    ModelingOperationActionArtmeshMirrorKeyInterpolationFour,
)
from .modeling_operation_action_artmesh_mirror_key_interpolation_one import (
    ModelingOperationActionArtmeshMirrorKeyInterpolationOne,
)
from .modeling_operation_action_artmesh_mirror_key_interpolation_three import (
    ModelingOperationActionArtmeshMirrorKeyInterpolationThree,
)
from .modeling_operation_action_artmesh_mirror_key_interpolation_two import (
    ModelingOperationActionArtmeshMirrorKeyInterpolationTwo,
)
from .modeling_operation_action_artmesh_mirror_key_interpolation_zero import (
    ModelingOperationActionArtmeshMirrorKeyInterpolationZero,
)

ModelingOperationActionArtmeshMirrorKeyInterpolation = typing.Union[
    ModelingOperationActionArtmeshMirrorKeyInterpolationZero,
    ModelingOperationActionArtmeshMirrorKeyInterpolationOne,
    ModelingOperationActionArtmeshMirrorKeyInterpolationTwo,
    ModelingOperationActionArtmeshMirrorKeyInterpolationThree,
    ModelingOperationActionArtmeshMirrorKeyInterpolationFour,
]
