

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .transaction_request_operations_operations_item_action_artmesh_binding_key_curve import (
    TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyCurve,
)
from .transaction_request_operations_operations_item_action_artmesh_binding_key_interpolation import (
    TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyInterpolation,
)
from .transaction_request_operations_operations_item_action_artmesh_binding_key_offsets_item import (
    TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyOffsetsItem,
)
from .transaction_request_operations_operations_item_action_artmesh_blend_shape_curve import (
    TransactionRequestOperationsOperationsItemActionArtmeshBlendShapeCurve,
)
from .transaction_request_operations_operations_item_action_artmesh_blend_shape_interpolation import (
    TransactionRequestOperationsOperationsItemActionArtmeshBlendShapeInterpolation,
)
from .transaction_request_operations_operations_item_action_artmesh_blend_shape_offsets_item import (
    TransactionRequestOperationsOperationsItemActionArtmeshBlendShapeOffsetsItem,
)
from .transaction_request_operations_operations_item_action_artmesh_generate_preset import (
    TransactionRequestOperationsOperationsItemActionArtmeshGeneratePreset,
)
from .transaction_request_operations_operations_item_action_artmesh_generate_quality import (
    TransactionRequestOperationsOperationsItemActionArtmeshGenerateQuality,
)
from .transaction_request_operations_operations_item_action_artmesh_generate_topology import (
    TransactionRequestOperationsOperationsItemActionArtmeshGenerateTopology,
)
from .transaction_request_operations_operations_item_action_artmesh_mirror_key_curve import (
    TransactionRequestOperationsOperationsItemActionArtmeshMirrorKeyCurve,
)
from .transaction_request_operations_operations_item_action_artmesh_mirror_key_interpolation import (
    TransactionRequestOperationsOperationsItemActionArtmeshMirrorKeyInterpolation,
)
from .transaction_request_operations_operations_item_action_artmesh_multi_key_curve import (
    TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyCurve,
)
from .transaction_request_operations_operations_item_action_artmesh_multi_key_interpolation import (
    TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyInterpolation,
)
from .transaction_request_operations_operations_item_action_artmesh_multi_key_offsets_item import (
    TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyOffsetsItem,
)
from .transaction_request_operations_operations_item_action_artmesh_offset_uv import (
    TransactionRequestOperationsOperationsItemActionArtmeshOffsetUv,
)
from .transaction_request_operations_operations_item_action_artmesh_quality_quality import (
    TransactionRequestOperationsOperationsItemActionArtmeshQualityQuality,
)
from .transaction_request_operations_operations_item_action_artmesh_rebuild_preset import (
    TransactionRequestOperationsOperationsItemActionArtmeshRebuildPreset,
)
from .transaction_request_operations_operations_item_action_artmesh_rebuild_quality import (
    TransactionRequestOperationsOperationsItemActionArtmeshRebuildQuality,
)
from .transaction_request_operations_operations_item_action_artmesh_rebuild_topology import (
    TransactionRequestOperationsOperationsItemActionArtmeshRebuildTopology,
)
from .transaction_request_operations_operations_item_action_binding_key_curve import (
    TransactionRequestOperationsOperationsItemActionBindingKeyCurve,
)
from .transaction_request_operations_operations_item_action_binding_key_interpolation import (
    TransactionRequestOperationsOperationsItemActionBindingKeyInterpolation,
)
from .transaction_request_operations_operations_item_action_binding_key_property import (
    TransactionRequestOperationsOperationsItemActionBindingKeyProperty,
)
from .transaction_request_operations_operations_item_action_blend_shape_set_shape import (
    TransactionRequestOperationsOperationsItemActionBlendShapeSetShape,
)
from .transaction_request_operations_operations_item_action_deform_brush_brush import (
    TransactionRequestOperationsOperationsItemActionDeformBrushBrush,
)
from .transaction_request_operations_operations_item_action_deformer_binding_key_curve import (
    TransactionRequestOperationsOperationsItemActionDeformerBindingKeyCurve,
)
from .transaction_request_operations_operations_item_action_deformer_binding_key_interpolation import (
    TransactionRequestOperationsOperationsItemActionDeformerBindingKeyInterpolation,
)
from .transaction_request_operations_operations_item_action_deformer_binding_key_property import (
    TransactionRequestOperationsOperationsItemActionDeformerBindingKeyProperty,
)
from .transaction_request_operations_operations_item_action_deformer_binding_remove_property import (
    TransactionRequestOperationsOperationsItemActionDeformerBindingRemoveProperty,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformer,
)
from .transaction_request_operations_operations_item_action_deformer_kind_set_kind import (
    TransactionRequestOperationsOperationsItemActionDeformerKindSetKind,
)
from .transaction_request_operations_operations_item_action_deformer_kind_set_warp import (
    TransactionRequestOperationsOperationsItemActionDeformerKindSetWarp,
)
from .transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata import (
    TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadata,
)
from .transaction_request_operations_operations_item_action_deformer_targets_set_mode import (
    TransactionRequestOperationsOperationsItemActionDeformerTargetsSetMode,
)
from .transaction_request_operations_operations_item_action_deformer_transform_operator import (
    TransactionRequestOperationsOperationsItemActionDeformerTransformOperator,
)
from .transaction_request_operations_operations_item_action_deformer_transform_property import (
    TransactionRequestOperationsOperationsItemActionDeformerTransformProperty,
)
from .transaction_request_operations_operations_item_action_parameter_add_parameter import (
    TransactionRequestOperationsOperationsItemActionParameterAddParameter,
)
from .transaction_request_operations_operations_item_action_part_alpha_reveal_reveal import (
    TransactionRequestOperationsOperationsItemActionPartAlphaRevealReveal,
)
from .transaction_request_operations_operations_item_action_part_blend_mode_mode import (
    TransactionRequestOperationsOperationsItemActionPartBlendModeMode,
)
from .transaction_request_operations_operations_item_action_part_clip_clip import (
    TransactionRequestOperationsOperationsItemActionPartClipClip,
)
from .transaction_request_operations_operations_item_action_part_contour_shade_shade import (
    TransactionRequestOperationsOperationsItemActionPartContourShadeShade,
)
from .transaction_request_operations_operations_item_action_part_tint_tint import (
    TransactionRequestOperationsOperationsItemActionPartTintTint,
)
from .transaction_request_operations_operations_item_action_role_confirm_role import (
    TransactionRequestOperationsOperationsItemActionRoleConfirmRole,
)
from .transaction_request_operations_operations_item_action_role_reclassify_expected_role import (
    TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRole,
)
from .transaction_request_operations_operations_item_action_role_reclassify_role import (
    TransactionRequestOperationsOperationsItemActionRoleReclassifyRole,
)
from .transaction_request_operations_operations_item_action_symmetry_artmesh_bindings_links_item import (
    TransactionRequestOperationsOperationsItemActionSymmetryArtmeshBindingsLinksItem,
)
from .transaction_request_operations_operations_item_action_symmetry_contract_contract import (
    TransactionRequestOperationsOperationsItemActionSymmetryContractContract,
)
from .transaction_request_operations_operations_item_action_transform_operator import (
    TransactionRequestOperationsOperationsItemActionTransformOperator,
)
from .transaction_request_operations_operations_item_action_transform_property import (
    TransactionRequestOperationsOperationsItemActionTransformProperty,
)
from .transaction_request_operations_operations_item_action_warp_pin_binding_key_curve import (
    TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyCurve,
)
from .transaction_request_operations_operations_item_action_warp_pin_binding_key_interpolation import (
    TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyInterpolation,
)
from .transaction_request_operations_operations_item_action_warp_pin_binding_key_property import (
    TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyProperty,
)


class TransactionRequestOperationsOperationsItemAction_BlendShapeSet(UniversalBaseModel):
    type: typing.Literal["blend-shape-set"] = "blend-shape-set"
    shape: TransactionRequestOperationsOperationsItemActionBlendShapeSetShape

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemAction_DeformBrush(UniversalBaseModel):
    type: typing.Literal["deform-brush"] = "deform-brush"
    brush: TransactionRequestOperationsOperationsItemActionDeformBrushBrush

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemAction_Transform(UniversalBaseModel):
    type: typing.Literal["transform"] = "transform"
    property: TransactionRequestOperationsOperationsItemActionTransformProperty
    operator: TransactionRequestOperationsOperationsItemActionTransformOperator
    value: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemAction_PartVisibility(UniversalBaseModel):
    type: typing.Literal["part-visibility"] = "part-visibility"
    visible: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemAction_PartDrawOrder(UniversalBaseModel):
    type: typing.Literal["part-draw-order"] = "part-draw-order"
    draw_order: typing_extensions.Annotated[float, FieldMetadata(alias="drawOrder"), pydantic.Field(alias="drawOrder")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemAction_PartBlendMode(UniversalBaseModel):
    type: typing.Literal["part-blend-mode"] = "part-blend-mode"
    mode: TransactionRequestOperationsOperationsItemActionPartBlendModeMode

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemAction_PartTint(UniversalBaseModel):
    type: typing.Literal["part-tint"] = "part-tint"
    tint: typing.Optional[TransactionRequestOperationsOperationsItemActionPartTintTint] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemAction_PartContourShade(UniversalBaseModel):
    type: typing.Literal["part-contour-shade"] = "part-contour-shade"
    shade: typing.Optional[TransactionRequestOperationsOperationsItemActionPartContourShadeShade] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemAction_PartAlphaReveal(UniversalBaseModel):
    type: typing.Literal["part-alpha-reveal"] = "part-alpha-reveal"
    reveal: typing.Optional[TransactionRequestOperationsOperationsItemActionPartAlphaRevealReveal] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemAction_PartClip(UniversalBaseModel):
    type: typing.Literal["part-clip"] = "part-clip"
    clip: typing.Optional[TransactionRequestOperationsOperationsItemActionPartClipClip] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemAction_RoleConfirm(UniversalBaseModel):
    type: typing.Literal["role-confirm"] = "role-confirm"
    role: TransactionRequestOperationsOperationsItemActionRoleConfirmRole

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemAction_RoleReclassify(UniversalBaseModel):
    type: typing.Literal["role-reclassify"] = "role-reclassify"
    expected_role: typing_extensions.Annotated[
        TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRole,
        FieldMetadata(alias="expectedRole"),
        pydantic.Field(alias="expectedRole"),
    ]
    role: TransactionRequestOperationsOperationsItemActionRoleReclassifyRole
    reason: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemAction_ParameterAdd(UniversalBaseModel):
    type: typing.Literal["parameter-add"] = "parameter-add"
    parameter: TransactionRequestOperationsOperationsItemActionParameterAddParameter

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemAction_DeformerCreate(UniversalBaseModel):
    type: typing.Literal["deformer-create"] = "deformer-create"
    deformer: TransactionRequestOperationsOperationsItemActionDeformerCreateDeformer

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemAction_DeformerKindSet(UniversalBaseModel):
    type: typing.Literal["deformer-kind-set"] = "deformer-kind-set"
    deformer_id: typing_extensions.Annotated[str, FieldMetadata(alias="deformerId"), pydantic.Field(alias="deformerId")]
    kind: TransactionRequestOperationsOperationsItemActionDeformerKindSetKind
    warp: typing.Optional[TransactionRequestOperationsOperationsItemActionDeformerKindSetWarp] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemAction_DeformerTargetsSet(UniversalBaseModel):
    type: typing.Literal["deformer-targets-set"] = "deformer-targets-set"
    deformer_id: typing_extensions.Annotated[str, FieldMetadata(alias="deformerId"), pydantic.Field(alias="deformerId")]
    target_part_ids: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="targetPartIds"), pydantic.Field(alias="targetPartIds")
    ]
    mode: typing.Optional[TransactionRequestOperationsOperationsItemActionDeformerTargetsSetMode] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemAction_DeformerParentSet(UniversalBaseModel):
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


class TransactionRequestOperationsOperationsItemAction_DeformerOrigin(UniversalBaseModel):
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


class TransactionRequestOperationsOperationsItemAction_DeformerTransform(UniversalBaseModel):
    type: typing.Literal["deformer-transform"] = "deformer-transform"
    deformer_id: typing_extensions.Annotated[str, FieldMetadata(alias="deformerId"), pydantic.Field(alias="deformerId")]
    property: TransactionRequestOperationsOperationsItemActionDeformerTransformProperty
    operator: TransactionRequestOperationsOperationsItemActionDeformerTransformOperator
    value: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemAction_ArtmeshOffset(UniversalBaseModel):
    type: typing.Literal["artmesh-offset"] = "artmesh-offset"
    x: float
    y: float
    uv: typing.Optional[TransactionRequestOperationsOperationsItemActionArtmeshOffsetUv] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemAction_ArtmeshBindingKey(UniversalBaseModel):
    type: typing.Literal["artmesh-binding-key"] = "artmesh-binding-key"
    parameter: str
    input: float
    offsets: typing.List[TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyOffsetsItem]
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyInterpolation] = (
        None
    )
    curve: typing.Optional[TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemAction_ArtmeshMultiKey(UniversalBaseModel):
    type: typing.Literal["artmesh-multi-key"] = "artmesh-multi-key"
    parameters: typing.List[typing.Any]
    inputs: typing.Dict[str, float]
    offsets: typing.List[TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyOffsetsItem]
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyInterpolation] = None
    curve: typing.Optional[TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemAction_ArtmeshBlendShape(UniversalBaseModel):
    type: typing.Literal["artmesh-blend-shape"] = "artmesh-blend-shape"
    id: str
    parameter: str
    neutral_input: typing_extensions.Annotated[
        float, FieldMetadata(alias="neutralInput"), pydantic.Field(alias="neutralInput")
    ]
    target_input: typing_extensions.Annotated[
        float, FieldMetadata(alias="targetInput"), pydantic.Field(alias="targetInput")
    ]
    offsets: typing.List[TransactionRequestOperationsOperationsItemActionArtmeshBlendShapeOffsetsItem]
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[TransactionRequestOperationsOperationsItemActionArtmeshBlendShapeInterpolation] = (
        None
    )
    curve: typing.Optional[TransactionRequestOperationsOperationsItemActionArtmeshBlendShapeCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemAction_ArtmeshMirrorKey(UniversalBaseModel):
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
    interpolation: typing.Optional[TransactionRequestOperationsOperationsItemActionArtmeshMirrorKeyInterpolation] = None
    curve: typing.Optional[TransactionRequestOperationsOperationsItemActionArtmeshMirrorKeyCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemAction_ArtmeshGenerate(UniversalBaseModel):
    type: typing.Literal["artmesh-generate"] = "artmesh-generate"
    preset: TransactionRequestOperationsOperationsItemActionArtmeshGeneratePreset
    topology: typing.Optional[TransactionRequestOperationsOperationsItemActionArtmeshGenerateTopology] = None
    columns: float
    rows: float
    alpha_threshold: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="alphaThreshold"), pydantic.Field(alias="alphaThreshold")
    ] = None
    quality: typing.Optional[TransactionRequestOperationsOperationsItemActionArtmeshGenerateQuality] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemAction_ArtmeshRebuild(UniversalBaseModel):
    type: typing.Literal["artmesh-rebuild"] = "artmesh-rebuild"
    preset: TransactionRequestOperationsOperationsItemActionArtmeshRebuildPreset
    topology: typing.Optional[TransactionRequestOperationsOperationsItemActionArtmeshRebuildTopology] = None
    columns: float
    rows: float
    alpha_threshold: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="alphaThreshold"), pydantic.Field(alias="alphaThreshold")
    ] = None
    quality: typing.Optional[TransactionRequestOperationsOperationsItemActionArtmeshRebuildQuality] = None
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


class TransactionRequestOperationsOperationsItemAction_ArtmeshQuality(UniversalBaseModel):
    type: typing.Literal["artmesh-quality"] = "artmesh-quality"
    quality: TransactionRequestOperationsOperationsItemActionArtmeshQualityQuality
    merge: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemAction_BindingKey(UniversalBaseModel):
    type: typing.Literal["binding-key"] = "binding-key"
    parameter: str
    property: TransactionRequestOperationsOperationsItemActionBindingKeyProperty
    input: float
    value: float
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[TransactionRequestOperationsOperationsItemActionBindingKeyInterpolation] = None
    curve: typing.Optional[TransactionRequestOperationsOperationsItemActionBindingKeyCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemAction_WarpPinBindingKey(UniversalBaseModel):
    type: typing.Literal["warp-pin-binding-key"] = "warp-pin-binding-key"
    deformer_id: typing_extensions.Annotated[str, FieldMetadata(alias="deformerId"), pydantic.Field(alias="deformerId")]
    pin_id: typing_extensions.Annotated[str, FieldMetadata(alias="pinId"), pydantic.Field(alias="pinId")]
    parameter: str
    property: TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyProperty
    input: float
    value: float
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyInterpolation] = (
        None
    )
    curve: typing.Optional[TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemAction_DeformerBindingKey(UniversalBaseModel):
    type: typing.Literal["deformer-binding-key"] = "deformer-binding-key"
    deformer_id: typing_extensions.Annotated[str, FieldMetadata(alias="deformerId"), pydantic.Field(alias="deformerId")]
    parameter: str
    property: TransactionRequestOperationsOperationsItemActionDeformerBindingKeyProperty
    input: float
    value: float
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[TransactionRequestOperationsOperationsItemActionDeformerBindingKeyInterpolation] = (
        None
    )
    curve: typing.Optional[TransactionRequestOperationsOperationsItemActionDeformerBindingKeyCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemAction_DeformerBindingRemove(UniversalBaseModel):
    type: typing.Literal["deformer-binding-remove"] = "deformer-binding-remove"
    deformer_id: typing_extensions.Annotated[str, FieldMetadata(alias="deformerId"), pydantic.Field(alias="deformerId")]
    parameter: str
    property: TransactionRequestOperationsOperationsItemActionDeformerBindingRemoveProperty

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemAction_DeformerSplit(UniversalBaseModel):
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


class TransactionRequestOperationsOperationsItemAction_DeformerRotationMetadata(UniversalBaseModel):
    type: typing.Literal["deformer-rotation-metadata"] = "deformer-rotation-metadata"
    deformer_id: typing_extensions.Annotated[str, FieldMetadata(alias="deformerId"), pydantic.Field(alias="deformerId")]
    metadata: TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadata

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemAction_SymmetryContract(UniversalBaseModel):
    type: typing.Literal["symmetry-contract"] = "symmetry-contract"
    contract: TransactionRequestOperationsOperationsItemActionSymmetryContractContract

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemAction_SymmetryArtmeshBindings(UniversalBaseModel):
    type: typing.Literal["symmetry-artmesh-bindings"] = "symmetry-artmesh-bindings"
    links: typing.List[TransactionRequestOperationsOperationsItemActionSymmetryArtmeshBindingsLinksItem]
    overwrite: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


TransactionRequestOperationsOperationsItemAction = typing_extensions.Annotated[
    typing.Union[
        TransactionRequestOperationsOperationsItemAction_BlendShapeSet,
        TransactionRequestOperationsOperationsItemAction_DeformBrush,
        TransactionRequestOperationsOperationsItemAction_Transform,
        TransactionRequestOperationsOperationsItemAction_PartVisibility,
        TransactionRequestOperationsOperationsItemAction_PartDrawOrder,
        TransactionRequestOperationsOperationsItemAction_PartBlendMode,
        TransactionRequestOperationsOperationsItemAction_PartTint,
        TransactionRequestOperationsOperationsItemAction_PartContourShade,
        TransactionRequestOperationsOperationsItemAction_PartAlphaReveal,
        TransactionRequestOperationsOperationsItemAction_PartClip,
        TransactionRequestOperationsOperationsItemAction_RoleConfirm,
        TransactionRequestOperationsOperationsItemAction_RoleReclassify,
        TransactionRequestOperationsOperationsItemAction_ParameterAdd,
        TransactionRequestOperationsOperationsItemAction_DeformerCreate,
        TransactionRequestOperationsOperationsItemAction_DeformerKindSet,
        TransactionRequestOperationsOperationsItemAction_DeformerTargetsSet,
        TransactionRequestOperationsOperationsItemAction_DeformerParentSet,
        TransactionRequestOperationsOperationsItemAction_DeformerOrigin,
        TransactionRequestOperationsOperationsItemAction_DeformerTransform,
        TransactionRequestOperationsOperationsItemAction_ArtmeshOffset,
        TransactionRequestOperationsOperationsItemAction_ArtmeshBindingKey,
        TransactionRequestOperationsOperationsItemAction_ArtmeshMultiKey,
        TransactionRequestOperationsOperationsItemAction_ArtmeshBlendShape,
        TransactionRequestOperationsOperationsItemAction_ArtmeshMirrorKey,
        TransactionRequestOperationsOperationsItemAction_ArtmeshGenerate,
        TransactionRequestOperationsOperationsItemAction_ArtmeshRebuild,
        TransactionRequestOperationsOperationsItemAction_ArtmeshQuality,
        TransactionRequestOperationsOperationsItemAction_BindingKey,
        TransactionRequestOperationsOperationsItemAction_WarpPinBindingKey,
        TransactionRequestOperationsOperationsItemAction_DeformerBindingKey,
        TransactionRequestOperationsOperationsItemAction_DeformerBindingRemove,
        TransactionRequestOperationsOperationsItemAction_DeformerSplit,
        TransactionRequestOperationsOperationsItemAction_DeformerRotationMetadata,
        TransactionRequestOperationsOperationsItemAction_SymmetryContract,
        TransactionRequestOperationsOperationsItemAction_SymmetryArtmeshBindings,
    ],
    pydantic.Field(discriminator="type"),
]
