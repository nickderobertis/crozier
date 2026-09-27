

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .modeling_operation_action_deform_brush_brush_destination_blend_shape_shape_curve import (
    ModelingOperationActionDeformBrushBrushDestinationBlendShapeShapeCurve,
)
from .modeling_operation_action_deform_brush_brush_destination_blend_shape_shape_interpolation import (
    ModelingOperationActionDeformBrushBrushDestinationBlendShapeShapeInterpolation,
)


class ModelingOperationActionDeformBrushBrushDestinationBlendShapeShape(UniversalBaseModel):
    id: str
    parameter: str
    neutral_input: typing_extensions.Annotated[
        float, FieldMetadata(alias="neutralInput"), pydantic.Field(alias="neutralInput")
    ]
    target_input: typing_extensions.Annotated[
        float, FieldMetadata(alias="targetInput"), pydantic.Field(alias="targetInput")
    ]
    interpolation: typing.Optional[ModelingOperationActionDeformBrushBrushDestinationBlendShapeShapeInterpolation] = (
        None
    )
    curve: typing.Optional[ModelingOperationActionDeformBrushBrushDestinationBlendShapeShapeCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
