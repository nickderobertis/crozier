

import typing

from .modeling_operation_action_artmesh_blend_shape_interpolation_four import (
    ModelingOperationActionArtmeshBlendShapeInterpolationFour,
)
from .modeling_operation_action_artmesh_blend_shape_interpolation_one import (
    ModelingOperationActionArtmeshBlendShapeInterpolationOne,
)
from .modeling_operation_action_artmesh_blend_shape_interpolation_three import (
    ModelingOperationActionArtmeshBlendShapeInterpolationThree,
)
from .modeling_operation_action_artmesh_blend_shape_interpolation_two import (
    ModelingOperationActionArtmeshBlendShapeInterpolationTwo,
)
from .modeling_operation_action_artmesh_blend_shape_interpolation_zero import (
    ModelingOperationActionArtmeshBlendShapeInterpolationZero,
)

ModelingOperationActionArtmeshBlendShapeInterpolation = typing.Union[
    ModelingOperationActionArtmeshBlendShapeInterpolationZero,
    ModelingOperationActionArtmeshBlendShapeInterpolationOne,
    ModelingOperationActionArtmeshBlendShapeInterpolationTwo,
    ModelingOperationActionArtmeshBlendShapeInterpolationThree,
    ModelingOperationActionArtmeshBlendShapeInterpolationFour,
]
