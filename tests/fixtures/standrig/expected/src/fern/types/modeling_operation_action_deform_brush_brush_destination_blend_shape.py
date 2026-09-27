

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .modeling_operation_action_deform_brush_brush_destination_blend_shape_shape import (
    ModelingOperationActionDeformBrushBrushDestinationBlendShapeShape,
)


class ModelingOperationActionDeformBrushBrushDestinationBlendShape(UniversalBaseModel):
    shape: ModelingOperationActionDeformBrushBrushDestinationBlendShapeShape

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
