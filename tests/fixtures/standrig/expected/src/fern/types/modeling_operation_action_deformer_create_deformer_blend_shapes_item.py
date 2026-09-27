

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .modeling_operation_action_deformer_create_deformer_blend_shapes_item_curve import (
    ModelingOperationActionDeformerCreateDeformerBlendShapesItemCurve,
)
from .modeling_operation_action_deformer_create_deformer_blend_shapes_item_interpolation import (
    ModelingOperationActionDeformerCreateDeformerBlendShapesItemInterpolation,
)
from .modeling_operation_action_deformer_create_deformer_blend_shapes_item_kind import (
    ModelingOperationActionDeformerCreateDeformerBlendShapesItemKind,
)
from .modeling_operation_action_deformer_create_deformer_blend_shapes_item_pins_item import (
    ModelingOperationActionDeformerCreateDeformerBlendShapesItemPinsItem,
)
from .modeling_operation_action_deformer_create_deformer_blend_shapes_item_shared_points_item import (
    ModelingOperationActionDeformerCreateDeformerBlendShapesItemSharedPointsItem,
)
from .modeling_operation_action_deformer_create_deformer_blend_shapes_item_transform import (
    ModelingOperationActionDeformerCreateDeformerBlendShapesItemTransform,
)
from .modeling_operation_action_deformer_create_deformer_blend_shapes_item_warp import (
    ModelingOperationActionDeformerCreateDeformerBlendShapesItemWarp,
)


class ModelingOperationActionDeformerCreateDeformerBlendShapesItem(UniversalBaseModel):
    kind: ModelingOperationActionDeformerCreateDeformerBlendShapesItemKind
    transform: typing.Optional[ModelingOperationActionDeformerCreateDeformerBlendShapesItemTransform] = None
    warp: typing.Optional[ModelingOperationActionDeformerCreateDeformerBlendShapesItemWarp] = None
    pins: typing.Optional[typing.List[ModelingOperationActionDeformerCreateDeformerBlendShapesItemPinsItem]] = None
    shared_points: typing_extensions.Annotated[
        typing.Optional[typing.List[ModelingOperationActionDeformerCreateDeformerBlendShapesItemSharedPointsItem]],
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
    interpolation: typing.Optional[ModelingOperationActionDeformerCreateDeformerBlendShapesItemInterpolation] = None
    curve: typing.Optional[ModelingOperationActionDeformerCreateDeformerBlendShapesItemCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
