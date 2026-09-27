

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .modeling_operation_action_deform_brush_brush_surface_warp_pins_space import (
    ModelingOperationActionDeformBrushBrushSurfaceWarpPinsSpace,
)


class ModelingOperationActionDeformBrushBrushSurfaceWarpPins(UniversalBaseModel):
    space: ModelingOperationActionDeformBrushBrushSurfaceWarpPinsSpace
    width: float
    height: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
