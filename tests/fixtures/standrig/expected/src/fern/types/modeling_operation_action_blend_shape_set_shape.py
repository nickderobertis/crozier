

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .modeling_operation_action_blend_shape_set_shape_art_path_curve import (
    ModelingOperationActionBlendShapeSetShapeArtPathCurve,
)
from .modeling_operation_action_blend_shape_set_shape_art_path_interpolation import (
    ModelingOperationActionBlendShapeSetShapeArtPathInterpolation,
)
from .modeling_operation_action_blend_shape_set_shape_art_path_points_item import (
    ModelingOperationActionBlendShapeSetShapeArtPathPointsItem,
)
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
from .modeling_operation_action_blend_shape_set_shape_glue_curve import (
    ModelingOperationActionBlendShapeSetShapeGlueCurve,
)
from .modeling_operation_action_blend_shape_set_shape_glue_interpolation import (
    ModelingOperationActionBlendShapeSetShapeGlueInterpolation,
)
from .modeling_operation_action_blend_shape_set_shape_part_curve import (
    ModelingOperationActionBlendShapeSetShapePartCurve,
)
from .modeling_operation_action_blend_shape_set_shape_part_interpolation import (
    ModelingOperationActionBlendShapeSetShapePartInterpolation,
)
from .modeling_operation_action_blend_shape_set_shape_part_transform import (
    ModelingOperationActionBlendShapeSetShapePartTransform,
)


class ModelingOperationActionBlendShapeSetShape_Part(UniversalBaseModel):
    kind: typing.Literal["part"] = "part"
    transform: ModelingOperationActionBlendShapeSetShapePartTransform
    id: str
    parameter: str
    neutral_input: typing_extensions.Annotated[
        float, FieldMetadata(alias="neutralInput"), pydantic.Field(alias="neutralInput")
    ]
    target_input: typing_extensions.Annotated[
        float, FieldMetadata(alias="targetInput"), pydantic.Field(alias="targetInput")
    ]
    interpolation: typing.Optional[ModelingOperationActionBlendShapeSetShapePartInterpolation] = None
    curve: typing.Optional[ModelingOperationActionBlendShapeSetShapePartCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationActionBlendShapeSetShape_Deformer(UniversalBaseModel):
    kind: typing.Literal["deformer"] = "deformer"
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


class ModelingOperationActionBlendShapeSetShape_ArtPath(UniversalBaseModel):
    kind: typing.Literal["art-path"] = "art-path"
    path_id: typing_extensions.Annotated[str, FieldMetadata(alias="pathId"), pydantic.Field(alias="pathId")]
    points: typing.Optional[typing.List[ModelingOperationActionBlendShapeSetShapeArtPathPointsItem]] = None
    width: typing.Optional[float] = None
    opacity: typing.Optional[float] = None
    id: str
    parameter: str
    neutral_input: typing_extensions.Annotated[
        float, FieldMetadata(alias="neutralInput"), pydantic.Field(alias="neutralInput")
    ]
    target_input: typing_extensions.Annotated[
        float, FieldMetadata(alias="targetInput"), pydantic.Field(alias="targetInput")
    ]
    interpolation: typing.Optional[ModelingOperationActionBlendShapeSetShapeArtPathInterpolation] = None
    curve: typing.Optional[ModelingOperationActionBlendShapeSetShapeArtPathCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationActionBlendShapeSetShape_Glue(UniversalBaseModel):
    kind: typing.Literal["glue"] = "glue"
    glue_id: typing_extensions.Annotated[str, FieldMetadata(alias="glueId"), pydantic.Field(alias="glueId")]
    strength: float
    id: str
    parameter: str
    neutral_input: typing_extensions.Annotated[
        float, FieldMetadata(alias="neutralInput"), pydantic.Field(alias="neutralInput")
    ]
    target_input: typing_extensions.Annotated[
        float, FieldMetadata(alias="targetInput"), pydantic.Field(alias="targetInput")
    ]
    interpolation: typing.Optional[ModelingOperationActionBlendShapeSetShapeGlueInterpolation] = None
    curve: typing.Optional[ModelingOperationActionBlendShapeSetShapeGlueCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ModelingOperationActionBlendShapeSetShape = typing_extensions.Annotated[
    typing.Union[
        ModelingOperationActionBlendShapeSetShape_Part,
        ModelingOperationActionBlendShapeSetShape_Deformer,
        ModelingOperationActionBlendShapeSetShape_ArtPath,
        ModelingOperationActionBlendShapeSetShape_Glue,
    ],
    pydantic.Field(discriminator="kind"),
]
