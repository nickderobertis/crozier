

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .modeling_operation_action_artmesh_binding_key_curve import ModelingOperationActionArtmeshBindingKeyCurve
from .modeling_operation_action_artmesh_binding_key_interpolation import (
    ModelingOperationActionArtmeshBindingKeyInterpolation,
)
from .modeling_operation_action_artmesh_binding_key_offsets_item import (
    ModelingOperationActionArtmeshBindingKeyOffsetsItem,
)
from .modeling_operation_action_artmesh_blend_shape_curve import ModelingOperationActionArtmeshBlendShapeCurve
from .modeling_operation_action_artmesh_blend_shape_interpolation import (
    ModelingOperationActionArtmeshBlendShapeInterpolation,
)
from .modeling_operation_action_artmesh_blend_shape_offsets_item import (
    ModelingOperationActionArtmeshBlendShapeOffsetsItem,
)
from .modeling_operation_action_artmesh_generate_preset import ModelingOperationActionArtmeshGeneratePreset
from .modeling_operation_action_artmesh_generate_quality import ModelingOperationActionArtmeshGenerateQuality
from .modeling_operation_action_artmesh_generate_topology import ModelingOperationActionArtmeshGenerateTopology
from .modeling_operation_action_artmesh_mirror_key_curve import ModelingOperationActionArtmeshMirrorKeyCurve
from .modeling_operation_action_artmesh_mirror_key_interpolation import (
    ModelingOperationActionArtmeshMirrorKeyInterpolation,
)
from .modeling_operation_action_artmesh_multi_key_curve import ModelingOperationActionArtmeshMultiKeyCurve
from .modeling_operation_action_artmesh_multi_key_interpolation import (
    ModelingOperationActionArtmeshMultiKeyInterpolation,
)
from .modeling_operation_action_artmesh_multi_key_offsets_item import ModelingOperationActionArtmeshMultiKeyOffsetsItem
from .modeling_operation_action_artmesh_offset_uv import ModelingOperationActionArtmeshOffsetUv
from .modeling_operation_action_artmesh_quality_quality import ModelingOperationActionArtmeshQualityQuality
from .modeling_operation_action_artmesh_rebuild_preset import ModelingOperationActionArtmeshRebuildPreset
from .modeling_operation_action_artmesh_rebuild_quality import ModelingOperationActionArtmeshRebuildQuality
from .modeling_operation_action_artmesh_rebuild_topology import ModelingOperationActionArtmeshRebuildTopology
from .modeling_operation_action_binding_key_curve import ModelingOperationActionBindingKeyCurve
from .modeling_operation_action_binding_key_interpolation import ModelingOperationActionBindingKeyInterpolation
from .modeling_operation_action_binding_key_property import ModelingOperationActionBindingKeyProperty
from .modeling_operation_action_blend_shape_set_shape import ModelingOperationActionBlendShapeSetShape
from .modeling_operation_action_deform_brush_brush import ModelingOperationActionDeformBrushBrush
from .modeling_operation_action_deformer_binding_key_curve import ModelingOperationActionDeformerBindingKeyCurve
from .modeling_operation_action_deformer_binding_key_interpolation import (
    ModelingOperationActionDeformerBindingKeyInterpolation,
)
from .modeling_operation_action_deformer_binding_key_property import ModelingOperationActionDeformerBindingKeyProperty
from .modeling_operation_action_deformer_binding_remove_property import (
    ModelingOperationActionDeformerBindingRemoveProperty,
)
from .modeling_operation_action_deformer_create_deformer import ModelingOperationActionDeformerCreateDeformer
from .modeling_operation_action_deformer_kind_set_kind import ModelingOperationActionDeformerKindSetKind
from .modeling_operation_action_deformer_kind_set_warp import ModelingOperationActionDeformerKindSetWarp
from .modeling_operation_action_deformer_rotation_metadata_metadata import (
    ModelingOperationActionDeformerRotationMetadataMetadata,
)
from .modeling_operation_action_deformer_targets_set_mode import ModelingOperationActionDeformerTargetsSetMode
from .modeling_operation_action_deformer_transform_operator import ModelingOperationActionDeformerTransformOperator
from .modeling_operation_action_deformer_transform_property import ModelingOperationActionDeformerTransformProperty
from .modeling_operation_action_parameter_add_parameter import ModelingOperationActionParameterAddParameter
from .modeling_operation_action_part_alpha_reveal_reveal import ModelingOperationActionPartAlphaRevealReveal
from .modeling_operation_action_part_blend_mode_mode import ModelingOperationActionPartBlendModeMode
from .modeling_operation_action_part_clip_clip import ModelingOperationActionPartClipClip
from .modeling_operation_action_part_contour_shade_shade import ModelingOperationActionPartContourShadeShade
from .modeling_operation_action_part_tint_tint import ModelingOperationActionPartTintTint
from .modeling_operation_action_role_confirm_role import ModelingOperationActionRoleConfirmRole
from .modeling_operation_action_role_reclassify_expected_role import ModelingOperationActionRoleReclassifyExpectedRole
from .modeling_operation_action_role_reclassify_role import ModelingOperationActionRoleReclassifyRole
from .modeling_operation_action_symmetry_artmesh_bindings_links_item import (
    ModelingOperationActionSymmetryArtmeshBindingsLinksItem,
)
from .modeling_operation_action_symmetry_contract_contract import ModelingOperationActionSymmetryContractContract
from .modeling_operation_action_transform_operator import ModelingOperationActionTransformOperator
from .modeling_operation_action_transform_property import ModelingOperationActionTransformProperty
from .modeling_operation_action_warp_pin_binding_key_curve import ModelingOperationActionWarpPinBindingKeyCurve
from .modeling_operation_action_warp_pin_binding_key_interpolation import (
    ModelingOperationActionWarpPinBindingKeyInterpolation,
)
from .modeling_operation_action_warp_pin_binding_key_property import ModelingOperationActionWarpPinBindingKeyProperty


class ModelingOperationAction_BlendShapeSet(UniversalBaseModel):
    type: typing.Literal["blend-shape-set"] = "blend-shape-set"
    shape: ModelingOperationActionBlendShapeSetShape

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationAction_DeformBrush(UniversalBaseModel):
    type: typing.Literal["deform-brush"] = "deform-brush"
    brush: ModelingOperationActionDeformBrushBrush

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationAction_Transform(UniversalBaseModel):
    type: typing.Literal["transform"] = "transform"
    property: ModelingOperationActionTransformProperty
    operator: ModelingOperationActionTransformOperator
    value: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationAction_PartVisibility(UniversalBaseModel):
    type: typing.Literal["part-visibility"] = "part-visibility"
    visible: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationAction_PartDrawOrder(UniversalBaseModel):
    type: typing.Literal["part-draw-order"] = "part-draw-order"
    draw_order: typing_extensions.Annotated[float, FieldMetadata(alias="drawOrder"), pydantic.Field(alias="drawOrder")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationAction_PartBlendMode(UniversalBaseModel):
    type: typing.Literal["part-blend-mode"] = "part-blend-mode"
    mode: ModelingOperationActionPartBlendModeMode

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationAction_PartTint(UniversalBaseModel):
    type: typing.Literal["part-tint"] = "part-tint"
    tint: typing.Optional[ModelingOperationActionPartTintTint] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationAction_PartContourShade(UniversalBaseModel):
    type: typing.Literal["part-contour-shade"] = "part-contour-shade"
    shade: typing.Optional[ModelingOperationActionPartContourShadeShade] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationAction_PartAlphaReveal(UniversalBaseModel):
    type: typing.Literal["part-alpha-reveal"] = "part-alpha-reveal"
    reveal: typing.Optional[ModelingOperationActionPartAlphaRevealReveal] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationAction_PartClip(UniversalBaseModel):
    type: typing.Literal["part-clip"] = "part-clip"
    clip: typing.Optional[ModelingOperationActionPartClipClip] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationAction_RoleConfirm(UniversalBaseModel):
    type: typing.Literal["role-confirm"] = "role-confirm"
    role: ModelingOperationActionRoleConfirmRole

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationAction_RoleReclassify(UniversalBaseModel):
    type: typing.Literal["role-reclassify"] = "role-reclassify"
    expected_role: typing_extensions.Annotated[
        ModelingOperationActionRoleReclassifyExpectedRole,
        FieldMetadata(alias="expectedRole"),
        pydantic.Field(alias="expectedRole"),
    ]
    role: ModelingOperationActionRoleReclassifyRole
    reason: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationAction_ParameterAdd(UniversalBaseModel):
    type: typing.Literal["parameter-add"] = "parameter-add"
    parameter: ModelingOperationActionParameterAddParameter

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationAction_DeformerCreate(UniversalBaseModel):
    type: typing.Literal["deformer-create"] = "deformer-create"
    deformer: ModelingOperationActionDeformerCreateDeformer

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationAction_DeformerKindSet(UniversalBaseModel):
    type: typing.Literal["deformer-kind-set"] = "deformer-kind-set"
    deformer_id: typing_extensions.Annotated[str, FieldMetadata(alias="deformerId"), pydantic.Field(alias="deformerId")]
    kind: ModelingOperationActionDeformerKindSetKind
    warp: typing.Optional[ModelingOperationActionDeformerKindSetWarp] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationAction_DeformerTargetsSet(UniversalBaseModel):
    type: typing.Literal["deformer-targets-set"] = "deformer-targets-set"
    deformer_id: typing_extensions.Annotated[str, FieldMetadata(alias="deformerId"), pydantic.Field(alias="deformerId")]
    target_part_ids: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="targetPartIds"), pydantic.Field(alias="targetPartIds")
    ]
    mode: typing.Optional[ModelingOperationActionDeformerTargetsSetMode] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationAction_DeformerParentSet(UniversalBaseModel):
    type: typing.Literal["deformer-parent-set"] = "deformer-parent-set"
    deformer_id: typing_extensions.Annotated[str, FieldMetadata(alias="deformerId"), pydantic.Field(alias="deformerId")]
    parent_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="parentId"), pydantic.Field(alias="parentId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationAction_DeformerOrigin(UniversalBaseModel):
    type: typing.Literal["deformer-origin"] = "deformer-origin"
    deformer_id: typing_extensions.Annotated[str, FieldMetadata(alias="deformerId"), pydantic.Field(alias="deformerId")]
    x: float
    y: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationAction_DeformerTransform(UniversalBaseModel):
    type: typing.Literal["deformer-transform"] = "deformer-transform"
    deformer_id: typing_extensions.Annotated[str, FieldMetadata(alias="deformerId"), pydantic.Field(alias="deformerId")]
    property: ModelingOperationActionDeformerTransformProperty
    operator: ModelingOperationActionDeformerTransformOperator
    value: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationAction_ArtmeshOffset(UniversalBaseModel):
    type: typing.Literal["artmesh-offset"] = "artmesh-offset"
    x: float
    y: float
    uv: typing.Optional[ModelingOperationActionArtmeshOffsetUv] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationAction_ArtmeshBindingKey(UniversalBaseModel):
    type: typing.Literal["artmesh-binding-key"] = "artmesh-binding-key"
    parameter: str
    input: float
    offsets: typing.List[ModelingOperationActionArtmeshBindingKeyOffsetsItem]
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[ModelingOperationActionArtmeshBindingKeyInterpolation] = None
    curve: typing.Optional[ModelingOperationActionArtmeshBindingKeyCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationAction_ArtmeshMultiKey(UniversalBaseModel):
    type: typing.Literal["artmesh-multi-key"] = "artmesh-multi-key"
    parameters: typing.List[typing.Any]
    inputs: typing.Dict[str, float]
    offsets: typing.List[ModelingOperationActionArtmeshMultiKeyOffsetsItem]
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[ModelingOperationActionArtmeshMultiKeyInterpolation] = None
    curve: typing.Optional[ModelingOperationActionArtmeshMultiKeyCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationAction_ArtmeshBlendShape(UniversalBaseModel):
    type: typing.Literal["artmesh-blend-shape"] = "artmesh-blend-shape"
    id: str
    parameter: str
    neutral_input: typing_extensions.Annotated[
        float, FieldMetadata(alias="neutralInput"), pydantic.Field(alias="neutralInput")
    ]
    target_input: typing_extensions.Annotated[
        float, FieldMetadata(alias="targetInput"), pydantic.Field(alias="targetInput")
    ]
    offsets: typing.List[ModelingOperationActionArtmeshBlendShapeOffsetsItem]
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[ModelingOperationActionArtmeshBlendShapeInterpolation] = None
    curve: typing.Optional[ModelingOperationActionArtmeshBlendShapeCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationAction_ArtmeshMirrorKey(UniversalBaseModel):
    type: typing.Literal["artmesh-mirror-key"] = "artmesh-mirror-key"
    parameter: str
    source_input: typing_extensions.Annotated[
        float, FieldMetadata(alias="sourceInput"), pydantic.Field(alias="sourceInput")
    ]
    target_input: typing_extensions.Annotated[
        float, FieldMetadata(alias="targetInput"), pydantic.Field(alias="targetInput")
    ]
    axis_u: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="axisU"), pydantic.Field(alias="axisU")
    ] = None
    tolerance: typing.Optional[float] = None
    protect_vertex_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="protectVertexIds"),
        pydantic.Field(alias="protectVertexIds"),
    ] = None
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[ModelingOperationActionArtmeshMirrorKeyInterpolation] = None
    curve: typing.Optional[ModelingOperationActionArtmeshMirrorKeyCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationAction_ArtmeshGenerate(UniversalBaseModel):
    type: typing.Literal["artmesh-generate"] = "artmesh-generate"
    preset: ModelingOperationActionArtmeshGeneratePreset
    topology: typing.Optional[ModelingOperationActionArtmeshGenerateTopology] = None
    columns: float
    rows: float
    alpha_threshold: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="alphaThreshold"), pydantic.Field(alias="alphaThreshold")
    ] = None
    quality: typing.Optional[ModelingOperationActionArtmeshGenerateQuality] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationAction_ArtmeshRebuild(UniversalBaseModel):
    type: typing.Literal["artmesh-rebuild"] = "artmesh-rebuild"
    preset: ModelingOperationActionArtmeshRebuildPreset
    topology: typing.Optional[ModelingOperationActionArtmeshRebuildTopology] = None
    columns: float
    rows: float
    alpha_threshold: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="alphaThreshold"), pydantic.Field(alias="alphaThreshold")
    ] = None
    quality: typing.Optional[ModelingOperationActionArtmeshRebuildQuality] = None
    preserve_bindings: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="preserveBindings"), pydantic.Field(alias="preserveBindings")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationAction_ArtmeshQuality(UniversalBaseModel):
    type: typing.Literal["artmesh-quality"] = "artmesh-quality"
    quality: ModelingOperationActionArtmeshQualityQuality
    merge: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationAction_BindingKey(UniversalBaseModel):
    type: typing.Literal["binding-key"] = "binding-key"
    parameter: str
    property: ModelingOperationActionBindingKeyProperty
    input: float
    value: float
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[ModelingOperationActionBindingKeyInterpolation] = None
    curve: typing.Optional[ModelingOperationActionBindingKeyCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationAction_WarpPinBindingKey(UniversalBaseModel):
    type: typing.Literal["warp-pin-binding-key"] = "warp-pin-binding-key"
    deformer_id: typing_extensions.Annotated[str, FieldMetadata(alias="deformerId"), pydantic.Field(alias="deformerId")]
    pin_id: typing_extensions.Annotated[str, FieldMetadata(alias="pinId"), pydantic.Field(alias="pinId")]
    parameter: str
    property: ModelingOperationActionWarpPinBindingKeyProperty
    input: float
    value: float
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[ModelingOperationActionWarpPinBindingKeyInterpolation] = None
    curve: typing.Optional[ModelingOperationActionWarpPinBindingKeyCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationAction_DeformerBindingKey(UniversalBaseModel):
    type: typing.Literal["deformer-binding-key"] = "deformer-binding-key"
    deformer_id: typing_extensions.Annotated[str, FieldMetadata(alias="deformerId"), pydantic.Field(alias="deformerId")]
    parameter: str
    property: ModelingOperationActionDeformerBindingKeyProperty
    input: float
    value: float
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[ModelingOperationActionDeformerBindingKeyInterpolation] = None
    curve: typing.Optional[ModelingOperationActionDeformerBindingKeyCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationAction_DeformerBindingRemove(UniversalBaseModel):
    type: typing.Literal["deformer-binding-remove"] = "deformer-binding-remove"
    deformer_id: typing_extensions.Annotated[str, FieldMetadata(alias="deformerId"), pydantic.Field(alias="deformerId")]
    parameter: str
    property: ModelingOperationActionDeformerBindingRemoveProperty

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationAction_DeformerSplit(UniversalBaseModel):
    type: typing.Literal["deformer-split"] = "deformer-split"
    source_deformer_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="sourceDeformerId"), pydantic.Field(alias="sourceDeformerId")
    ]
    parent_deformer_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="parentDeformerId"), pydantic.Field(alias="parentDeformerId")
    ]
    move_parameter_ids: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="moveParameterIds"), pydantic.Field(alias="moveParameterIds")
    ]
    parent_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="parentName"), pydantic.Field(alias="parentName")
    ] = None
    expected_parent_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="expectedParentId"), pydantic.Field(alias="expectedParentId")
    ] = None
    parent_tags: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="parentTags"), pydantic.Field(alias="parentTags")
    ] = None
    source_tags: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="sourceTags"), pydantic.Field(alias="sourceTags")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationAction_DeformerRotationMetadata(UniversalBaseModel):
    type: typing.Literal["deformer-rotation-metadata"] = "deformer-rotation-metadata"
    deformer_id: typing_extensions.Annotated[str, FieldMetadata(alias="deformerId"), pydantic.Field(alias="deformerId")]
    metadata: ModelingOperationActionDeformerRotationMetadataMetadata

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationAction_SymmetryContract(UniversalBaseModel):
    type: typing.Literal["symmetry-contract"] = "symmetry-contract"
    contract: ModelingOperationActionSymmetryContractContract

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationAction_SymmetryArtmeshBindings(UniversalBaseModel):
    type: typing.Literal["symmetry-artmesh-bindings"] = "symmetry-artmesh-bindings"
    links: typing.List[ModelingOperationActionSymmetryArtmeshBindingsLinksItem]
    overwrite: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ModelingOperationAction = typing_extensions.Annotated[
    typing.Union[
        ModelingOperationAction_BlendShapeSet,
        ModelingOperationAction_DeformBrush,
        ModelingOperationAction_Transform,
        ModelingOperationAction_PartVisibility,
        ModelingOperationAction_PartDrawOrder,
        ModelingOperationAction_PartBlendMode,
        ModelingOperationAction_PartTint,
        ModelingOperationAction_PartContourShade,
        ModelingOperationAction_PartAlphaReveal,
        ModelingOperationAction_PartClip,
        ModelingOperationAction_RoleConfirm,
        ModelingOperationAction_RoleReclassify,
        ModelingOperationAction_ParameterAdd,
        ModelingOperationAction_DeformerCreate,
        ModelingOperationAction_DeformerKindSet,
        ModelingOperationAction_DeformerTargetsSet,
        ModelingOperationAction_DeformerParentSet,
        ModelingOperationAction_DeformerOrigin,
        ModelingOperationAction_DeformerTransform,
        ModelingOperationAction_ArtmeshOffset,
        ModelingOperationAction_ArtmeshBindingKey,
        ModelingOperationAction_ArtmeshMultiKey,
        ModelingOperationAction_ArtmeshBlendShape,
        ModelingOperationAction_ArtmeshMirrorKey,
        ModelingOperationAction_ArtmeshGenerate,
        ModelingOperationAction_ArtmeshRebuild,
        ModelingOperationAction_ArtmeshQuality,
        ModelingOperationAction_BindingKey,
        ModelingOperationAction_WarpPinBindingKey,
        ModelingOperationAction_DeformerBindingKey,
        ModelingOperationAction_DeformerBindingRemove,
        ModelingOperationAction_DeformerSplit,
        ModelingOperationAction_DeformerRotationMetadata,
        ModelingOperationAction_SymmetryContract,
        ModelingOperationAction_SymmetryArtmeshBindings,
    ],
    pydantic.Field(discriminator="type"),
]
