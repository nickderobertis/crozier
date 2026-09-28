

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .modeling_operation_action_deformer_create_deformer_shared_warp_bounds import (
    ModelingOperationActionDeformerCreateDeformerSharedWarpBounds,
)
from .modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item import (
    ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItem,
)
from .modeling_operation_action_deformer_create_deformer_shared_warp_grid import (
    ModelingOperationActionDeformerCreateDeformerSharedWarpGrid,
)


class ModelingOperationActionDeformerCreateDeformerSharedWarp(UniversalBaseModel):
    version: float
    enabled: bool
    bounds: ModelingOperationActionDeformerCreateDeformerSharedWarpBounds
    grid: ModelingOperationActionDeformerCreateDeformerSharedWarpGrid
    control_points: typing_extensions.Annotated[
        typing.List[ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItem],
        FieldMetadata(alias="controlPoints"),
        pydantic.Field(alias="controlPoints"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
