

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .modeling_operation_action_blend_shape_set_shape_deformer_curve import (
    ModelingOperationActionBlendShapeSetShapeDeformerCurve,
)
from .modeling_operation_action_blend_shape_set_shape_deformer_interpolation import (
    ModelingOperationActionBlendShapeSetShapeDeformerInterpolation,
)
from .modeling_operation_action_blend_shape_set_shape_deformer_pins_item import (
    ModelingOperationActionBlendShapeSetShapeDeformerPinsItem,
)
from .modeling_operation_action_blend_shape_set_shape_deformer_shared_points_item import (
    ModelingOperationActionBlendShapeSetShapeDeformerSharedPointsItem,
)
from .modeling_operation_action_blend_shape_set_shape_deformer_transform import (
    ModelingOperationActionBlendShapeSetShapeDeformerTransform,
)
from .modeling_operation_action_blend_shape_set_shape_deformer_warp import (
    ModelingOperationActionBlendShapeSetShapeDeformerWarp,
)


class ModelingOperationActionBlendShapeSetShapeDeformer(UniversalBaseModel):
    transform: typing.Optional[ModelingOperationActionBlendShapeSetShapeDeformerTransform] = None
    warp: typing.Optional[ModelingOperationActionBlendShapeSetShapeDeformerWarp] = None
    pins: typing.Optional[typing.List[ModelingOperationActionBlendShapeSetShapeDeformerPinsItem]] = None
    shared_points: typing_extensions.Annotated[
        typing.Optional[typing.List[ModelingOperationActionBlendShapeSetShapeDeformerSharedPointsItem]],
        FieldMetadata(alias="sharedPoints"),
        pydantic.Field(alias="sharedPoints"),
    ] = None
    id: str
    parameter: str
    neutral_input: typing_extensions.Annotated[
        float, FieldMetadata(alias="neutralInput"), pydantic.Field(alias="neutralInput")
    ]
    target_input: typing_extensions.Annotated[
        float, FieldMetadata(alias="targetInput"), pydantic.Field(alias="targetInput")
    ]
    interpolation: typing.Optional[ModelingOperationActionBlendShapeSetShapeDeformerInterpolation] = None
    curve: typing.Optional[ModelingOperationActionBlendShapeSetShapeDeformerCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
