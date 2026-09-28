



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_api_playback_motion_response import GetApiPlaybackMotionResponse
    from .get_api_playback_motion_response_playback import GetApiPlaybackMotionResponsePlayback
    from .get_api_playback_motion_response_playback_demo import GetApiPlaybackMotionResponsePlaybackDemo
    from .get_api_playback_motion_response_playback_demo_mode import GetApiPlaybackMotionResponsePlaybackDemoMode
    from .get_api_playback_motion_response_playback_motion import GetApiPlaybackMotionResponsePlaybackMotion
    from .get_api_playback_response import GetApiPlaybackResponse
    from .get_api_playback_response_playback import GetApiPlaybackResponsePlayback
    from .get_api_playback_response_playback_demo import GetApiPlaybackResponsePlaybackDemo
    from .get_api_playback_response_playback_demo_mode import GetApiPlaybackResponsePlaybackDemoMode
    from .get_api_playback_response_playback_motion import GetApiPlaybackResponsePlaybackMotion
    from .modeling_operation import ModelingOperation
    from .modeling_operation_action import (
        ModelingOperationAction,
        ModelingOperationAction_ArtmeshBindingKey,
        ModelingOperationAction_ArtmeshBlendShape,
        ModelingOperationAction_ArtmeshGenerate,
        ModelingOperationAction_ArtmeshMirrorKey,
        ModelingOperationAction_ArtmeshMultiKey,
        ModelingOperationAction_ArtmeshOffset,
        ModelingOperationAction_ArtmeshQuality,
        ModelingOperationAction_ArtmeshRebuild,
        ModelingOperationAction_BindingKey,
        ModelingOperationAction_BlendShapeSet,
        ModelingOperationAction_DeformBrush,
        ModelingOperationAction_DeformerBindingKey,
        ModelingOperationAction_DeformerBindingRemove,
        ModelingOperationAction_DeformerCreate,
        ModelingOperationAction_DeformerKindSet,
        ModelingOperationAction_DeformerOrigin,
        ModelingOperationAction_DeformerParentSet,
        ModelingOperationAction_DeformerRotationMetadata,
        ModelingOperationAction_DeformerSplit,
        ModelingOperationAction_DeformerTargetsSet,
        ModelingOperationAction_DeformerTransform,
        ModelingOperationAction_ParameterAdd,
        ModelingOperationAction_PartAlphaReveal,
        ModelingOperationAction_PartBlendMode,
        ModelingOperationAction_PartClip,
        ModelingOperationAction_PartContourShade,
        ModelingOperationAction_PartDrawOrder,
        ModelingOperationAction_PartTint,
        ModelingOperationAction_PartVisibility,
        ModelingOperationAction_RoleConfirm,
        ModelingOperationAction_RoleReclassify,
        ModelingOperationAction_SymmetryArtmeshBindings,
        ModelingOperationAction_SymmetryContract,
        ModelingOperationAction_Transform,
        ModelingOperationAction_WarpPinBindingKey,
    )
    from .modeling_operation_action_artmesh_binding_key import ModelingOperationActionArtmeshBindingKey
    from .modeling_operation_action_artmesh_binding_key_curve import ModelingOperationActionArtmeshBindingKeyCurve
    from .modeling_operation_action_artmesh_binding_key_curve_control_points_item import (
        ModelingOperationActionArtmeshBindingKeyCurveControlPointsItem,
    )
    from .modeling_operation_action_artmesh_binding_key_interpolation import (
        ModelingOperationActionArtmeshBindingKeyInterpolation,
    )
    from .modeling_operation_action_artmesh_binding_key_interpolation_four import (
        ModelingOperationActionArtmeshBindingKeyInterpolationFour,
    )
    from .modeling_operation_action_artmesh_binding_key_interpolation_one import (
        ModelingOperationActionArtmeshBindingKeyInterpolationOne,
    )
    from .modeling_operation_action_artmesh_binding_key_interpolation_three import (
        ModelingOperationActionArtmeshBindingKeyInterpolationThree,
    )
    from .modeling_operation_action_artmesh_binding_key_interpolation_two import (
        ModelingOperationActionArtmeshBindingKeyInterpolationTwo,
    )
    from .modeling_operation_action_artmesh_binding_key_interpolation_zero import (
        ModelingOperationActionArtmeshBindingKeyInterpolationZero,
    )
    from .modeling_operation_action_artmesh_binding_key_offsets_item import (
        ModelingOperationActionArtmeshBindingKeyOffsetsItem,
    )
    from .modeling_operation_action_artmesh_blend_shape import ModelingOperationActionArtmeshBlendShape
    from .modeling_operation_action_artmesh_blend_shape_curve import ModelingOperationActionArtmeshBlendShapeCurve
    from .modeling_operation_action_artmesh_blend_shape_curve_control_points_item import (
        ModelingOperationActionArtmeshBlendShapeCurveControlPointsItem,
    )
    from .modeling_operation_action_artmesh_blend_shape_interpolation import (
        ModelingOperationActionArtmeshBlendShapeInterpolation,
    )
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
    from .modeling_operation_action_artmesh_blend_shape_offsets_item import (
        ModelingOperationActionArtmeshBlendShapeOffsetsItem,
    )
    from .modeling_operation_action_artmesh_generate import ModelingOperationActionArtmeshGenerate
    from .modeling_operation_action_artmesh_generate_preset import ModelingOperationActionArtmeshGeneratePreset
    from .modeling_operation_action_artmesh_generate_preset_five import ModelingOperationActionArtmeshGeneratePresetFive
    from .modeling_operation_action_artmesh_generate_preset_four import ModelingOperationActionArtmeshGeneratePresetFour
    from .modeling_operation_action_artmesh_generate_preset_one import ModelingOperationActionArtmeshGeneratePresetOne
    from .modeling_operation_action_artmesh_generate_preset_three import (
        ModelingOperationActionArtmeshGeneratePresetThree,
    )
    from .modeling_operation_action_artmesh_generate_preset_two import ModelingOperationActionArtmeshGeneratePresetTwo
    from .modeling_operation_action_artmesh_generate_preset_zero import ModelingOperationActionArtmeshGeneratePresetZero
    from .modeling_operation_action_artmesh_generate_quality import ModelingOperationActionArtmeshGenerateQuality
    from .modeling_operation_action_artmesh_generate_topology import ModelingOperationActionArtmeshGenerateTopology
    from .modeling_operation_action_artmesh_generate_topology_one import (
        ModelingOperationActionArtmeshGenerateTopologyOne,
    )
    from .modeling_operation_action_artmesh_generate_topology_zero import (
        ModelingOperationActionArtmeshGenerateTopologyZero,
    )
    from .modeling_operation_action_artmesh_mirror_key import ModelingOperationActionArtmeshMirrorKey
    from .modeling_operation_action_artmesh_mirror_key_curve import ModelingOperationActionArtmeshMirrorKeyCurve
    from .modeling_operation_action_artmesh_mirror_key_curve_control_points_item import (
        ModelingOperationActionArtmeshMirrorKeyCurveControlPointsItem,
    )
    from .modeling_operation_action_artmesh_mirror_key_interpolation import (
        ModelingOperationActionArtmeshMirrorKeyInterpolation,
    )
    from .modeling_operation_action_artmesh_mirror_key_interpolation_four import (
        ModelingOperationActionArtmeshMirrorKeyInterpolationFour,
    )
    from .modeling_operation_action_artmesh_mirror_key_interpolation_one import (
        ModelingOperationActionArtmeshMirrorKeyInterpolationOne,
    )
    from .modeling_operation_action_artmesh_mirror_key_interpolation_three import (
        ModelingOperationActionArtmeshMirrorKeyInterpolationThree,
    )
    from .modeling_operation_action_artmesh_mirror_key_interpolation_two import (
        ModelingOperationActionArtmeshMirrorKeyInterpolationTwo,
    )
    from .modeling_operation_action_artmesh_mirror_key_interpolation_zero import (
        ModelingOperationActionArtmeshMirrorKeyInterpolationZero,
    )
    from .modeling_operation_action_artmesh_multi_key import ModelingOperationActionArtmeshMultiKey
    from .modeling_operation_action_artmesh_multi_key_curve import ModelingOperationActionArtmeshMultiKeyCurve
    from .modeling_operation_action_artmesh_multi_key_curve_control_points_item import (
        ModelingOperationActionArtmeshMultiKeyCurveControlPointsItem,
    )
    from .modeling_operation_action_artmesh_multi_key_interpolation import (
        ModelingOperationActionArtmeshMultiKeyInterpolation,
    )
    from .modeling_operation_action_artmesh_multi_key_interpolation_four import (
        ModelingOperationActionArtmeshMultiKeyInterpolationFour,
    )
    from .modeling_operation_action_artmesh_multi_key_interpolation_one import (
        ModelingOperationActionArtmeshMultiKeyInterpolationOne,
    )
    from .modeling_operation_action_artmesh_multi_key_interpolation_three import (
        ModelingOperationActionArtmeshMultiKeyInterpolationThree,
    )
    from .modeling_operation_action_artmesh_multi_key_interpolation_two import (
        ModelingOperationActionArtmeshMultiKeyInterpolationTwo,
    )
    from .modeling_operation_action_artmesh_multi_key_interpolation_zero import (
        ModelingOperationActionArtmeshMultiKeyInterpolationZero,
    )
    from .modeling_operation_action_artmesh_multi_key_offsets_item import (
        ModelingOperationActionArtmeshMultiKeyOffsetsItem,
    )
    from .modeling_operation_action_artmesh_offset import ModelingOperationActionArtmeshOffset
    from .modeling_operation_action_artmesh_offset_uv import ModelingOperationActionArtmeshOffsetUv
    from .modeling_operation_action_artmesh_quality import ModelingOperationActionArtmeshQuality
    from .modeling_operation_action_artmesh_quality_quality import ModelingOperationActionArtmeshQualityQuality
    from .modeling_operation_action_artmesh_rebuild import ModelingOperationActionArtmeshRebuild
    from .modeling_operation_action_artmesh_rebuild_preset import ModelingOperationActionArtmeshRebuildPreset
    from .modeling_operation_action_artmesh_rebuild_preset_five import ModelingOperationActionArtmeshRebuildPresetFive
    from .modeling_operation_action_artmesh_rebuild_preset_four import ModelingOperationActionArtmeshRebuildPresetFour
    from .modeling_operation_action_artmesh_rebuild_preset_one import ModelingOperationActionArtmeshRebuildPresetOne
    from .modeling_operation_action_artmesh_rebuild_preset_three import ModelingOperationActionArtmeshRebuildPresetThree
    from .modeling_operation_action_artmesh_rebuild_preset_two import ModelingOperationActionArtmeshRebuildPresetTwo
    from .modeling_operation_action_artmesh_rebuild_preset_zero import ModelingOperationActionArtmeshRebuildPresetZero
    from .modeling_operation_action_artmesh_rebuild_quality import ModelingOperationActionArtmeshRebuildQuality
    from .modeling_operation_action_artmesh_rebuild_topology import ModelingOperationActionArtmeshRebuildTopology
    from .modeling_operation_action_artmesh_rebuild_topology_one import ModelingOperationActionArtmeshRebuildTopologyOne
    from .modeling_operation_action_artmesh_rebuild_topology_zero import (
        ModelingOperationActionArtmeshRebuildTopologyZero,
    )
    from .modeling_operation_action_binding_key import ModelingOperationActionBindingKey
    from .modeling_operation_action_binding_key_curve import ModelingOperationActionBindingKeyCurve
    from .modeling_operation_action_binding_key_curve_control_points_item import (
        ModelingOperationActionBindingKeyCurveControlPointsItem,
    )
    from .modeling_operation_action_binding_key_interpolation import ModelingOperationActionBindingKeyInterpolation
    from .modeling_operation_action_binding_key_interpolation_four import (
        ModelingOperationActionBindingKeyInterpolationFour,
    )
    from .modeling_operation_action_binding_key_interpolation_one import (
        ModelingOperationActionBindingKeyInterpolationOne,
    )
    from .modeling_operation_action_binding_key_interpolation_three import (
        ModelingOperationActionBindingKeyInterpolationThree,
    )
    from .modeling_operation_action_binding_key_interpolation_two import (
        ModelingOperationActionBindingKeyInterpolationTwo,
    )
    from .modeling_operation_action_binding_key_interpolation_zero import (
        ModelingOperationActionBindingKeyInterpolationZero,
    )
    from .modeling_operation_action_binding_key_property import ModelingOperationActionBindingKeyProperty
    from .modeling_operation_action_binding_key_property_five import ModelingOperationActionBindingKeyPropertyFive
    from .modeling_operation_action_binding_key_property_four import ModelingOperationActionBindingKeyPropertyFour
    from .modeling_operation_action_binding_key_property_one import ModelingOperationActionBindingKeyPropertyOne
    from .modeling_operation_action_binding_key_property_three import ModelingOperationActionBindingKeyPropertyThree
    from .modeling_operation_action_binding_key_property_two import ModelingOperationActionBindingKeyPropertyTwo
    from .modeling_operation_action_binding_key_property_zero import ModelingOperationActionBindingKeyPropertyZero
    from .modeling_operation_action_blend_shape_set import ModelingOperationActionBlendShapeSet
    from .modeling_operation_action_blend_shape_set_shape import (
        ModelingOperationActionBlendShapeSetShape,
        ModelingOperationActionBlendShapeSetShape_ArtPath,
        ModelingOperationActionBlendShapeSetShape_Deformer,
        ModelingOperationActionBlendShapeSetShape_Glue,
        ModelingOperationActionBlendShapeSetShape_Part,
    )
    from .modeling_operation_action_blend_shape_set_shape_art_path import (
        ModelingOperationActionBlendShapeSetShapeArtPath,
    )
    from .modeling_operation_action_blend_shape_set_shape_art_path_curve import (
        ModelingOperationActionBlendShapeSetShapeArtPathCurve,
    )
    from .modeling_operation_action_blend_shape_set_shape_art_path_curve_control_points_item import (
        ModelingOperationActionBlendShapeSetShapeArtPathCurveControlPointsItem,
    )
    from .modeling_operation_action_blend_shape_set_shape_art_path_interpolation import (
        ModelingOperationActionBlendShapeSetShapeArtPathInterpolation,
    )
    from .modeling_operation_action_blend_shape_set_shape_art_path_interpolation_four import (
        ModelingOperationActionBlendShapeSetShapeArtPathInterpolationFour,
    )
    from .modeling_operation_action_blend_shape_set_shape_art_path_interpolation_one import (
        ModelingOperationActionBlendShapeSetShapeArtPathInterpolationOne,
    )
    from .modeling_operation_action_blend_shape_set_shape_art_path_interpolation_three import (
        ModelingOperationActionBlendShapeSetShapeArtPathInterpolationThree,
    )
    from .modeling_operation_action_blend_shape_set_shape_art_path_interpolation_two import (
        ModelingOperationActionBlendShapeSetShapeArtPathInterpolationTwo,
    )
    from .modeling_operation_action_blend_shape_set_shape_art_path_interpolation_zero import (
        ModelingOperationActionBlendShapeSetShapeArtPathInterpolationZero,
    )
    from .modeling_operation_action_blend_shape_set_shape_art_path_points_item import (
        ModelingOperationActionBlendShapeSetShapeArtPathPointsItem,
    )
    from .modeling_operation_action_blend_shape_set_shape_deformer import (
        ModelingOperationActionBlendShapeSetShapeDeformer,
    )
    from .modeling_operation_action_blend_shape_set_shape_deformer_curve import (
        ModelingOperationActionBlendShapeSetShapeDeformerCurve,
    )
    from .modeling_operation_action_blend_shape_set_shape_deformer_curve_control_points_item import (
        ModelingOperationActionBlendShapeSetShapeDeformerCurveControlPointsItem,
    )
    from .modeling_operation_action_blend_shape_set_shape_deformer_interpolation import (
        ModelingOperationActionBlendShapeSetShapeDeformerInterpolation,
    )
    from .modeling_operation_action_blend_shape_set_shape_deformer_interpolation_four import (
        ModelingOperationActionBlendShapeSetShapeDeformerInterpolationFour,
    )
    from .modeling_operation_action_blend_shape_set_shape_deformer_interpolation_one import (
        ModelingOperationActionBlendShapeSetShapeDeformerInterpolationOne,
    )
    from .modeling_operation_action_blend_shape_set_shape_deformer_interpolation_three import (
        ModelingOperationActionBlendShapeSetShapeDeformerInterpolationThree,
    )
    from .modeling_operation_action_blend_shape_set_shape_deformer_interpolation_two import (
        ModelingOperationActionBlendShapeSetShapeDeformerInterpolationTwo,
    )
    from .modeling_operation_action_blend_shape_set_shape_deformer_interpolation_zero import (
        ModelingOperationActionBlendShapeSetShapeDeformerInterpolationZero,
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
    from .modeling_operation_action_blend_shape_set_shape_glue import ModelingOperationActionBlendShapeSetShapeGlue
    from .modeling_operation_action_blend_shape_set_shape_glue_curve import (
        ModelingOperationActionBlendShapeSetShapeGlueCurve,
    )
    from .modeling_operation_action_blend_shape_set_shape_glue_curve_control_points_item import (
        ModelingOperationActionBlendShapeSetShapeGlueCurveControlPointsItem,
    )
    from .modeling_operation_action_blend_shape_set_shape_glue_interpolation import (
        ModelingOperationActionBlendShapeSetShapeGlueInterpolation,
    )
    from .modeling_operation_action_blend_shape_set_shape_glue_interpolation_four import (
        ModelingOperationActionBlendShapeSetShapeGlueInterpolationFour,
    )
    from .modeling_operation_action_blend_shape_set_shape_glue_interpolation_one import (
        ModelingOperationActionBlendShapeSetShapeGlueInterpolationOne,
    )
    from .modeling_operation_action_blend_shape_set_shape_glue_interpolation_three import (
        ModelingOperationActionBlendShapeSetShapeGlueInterpolationThree,
    )
    from .modeling_operation_action_blend_shape_set_shape_glue_interpolation_two import (
        ModelingOperationActionBlendShapeSetShapeGlueInterpolationTwo,
    )
    from .modeling_operation_action_blend_shape_set_shape_glue_interpolation_zero import (
        ModelingOperationActionBlendShapeSetShapeGlueInterpolationZero,
    )
    from .modeling_operation_action_blend_shape_set_shape_part import ModelingOperationActionBlendShapeSetShapePart
    from .modeling_operation_action_blend_shape_set_shape_part_curve import (
        ModelingOperationActionBlendShapeSetShapePartCurve,
    )
    from .modeling_operation_action_blend_shape_set_shape_part_curve_control_points_item import (
        ModelingOperationActionBlendShapeSetShapePartCurveControlPointsItem,
    )
    from .modeling_operation_action_blend_shape_set_shape_part_interpolation import (
        ModelingOperationActionBlendShapeSetShapePartInterpolation,
    )
    from .modeling_operation_action_blend_shape_set_shape_part_interpolation_four import (
        ModelingOperationActionBlendShapeSetShapePartInterpolationFour,
    )
    from .modeling_operation_action_blend_shape_set_shape_part_interpolation_one import (
        ModelingOperationActionBlendShapeSetShapePartInterpolationOne,
    )
    from .modeling_operation_action_blend_shape_set_shape_part_interpolation_three import (
        ModelingOperationActionBlendShapeSetShapePartInterpolationThree,
    )
    from .modeling_operation_action_blend_shape_set_shape_part_interpolation_two import (
        ModelingOperationActionBlendShapeSetShapePartInterpolationTwo,
    )
    from .modeling_operation_action_blend_shape_set_shape_part_interpolation_zero import (
        ModelingOperationActionBlendShapeSetShapePartInterpolationZero,
    )
    from .modeling_operation_action_blend_shape_set_shape_part_transform import (
        ModelingOperationActionBlendShapeSetShapePartTransform,
    )
    from .modeling_operation_action_deform_brush import ModelingOperationActionDeformBrush
    from .modeling_operation_action_deform_brush_brush import ModelingOperationActionDeformBrushBrush
    from .modeling_operation_action_deform_brush_brush_destination import (
        ModelingOperationActionDeformBrushBrushDestination,
        ModelingOperationActionDeformBrushBrushDestination_Base,
        ModelingOperationActionDeformBrushBrushDestination_BlendShape,
        ModelingOperationActionDeformBrushBrushDestination_Keyform,
    )
    from .modeling_operation_action_deform_brush_brush_destination_base import (
        ModelingOperationActionDeformBrushBrushDestinationBase,
    )
    from .modeling_operation_action_deform_brush_brush_destination_blend_shape import (
        ModelingOperationActionDeformBrushBrushDestinationBlendShape,
    )
    from .modeling_operation_action_deform_brush_brush_destination_blend_shape_shape import (
        ModelingOperationActionDeformBrushBrushDestinationBlendShapeShape,
    )
    from .modeling_operation_action_deform_brush_brush_destination_blend_shape_shape_curve import (
        ModelingOperationActionDeformBrushBrushDestinationBlendShapeShapeCurve,
    )
    from .modeling_operation_action_deform_brush_brush_destination_blend_shape_shape_curve_control_points_item import (
        ModelingOperationActionDeformBrushBrushDestinationBlendShapeShapeCurveControlPointsItem,
    )
    from .modeling_operation_action_deform_brush_brush_destination_blend_shape_shape_interpolation import (
        ModelingOperationActionDeformBrushBrushDestinationBlendShapeShapeInterpolation,
    )
    from .modeling_operation_action_deform_brush_brush_destination_blend_shape_shape_interpolation_four import (
        ModelingOperationActionDeformBrushBrushDestinationBlendShapeShapeInterpolationFour,
    )
    from .modeling_operation_action_deform_brush_brush_destination_blend_shape_shape_interpolation_one import (
        ModelingOperationActionDeformBrushBrushDestinationBlendShapeShapeInterpolationOne,
    )
    from .modeling_operation_action_deform_brush_brush_destination_blend_shape_shape_interpolation_three import (
        ModelingOperationActionDeformBrushBrushDestinationBlendShapeShapeInterpolationThree,
    )
    from .modeling_operation_action_deform_brush_brush_destination_blend_shape_shape_interpolation_two import (
        ModelingOperationActionDeformBrushBrushDestinationBlendShapeShapeInterpolationTwo,
    )
    from .modeling_operation_action_deform_brush_brush_destination_blend_shape_shape_interpolation_zero import (
        ModelingOperationActionDeformBrushBrushDestinationBlendShapeShapeInterpolationZero,
    )
    from .modeling_operation_action_deform_brush_brush_destination_keyform import (
        ModelingOperationActionDeformBrushBrushDestinationKeyform,
    )
    from .modeling_operation_action_deform_brush_brush_effect import (
        ModelingOperationActionDeformBrushBrushEffect,
        ModelingOperationActionDeformBrushBrushEffect_Bend,
        ModelingOperationActionDeformBrushBrushEffect_ContourFollow,
        ModelingOperationActionDeformBrushBrushEffect_Inflate,
        ModelingOperationActionDeformBrushBrushEffect_Pinch,
        ModelingOperationActionDeformBrushBrushEffect_Relax,
        ModelingOperationActionDeformBrushBrushEffect_Smooth,
    )
    from .modeling_operation_action_deform_brush_brush_effect_bend import (
        ModelingOperationActionDeformBrushBrushEffectBend,
    )
    from .modeling_operation_action_deform_brush_brush_effect_contour_follow import (
        ModelingOperationActionDeformBrushBrushEffectContourFollow,
    )
    from .modeling_operation_action_deform_brush_brush_effect_inflate import (
        ModelingOperationActionDeformBrushBrushEffectInflate,
    )
    from .modeling_operation_action_deform_brush_brush_effect_pinch import (
        ModelingOperationActionDeformBrushBrushEffectPinch,
    )
    from .modeling_operation_action_deform_brush_brush_effect_relax import (
        ModelingOperationActionDeformBrushBrushEffectRelax,
    )
    from .modeling_operation_action_deform_brush_brush_effect_smooth import (
        ModelingOperationActionDeformBrushBrushEffectSmooth,
    )
    from .modeling_operation_action_deform_brush_brush_falloff import ModelingOperationActionDeformBrushBrushFalloff
    from .modeling_operation_action_deform_brush_brush_falloff_one import (
        ModelingOperationActionDeformBrushBrushFalloffOne,
    )
    from .modeling_operation_action_deform_brush_brush_falloff_zero import (
        ModelingOperationActionDeformBrushBrushFalloffZero,
    )
    from .modeling_operation_action_deform_brush_brush_surface import (
        ModelingOperationActionDeformBrushBrushSurface,
        ModelingOperationActionDeformBrushBrushSurface_Artmesh,
        ModelingOperationActionDeformBrushBrushSurface_SharedWarp,
        ModelingOperationActionDeformBrushBrushSurface_WarpPins,
    )
    from .modeling_operation_action_deform_brush_brush_surface_artmesh import (
        ModelingOperationActionDeformBrushBrushSurfaceArtmesh,
    )
    from .modeling_operation_action_deform_brush_brush_surface_artmesh_space import (
        ModelingOperationActionDeformBrushBrushSurfaceArtmeshSpace,
    )
    from .modeling_operation_action_deform_brush_brush_surface_shared_warp import (
        ModelingOperationActionDeformBrushBrushSurfaceSharedWarp,
    )
    from .modeling_operation_action_deform_brush_brush_surface_shared_warp_space import (
        ModelingOperationActionDeformBrushBrushSurfaceSharedWarpSpace,
    )
    from .modeling_operation_action_deform_brush_brush_surface_warp_pins import (
        ModelingOperationActionDeformBrushBrushSurfaceWarpPins,
    )
    from .modeling_operation_action_deform_brush_brush_surface_warp_pins_space import (
        ModelingOperationActionDeformBrushBrushSurfaceWarpPinsSpace,
    )
    from .modeling_operation_action_deformer_binding_key import ModelingOperationActionDeformerBindingKey
    from .modeling_operation_action_deformer_binding_key_curve import ModelingOperationActionDeformerBindingKeyCurve
    from .modeling_operation_action_deformer_binding_key_curve_control_points_item import (
        ModelingOperationActionDeformerBindingKeyCurveControlPointsItem,
    )
    from .modeling_operation_action_deformer_binding_key_interpolation import (
        ModelingOperationActionDeformerBindingKeyInterpolation,
    )
    from .modeling_operation_action_deformer_binding_key_interpolation_four import (
        ModelingOperationActionDeformerBindingKeyInterpolationFour,
    )
    from .modeling_operation_action_deformer_binding_key_interpolation_one import (
        ModelingOperationActionDeformerBindingKeyInterpolationOne,
    )
    from .modeling_operation_action_deformer_binding_key_interpolation_three import (
        ModelingOperationActionDeformerBindingKeyInterpolationThree,
    )
    from .modeling_operation_action_deformer_binding_key_interpolation_two import (
        ModelingOperationActionDeformerBindingKeyInterpolationTwo,
    )
    from .modeling_operation_action_deformer_binding_key_interpolation_zero import (
        ModelingOperationActionDeformerBindingKeyInterpolationZero,
    )
    from .modeling_operation_action_deformer_binding_key_property import (
        ModelingOperationActionDeformerBindingKeyProperty,
    )
    from .modeling_operation_action_deformer_binding_key_property_eight import (
        ModelingOperationActionDeformerBindingKeyPropertyEight,
    )
    from .modeling_operation_action_deformer_binding_key_property_five import (
        ModelingOperationActionDeformerBindingKeyPropertyFive,
    )
    from .modeling_operation_action_deformer_binding_key_property_four import (
        ModelingOperationActionDeformerBindingKeyPropertyFour,
    )
    from .modeling_operation_action_deformer_binding_key_property_nine import (
        ModelingOperationActionDeformerBindingKeyPropertyNine,
    )
    from .modeling_operation_action_deformer_binding_key_property_one import (
        ModelingOperationActionDeformerBindingKeyPropertyOne,
    )
    from .modeling_operation_action_deformer_binding_key_property_seven import (
        ModelingOperationActionDeformerBindingKeyPropertySeven,
    )
    from .modeling_operation_action_deformer_binding_key_property_six import (
        ModelingOperationActionDeformerBindingKeyPropertySix,
    )
    from .modeling_operation_action_deformer_binding_key_property_three import (
        ModelingOperationActionDeformerBindingKeyPropertyThree,
    )
    from .modeling_operation_action_deformer_binding_key_property_two import (
        ModelingOperationActionDeformerBindingKeyPropertyTwo,
    )
    from .modeling_operation_action_deformer_binding_key_property_zero import (
        ModelingOperationActionDeformerBindingKeyPropertyZero,
    )
    from .modeling_operation_action_deformer_binding_remove import ModelingOperationActionDeformerBindingRemove
    from .modeling_operation_action_deformer_binding_remove_property import (
        ModelingOperationActionDeformerBindingRemoveProperty,
    )
    from .modeling_operation_action_deformer_binding_remove_property_eight import (
        ModelingOperationActionDeformerBindingRemovePropertyEight,
    )
    from .modeling_operation_action_deformer_binding_remove_property_five import (
        ModelingOperationActionDeformerBindingRemovePropertyFive,
    )
    from .modeling_operation_action_deformer_binding_remove_property_four import (
        ModelingOperationActionDeformerBindingRemovePropertyFour,
    )
    from .modeling_operation_action_deformer_binding_remove_property_nine import (
        ModelingOperationActionDeformerBindingRemovePropertyNine,
    )
    from .modeling_operation_action_deformer_binding_remove_property_one import (
        ModelingOperationActionDeformerBindingRemovePropertyOne,
    )
    from .modeling_operation_action_deformer_binding_remove_property_seven import (
        ModelingOperationActionDeformerBindingRemovePropertySeven,
    )
    from .modeling_operation_action_deformer_binding_remove_property_six import (
        ModelingOperationActionDeformerBindingRemovePropertySix,
    )
    from .modeling_operation_action_deformer_binding_remove_property_three import (
        ModelingOperationActionDeformerBindingRemovePropertyThree,
    )
    from .modeling_operation_action_deformer_binding_remove_property_two import (
        ModelingOperationActionDeformerBindingRemovePropertyTwo,
    )
    from .modeling_operation_action_deformer_binding_remove_property_zero import (
        ModelingOperationActionDeformerBindingRemovePropertyZero,
    )
    from .modeling_operation_action_deformer_create import ModelingOperationActionDeformerCreate
    from .modeling_operation_action_deformer_create_deformer import ModelingOperationActionDeformerCreateDeformer
    from .modeling_operation_action_deformer_create_deformer_bindings_item import (
        ModelingOperationActionDeformerCreateDeformerBindingsItem,
    )
    from .modeling_operation_action_deformer_create_deformer_bindings_item_composition import (
        ModelingOperationActionDeformerCreateDeformerBindingsItemComposition,
    )
    from .modeling_operation_action_deformer_create_deformer_bindings_item_composition_one import (
        ModelingOperationActionDeformerCreateDeformerBindingsItemCompositionOne,
    )
    from .modeling_operation_action_deformer_create_deformer_bindings_item_composition_zero import (
        ModelingOperationActionDeformerCreateDeformerBindingsItemCompositionZero,
    )
    from .modeling_operation_action_deformer_create_deformer_bindings_item_curve import (
        ModelingOperationActionDeformerCreateDeformerBindingsItemCurve,
    )
    from .modeling_operation_action_deformer_create_deformer_bindings_item_curve_control_points_item import (
        ModelingOperationActionDeformerCreateDeformerBindingsItemCurveControlPointsItem,
    )
    from .modeling_operation_action_deformer_create_deformer_bindings_item_interpolation import (
        ModelingOperationActionDeformerCreateDeformerBindingsItemInterpolation,
    )
    from .modeling_operation_action_deformer_create_deformer_bindings_item_interpolation_four import (
        ModelingOperationActionDeformerCreateDeformerBindingsItemInterpolationFour,
    )
    from .modeling_operation_action_deformer_create_deformer_bindings_item_interpolation_one import (
        ModelingOperationActionDeformerCreateDeformerBindingsItemInterpolationOne,
    )
    from .modeling_operation_action_deformer_create_deformer_bindings_item_interpolation_three import (
        ModelingOperationActionDeformerCreateDeformerBindingsItemInterpolationThree,
    )
    from .modeling_operation_action_deformer_create_deformer_bindings_item_interpolation_two import (
        ModelingOperationActionDeformerCreateDeformerBindingsItemInterpolationTwo,
    )
    from .modeling_operation_action_deformer_create_deformer_bindings_item_interpolation_zero import (
        ModelingOperationActionDeformerCreateDeformerBindingsItemInterpolationZero,
    )
    from .modeling_operation_action_deformer_create_deformer_bindings_item_keys_item import (
        ModelingOperationActionDeformerCreateDeformerBindingsItemKeysItem,
    )
    from .modeling_operation_action_deformer_create_deformer_bindings_item_property import (
        ModelingOperationActionDeformerCreateDeformerBindingsItemProperty,
    )
    from .modeling_operation_action_deformer_create_deformer_bindings_item_property_eight import (
        ModelingOperationActionDeformerCreateDeformerBindingsItemPropertyEight,
    )
    from .modeling_operation_action_deformer_create_deformer_bindings_item_property_five import (
        ModelingOperationActionDeformerCreateDeformerBindingsItemPropertyFive,
    )
    from .modeling_operation_action_deformer_create_deformer_bindings_item_property_four import (
        ModelingOperationActionDeformerCreateDeformerBindingsItemPropertyFour,
    )
    from .modeling_operation_action_deformer_create_deformer_bindings_item_property_nine import (
        ModelingOperationActionDeformerCreateDeformerBindingsItemPropertyNine,
    )
    from .modeling_operation_action_deformer_create_deformer_bindings_item_property_one import (
        ModelingOperationActionDeformerCreateDeformerBindingsItemPropertyOne,
    )
    from .modeling_operation_action_deformer_create_deformer_bindings_item_property_seven import (
        ModelingOperationActionDeformerCreateDeformerBindingsItemPropertySeven,
    )
    from .modeling_operation_action_deformer_create_deformer_bindings_item_property_six import (
        ModelingOperationActionDeformerCreateDeformerBindingsItemPropertySix,
    )
    from .modeling_operation_action_deformer_create_deformer_bindings_item_property_three import (
        ModelingOperationActionDeformerCreateDeformerBindingsItemPropertyThree,
    )
    from .modeling_operation_action_deformer_create_deformer_bindings_item_property_two import (
        ModelingOperationActionDeformerCreateDeformerBindingsItemPropertyTwo,
    )
    from .modeling_operation_action_deformer_create_deformer_bindings_item_property_zero import (
        ModelingOperationActionDeformerCreateDeformerBindingsItemPropertyZero,
    )
    from .modeling_operation_action_deformer_create_deformer_blend_shapes_item import (
        ModelingOperationActionDeformerCreateDeformerBlendShapesItem,
    )
    from .modeling_operation_action_deformer_create_deformer_blend_shapes_item_curve import (
        ModelingOperationActionDeformerCreateDeformerBlendShapesItemCurve,
    )
    from .modeling_operation_action_deformer_create_deformer_blend_shapes_item_curve_control_points_item import (
        ModelingOperationActionDeformerCreateDeformerBlendShapesItemCurveControlPointsItem,
    )
    from .modeling_operation_action_deformer_create_deformer_blend_shapes_item_interpolation import (
        ModelingOperationActionDeformerCreateDeformerBlendShapesItemInterpolation,
    )
    from .modeling_operation_action_deformer_create_deformer_blend_shapes_item_interpolation_four import (
        ModelingOperationActionDeformerCreateDeformerBlendShapesItemInterpolationFour,
    )
    from .modeling_operation_action_deformer_create_deformer_blend_shapes_item_interpolation_one import (
        ModelingOperationActionDeformerCreateDeformerBlendShapesItemInterpolationOne,
    )
    from .modeling_operation_action_deformer_create_deformer_blend_shapes_item_interpolation_three import (
        ModelingOperationActionDeformerCreateDeformerBlendShapesItemInterpolationThree,
    )
    from .modeling_operation_action_deformer_create_deformer_blend_shapes_item_interpolation_two import (
        ModelingOperationActionDeformerCreateDeformerBlendShapesItemInterpolationTwo,
    )
    from .modeling_operation_action_deformer_create_deformer_blend_shapes_item_interpolation_zero import (
        ModelingOperationActionDeformerCreateDeformerBlendShapesItemInterpolationZero,
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
    from .modeling_operation_action_deformer_create_deformer_kind import (
        ModelingOperationActionDeformerCreateDeformerKind,
    )
    from .modeling_operation_action_deformer_create_deformer_kind_one import (
        ModelingOperationActionDeformerCreateDeformerKindOne,
    )
    from .modeling_operation_action_deformer_create_deformer_kind_two import (
        ModelingOperationActionDeformerCreateDeformerKindTwo,
    )
    from .modeling_operation_action_deformer_create_deformer_kind_zero import (
        ModelingOperationActionDeformerCreateDeformerKindZero,
    )
    from .modeling_operation_action_deformer_create_deformer_multi_bindings_item import (
        ModelingOperationActionDeformerCreateDeformerMultiBindingsItem,
    )
    from .modeling_operation_action_deformer_create_deformer_multi_bindings_item_composition import (
        ModelingOperationActionDeformerCreateDeformerMultiBindingsItemComposition,
    )
    from .modeling_operation_action_deformer_create_deformer_multi_bindings_item_composition_one import (
        ModelingOperationActionDeformerCreateDeformerMultiBindingsItemCompositionOne,
    )
    from .modeling_operation_action_deformer_create_deformer_multi_bindings_item_composition_zero import (
        ModelingOperationActionDeformerCreateDeformerMultiBindingsItemCompositionZero,
    )
    from .modeling_operation_action_deformer_create_deformer_multi_bindings_item_curve import (
        ModelingOperationActionDeformerCreateDeformerMultiBindingsItemCurve,
    )
    from .modeling_operation_action_deformer_create_deformer_multi_bindings_item_curve_control_points_item import (
        ModelingOperationActionDeformerCreateDeformerMultiBindingsItemCurveControlPointsItem,
    )
    from .modeling_operation_action_deformer_create_deformer_multi_bindings_item_interpolation import (
        ModelingOperationActionDeformerCreateDeformerMultiBindingsItemInterpolation,
    )
    from .modeling_operation_action_deformer_create_deformer_multi_bindings_item_interpolation_four import (
        ModelingOperationActionDeformerCreateDeformerMultiBindingsItemInterpolationFour,
    )
    from .modeling_operation_action_deformer_create_deformer_multi_bindings_item_interpolation_one import (
        ModelingOperationActionDeformerCreateDeformerMultiBindingsItemInterpolationOne,
    )
    from .modeling_operation_action_deformer_create_deformer_multi_bindings_item_interpolation_three import (
        ModelingOperationActionDeformerCreateDeformerMultiBindingsItemInterpolationThree,
    )
    from .modeling_operation_action_deformer_create_deformer_multi_bindings_item_interpolation_two import (
        ModelingOperationActionDeformerCreateDeformerMultiBindingsItemInterpolationTwo,
    )
    from .modeling_operation_action_deformer_create_deformer_multi_bindings_item_interpolation_zero import (
        ModelingOperationActionDeformerCreateDeformerMultiBindingsItemInterpolationZero,
    )
    from .modeling_operation_action_deformer_create_deformer_multi_bindings_item_keyforms_item import (
        ModelingOperationActionDeformerCreateDeformerMultiBindingsItemKeyformsItem,
    )
    from .modeling_operation_action_deformer_create_deformer_multi_bindings_item_property import (
        ModelingOperationActionDeformerCreateDeformerMultiBindingsItemProperty,
    )
    from .modeling_operation_action_deformer_create_deformer_multi_bindings_item_property_eight import (
        ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertyEight,
    )
    from .modeling_operation_action_deformer_create_deformer_multi_bindings_item_property_eleven import (
        ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertyEleven,
    )
    from .modeling_operation_action_deformer_create_deformer_multi_bindings_item_property_five import (
        ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertyFive,
    )
    from .modeling_operation_action_deformer_create_deformer_multi_bindings_item_property_four import (
        ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertyFour,
    )
    from .modeling_operation_action_deformer_create_deformer_multi_bindings_item_property_nine import (
        ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertyNine,
    )
    from .modeling_operation_action_deformer_create_deformer_multi_bindings_item_property_one import (
        ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertyOne,
    )
    from .modeling_operation_action_deformer_create_deformer_multi_bindings_item_property_seven import (
        ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertySeven,
    )
    from .modeling_operation_action_deformer_create_deformer_multi_bindings_item_property_six import (
        ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertySix,
    )
    from .modeling_operation_action_deformer_create_deformer_multi_bindings_item_property_ten import (
        ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertyTen,
    )
    from .modeling_operation_action_deformer_create_deformer_multi_bindings_item_property_three import (
        ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertyThree,
    )
    from .modeling_operation_action_deformer_create_deformer_multi_bindings_item_property_two import (
        ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertyTwo,
    )
    from .modeling_operation_action_deformer_create_deformer_multi_bindings_item_property_zero import (
        ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertyZero,
    )
    from .modeling_operation_action_deformer_create_deformer_origin import (
        ModelingOperationActionDeformerCreateDeformerOrigin,
    )
    from .modeling_operation_action_deformer_create_deformer_rotation_metadata import (
        ModelingOperationActionDeformerCreateDeformerRotationMetadata,
    )
    from .modeling_operation_action_deformer_create_deformer_rotation_metadata_angle_range import (
        ModelingOperationActionDeformerCreateDeformerRotationMetadataAngleRange,
    )
    from .modeling_operation_action_deformer_create_deformer_rotation_metadata_angle_unit import (
        ModelingOperationActionDeformerCreateDeformerRotationMetadataAngleUnit,
    )
    from .modeling_operation_action_deformer_create_deformer_rotation_metadata_parent_composition import (
        ModelingOperationActionDeformerCreateDeformerRotationMetadataParentComposition,
    )
    from .modeling_operation_action_deformer_create_deformer_rotation_metadata_parent_composition_one import (
        ModelingOperationActionDeformerCreateDeformerRotationMetadataParentCompositionOne,
    )
    from .modeling_operation_action_deformer_create_deformer_rotation_metadata_parent_composition_zero import (
        ModelingOperationActionDeformerCreateDeformerRotationMetadataParentCompositionZero,
    )
    from .modeling_operation_action_deformer_create_deformer_rotation_metadata_pivot import (
        ModelingOperationActionDeformerCreateDeformerRotationMetadataPivot,
    )
    from .modeling_operation_action_deformer_create_deformer_rotation_metadata_pivot_space import (
        ModelingOperationActionDeformerCreateDeformerRotationMetadataPivotSpace,
    )
    from .modeling_operation_action_deformer_create_deformer_rotation_metadata_pivot_space_one import (
        ModelingOperationActionDeformerCreateDeformerRotationMetadataPivotSpaceOne,
    )
    from .modeling_operation_action_deformer_create_deformer_rotation_metadata_pivot_space_zero import (
        ModelingOperationActionDeformerCreateDeformerRotationMetadataPivotSpaceZero,
    )
    from .modeling_operation_action_deformer_create_deformer_rotation_metadata_shape_preservation import (
        ModelingOperationActionDeformerCreateDeformerRotationMetadataShapePreservation,
    )
    from .modeling_operation_action_deformer_create_deformer_rotation_metadata_shape_preservation_one import (
        ModelingOperationActionDeformerCreateDeformerRotationMetadataShapePreservationOne,
    )
    from .modeling_operation_action_deformer_create_deformer_rotation_metadata_shape_preservation_two import (
        ModelingOperationActionDeformerCreateDeformerRotationMetadataShapePreservationTwo,
    )
    from .modeling_operation_action_deformer_create_deformer_rotation_metadata_shape_preservation_zero import (
        ModelingOperationActionDeformerCreateDeformerRotationMetadataShapePreservationZero,
    )
    from .modeling_operation_action_deformer_create_deformer_shared_warp import (
        ModelingOperationActionDeformerCreateDeformerSharedWarp,
    )
    from .modeling_operation_action_deformer_create_deformer_shared_warp_bounds import (
        ModelingOperationActionDeformerCreateDeformerSharedWarpBounds,
    )
    from .modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item import (
        ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItem,
    )
    from .modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item import (
        ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItem,
    )
    from .modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_curve import (
        ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemCurve,
    )
    from .modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_curve_control_points_item import (
        ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemCurveControlPointsItem,
    )
    from .modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_interpolation import (
        ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolation,
    )
    from .modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_interpolation_four import (
        ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolationFour,
    )
    from .modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_interpolation_one import (
        ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolationOne,
    )
    from .modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_interpolation_three import (
        ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolationThree,
    )
    from .modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_interpolation_two import (
        ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolationTwo,
    )
    from .modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_interpolation_zero import (
        ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolationZero,
    )
    from .modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_keys_item import (
        ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemKeysItem,
    )
    from .modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_property import (
        ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemProperty,
    )
    from .modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_property_one import (
        ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemPropertyOne,
    )
    from .modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_property_zero import (
        ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemPropertyZero,
    )
    from .modeling_operation_action_deformer_create_deformer_shared_warp_grid import (
        ModelingOperationActionDeformerCreateDeformerSharedWarpGrid,
    )
    from .modeling_operation_action_deformer_create_deformer_transform import (
        ModelingOperationActionDeformerCreateDeformerTransform,
    )
    from .modeling_operation_action_deformer_create_deformer_warp import (
        ModelingOperationActionDeformerCreateDeformerWarp,
    )
    from .modeling_operation_action_deformer_create_deformer_warp_grid import (
        ModelingOperationActionDeformerCreateDeformerWarpGrid,
    )
    from .modeling_operation_action_deformer_create_deformer_warp_pin_blend_mode import (
        ModelingOperationActionDeformerCreateDeformerWarpPinBlendMode,
    )
    from .modeling_operation_action_deformer_create_deformer_warp_pin_blend_mode_one import (
        ModelingOperationActionDeformerCreateDeformerWarpPinBlendModeOne,
    )
    from .modeling_operation_action_deformer_create_deformer_warp_pin_blend_mode_zero import (
        ModelingOperationActionDeformerCreateDeformerWarpPinBlendModeZero,
    )
    from .modeling_operation_action_deformer_create_deformer_warp_pins_item import (
        ModelingOperationActionDeformerCreateDeformerWarpPinsItem,
    )
    from .modeling_operation_action_deformer_create_deformer_warp_pins_item_bindings_item import (
        ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItem,
    )
    from .modeling_operation_action_deformer_create_deformer_warp_pins_item_bindings_item_curve import (
        ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemCurve,
    )
    from .modeling_operation_action_deformer_create_deformer_warp_pins_item_bindings_item_curve_control_points_item import (
        ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemCurveControlPointsItem,
    )
    from .modeling_operation_action_deformer_create_deformer_warp_pins_item_bindings_item_interpolation import (
        ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolation,
    )
    from .modeling_operation_action_deformer_create_deformer_warp_pins_item_bindings_item_interpolation_four import (
        ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolationFour,
    )
    from .modeling_operation_action_deformer_create_deformer_warp_pins_item_bindings_item_interpolation_one import (
        ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolationOne,
    )
    from .modeling_operation_action_deformer_create_deformer_warp_pins_item_bindings_item_interpolation_three import (
        ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolationThree,
    )
    from .modeling_operation_action_deformer_create_deformer_warp_pins_item_bindings_item_interpolation_two import (
        ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolationTwo,
    )
    from .modeling_operation_action_deformer_create_deformer_warp_pins_item_bindings_item_interpolation_zero import (
        ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolationZero,
    )
    from .modeling_operation_action_deformer_create_deformer_warp_pins_item_bindings_item_keys_item import (
        ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemKeysItem,
    )
    from .modeling_operation_action_deformer_create_deformer_warp_pins_item_bindings_item_property import (
        ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemProperty,
    )
    from .modeling_operation_action_deformer_create_deformer_warp_pins_item_bindings_item_property_one import (
        ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemPropertyOne,
    )
    from .modeling_operation_action_deformer_create_deformer_warp_pins_item_bindings_item_property_zero import (
        ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemPropertyZero,
    )
    from .modeling_operation_action_deformer_create_deformer_warp_pins_item_multi_bindings_item import (
        ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItem,
    )
    from .modeling_operation_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_curve import (
        ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemCurve,
    )
    from .modeling_operation_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_curve_control_points_item import (
        ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemCurveControlPointsItem,
    )
    from .modeling_operation_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_interpolation import (
        ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolation,
    )
    from .modeling_operation_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_interpolation_four import (
        ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolationFour,
    )
    from .modeling_operation_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_interpolation_one import (
        ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolationOne,
    )
    from .modeling_operation_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_interpolation_three import (
        ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolationThree,
    )
    from .modeling_operation_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_interpolation_two import (
        ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolationTwo,
    )
    from .modeling_operation_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_interpolation_zero import (
        ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolationZero,
    )
    from .modeling_operation_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_keyforms_item import (
        ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemKeyformsItem,
    )
    from .modeling_operation_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_property import (
        ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemProperty,
    )
    from .modeling_operation_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_property_one import (
        ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemPropertyOne,
    )
    from .modeling_operation_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_property_zero import (
        ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemPropertyZero,
    )
    from .modeling_operation_action_deformer_kind_set import ModelingOperationActionDeformerKindSet
    from .modeling_operation_action_deformer_kind_set_kind import ModelingOperationActionDeformerKindSetKind
    from .modeling_operation_action_deformer_kind_set_kind_one import ModelingOperationActionDeformerKindSetKindOne
    from .modeling_operation_action_deformer_kind_set_kind_two import ModelingOperationActionDeformerKindSetKindTwo
    from .modeling_operation_action_deformer_kind_set_kind_zero import ModelingOperationActionDeformerKindSetKindZero
    from .modeling_operation_action_deformer_kind_set_warp import ModelingOperationActionDeformerKindSetWarp
    from .modeling_operation_action_deformer_kind_set_warp_grid import ModelingOperationActionDeformerKindSetWarpGrid
    from .modeling_operation_action_deformer_kind_set_warp_pin_blend_mode import (
        ModelingOperationActionDeformerKindSetWarpPinBlendMode,
    )
    from .modeling_operation_action_deformer_kind_set_warp_pin_blend_mode_one import (
        ModelingOperationActionDeformerKindSetWarpPinBlendModeOne,
    )
    from .modeling_operation_action_deformer_kind_set_warp_pin_blend_mode_zero import (
        ModelingOperationActionDeformerKindSetWarpPinBlendModeZero,
    )
    from .modeling_operation_action_deformer_kind_set_warp_pins_item import (
        ModelingOperationActionDeformerKindSetWarpPinsItem,
    )
    from .modeling_operation_action_deformer_kind_set_warp_pins_item_bindings_item import (
        ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItem,
    )
    from .modeling_operation_action_deformer_kind_set_warp_pins_item_bindings_item_curve import (
        ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemCurve,
    )
    from .modeling_operation_action_deformer_kind_set_warp_pins_item_bindings_item_curve_control_points_item import (
        ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemCurveControlPointsItem,
    )
    from .modeling_operation_action_deformer_kind_set_warp_pins_item_bindings_item_interpolation import (
        ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemInterpolation,
    )
    from .modeling_operation_action_deformer_kind_set_warp_pins_item_bindings_item_interpolation_four import (
        ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemInterpolationFour,
    )
    from .modeling_operation_action_deformer_kind_set_warp_pins_item_bindings_item_interpolation_one import (
        ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemInterpolationOne,
    )
    from .modeling_operation_action_deformer_kind_set_warp_pins_item_bindings_item_interpolation_three import (
        ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemInterpolationThree,
    )
    from .modeling_operation_action_deformer_kind_set_warp_pins_item_bindings_item_interpolation_two import (
        ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemInterpolationTwo,
    )
    from .modeling_operation_action_deformer_kind_set_warp_pins_item_bindings_item_interpolation_zero import (
        ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemInterpolationZero,
    )
    from .modeling_operation_action_deformer_kind_set_warp_pins_item_bindings_item_keys_item import (
        ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemKeysItem,
    )
    from .modeling_operation_action_deformer_kind_set_warp_pins_item_bindings_item_property import (
        ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemProperty,
    )
    from .modeling_operation_action_deformer_kind_set_warp_pins_item_bindings_item_property_one import (
        ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemPropertyOne,
    )
    from .modeling_operation_action_deformer_kind_set_warp_pins_item_bindings_item_property_zero import (
        ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemPropertyZero,
    )
    from .modeling_operation_action_deformer_kind_set_warp_pins_item_multi_bindings_item import (
        ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItem,
    )
    from .modeling_operation_action_deformer_kind_set_warp_pins_item_multi_bindings_item_curve import (
        ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemCurve,
    )
    from .modeling_operation_action_deformer_kind_set_warp_pins_item_multi_bindings_item_curve_control_points_item import (
        ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemCurveControlPointsItem,
    )
    from .modeling_operation_action_deformer_kind_set_warp_pins_item_multi_bindings_item_interpolation import (
        ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolation,
    )
    from .modeling_operation_action_deformer_kind_set_warp_pins_item_multi_bindings_item_interpolation_four import (
        ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolationFour,
    )
    from .modeling_operation_action_deformer_kind_set_warp_pins_item_multi_bindings_item_interpolation_one import (
        ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolationOne,
    )
    from .modeling_operation_action_deformer_kind_set_warp_pins_item_multi_bindings_item_interpolation_three import (
        ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolationThree,
    )
    from .modeling_operation_action_deformer_kind_set_warp_pins_item_multi_bindings_item_interpolation_two import (
        ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolationTwo,
    )
    from .modeling_operation_action_deformer_kind_set_warp_pins_item_multi_bindings_item_interpolation_zero import (
        ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolationZero,
    )
    from .modeling_operation_action_deformer_kind_set_warp_pins_item_multi_bindings_item_keyforms_item import (
        ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemKeyformsItem,
    )
    from .modeling_operation_action_deformer_kind_set_warp_pins_item_multi_bindings_item_property import (
        ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemProperty,
    )
    from .modeling_operation_action_deformer_kind_set_warp_pins_item_multi_bindings_item_property_one import (
        ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemPropertyOne,
    )
    from .modeling_operation_action_deformer_kind_set_warp_pins_item_multi_bindings_item_property_zero import (
        ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemPropertyZero,
    )
    from .modeling_operation_action_deformer_origin import ModelingOperationActionDeformerOrigin
    from .modeling_operation_action_deformer_parent_set import ModelingOperationActionDeformerParentSet
    from .modeling_operation_action_deformer_rotation_metadata import ModelingOperationActionDeformerRotationMetadata
    from .modeling_operation_action_deformer_rotation_metadata_metadata import (
        ModelingOperationActionDeformerRotationMetadataMetadata,
    )
    from .modeling_operation_action_deformer_rotation_metadata_metadata_angle_range import (
        ModelingOperationActionDeformerRotationMetadataMetadataAngleRange,
    )
    from .modeling_operation_action_deformer_rotation_metadata_metadata_angle_unit import (
        ModelingOperationActionDeformerRotationMetadataMetadataAngleUnit,
    )
    from .modeling_operation_action_deformer_rotation_metadata_metadata_parent_composition import (
        ModelingOperationActionDeformerRotationMetadataMetadataParentComposition,
    )
    from .modeling_operation_action_deformer_rotation_metadata_metadata_parent_composition_one import (
        ModelingOperationActionDeformerRotationMetadataMetadataParentCompositionOne,
    )
    from .modeling_operation_action_deformer_rotation_metadata_metadata_parent_composition_zero import (
        ModelingOperationActionDeformerRotationMetadataMetadataParentCompositionZero,
    )
    from .modeling_operation_action_deformer_rotation_metadata_metadata_pivot import (
        ModelingOperationActionDeformerRotationMetadataMetadataPivot,
    )
    from .modeling_operation_action_deformer_rotation_metadata_metadata_pivot_space import (
        ModelingOperationActionDeformerRotationMetadataMetadataPivotSpace,
    )
    from .modeling_operation_action_deformer_rotation_metadata_metadata_pivot_space_one import (
        ModelingOperationActionDeformerRotationMetadataMetadataPivotSpaceOne,
    )
    from .modeling_operation_action_deformer_rotation_metadata_metadata_pivot_space_zero import (
        ModelingOperationActionDeformerRotationMetadataMetadataPivotSpaceZero,
    )
    from .modeling_operation_action_deformer_rotation_metadata_metadata_shape_preservation import (
        ModelingOperationActionDeformerRotationMetadataMetadataShapePreservation,
    )
    from .modeling_operation_action_deformer_rotation_metadata_metadata_shape_preservation_one import (
        ModelingOperationActionDeformerRotationMetadataMetadataShapePreservationOne,
    )
    from .modeling_operation_action_deformer_rotation_metadata_metadata_shape_preservation_two import (
        ModelingOperationActionDeformerRotationMetadataMetadataShapePreservationTwo,
    )
    from .modeling_operation_action_deformer_rotation_metadata_metadata_shape_preservation_zero import (
        ModelingOperationActionDeformerRotationMetadataMetadataShapePreservationZero,
    )
    from .modeling_operation_action_deformer_split import ModelingOperationActionDeformerSplit
    from .modeling_operation_action_deformer_targets_set import ModelingOperationActionDeformerTargetsSet
    from .modeling_operation_action_deformer_targets_set_mode import ModelingOperationActionDeformerTargetsSetMode
    from .modeling_operation_action_deformer_targets_set_mode_one import (
        ModelingOperationActionDeformerTargetsSetModeOne,
    )
    from .modeling_operation_action_deformer_targets_set_mode_zero import (
        ModelingOperationActionDeformerTargetsSetModeZero,
    )
    from .modeling_operation_action_deformer_transform import ModelingOperationActionDeformerTransform
    from .modeling_operation_action_deformer_transform_operator import ModelingOperationActionDeformerTransformOperator
    from .modeling_operation_action_deformer_transform_operator_one import (
        ModelingOperationActionDeformerTransformOperatorOne,
    )
    from .modeling_operation_action_deformer_transform_operator_two import (
        ModelingOperationActionDeformerTransformOperatorTwo,
    )
    from .modeling_operation_action_deformer_transform_operator_zero import (
        ModelingOperationActionDeformerTransformOperatorZero,
    )
    from .modeling_operation_action_deformer_transform_property import ModelingOperationActionDeformerTransformProperty
    from .modeling_operation_action_deformer_transform_property_five import (
        ModelingOperationActionDeformerTransformPropertyFive,
    )
    from .modeling_operation_action_deformer_transform_property_four import (
        ModelingOperationActionDeformerTransformPropertyFour,
    )
    from .modeling_operation_action_deformer_transform_property_one import (
        ModelingOperationActionDeformerTransformPropertyOne,
    )
    from .modeling_operation_action_deformer_transform_property_three import (
        ModelingOperationActionDeformerTransformPropertyThree,
    )
    from .modeling_operation_action_deformer_transform_property_two import (
        ModelingOperationActionDeformerTransformPropertyTwo,
    )
    from .modeling_operation_action_deformer_transform_property_zero import (
        ModelingOperationActionDeformerTransformPropertyZero,
    )
    from .modeling_operation_action_parameter_add import ModelingOperationActionParameterAdd
    from .modeling_operation_action_parameter_add_parameter import ModelingOperationActionParameterAddParameter
    from .modeling_operation_action_part_alpha_reveal import ModelingOperationActionPartAlphaReveal
    from .modeling_operation_action_part_alpha_reveal_reveal import ModelingOperationActionPartAlphaRevealReveal
    from .modeling_operation_action_part_blend_mode import ModelingOperationActionPartBlendMode
    from .modeling_operation_action_part_blend_mode_mode import ModelingOperationActionPartBlendModeMode
    from .modeling_operation_action_part_blend_mode_mode_one import ModelingOperationActionPartBlendModeModeOne
    from .modeling_operation_action_part_blend_mode_mode_three import ModelingOperationActionPartBlendModeModeThree
    from .modeling_operation_action_part_blend_mode_mode_two import ModelingOperationActionPartBlendModeModeTwo
    from .modeling_operation_action_part_blend_mode_mode_zero import ModelingOperationActionPartBlendModeModeZero
    from .modeling_operation_action_part_clip import ModelingOperationActionPartClip
    from .modeling_operation_action_part_clip_clip import ModelingOperationActionPartClipClip
    from .modeling_operation_action_part_clip_clip_mask_opacity import ModelingOperationActionPartClipClipMaskOpacity
    from .modeling_operation_action_part_clip_clip_mask_opacity_one import (
        ModelingOperationActionPartClipClipMaskOpacityOne,
    )
    from .modeling_operation_action_part_clip_clip_mask_opacity_zero import (
        ModelingOperationActionPartClipClipMaskOpacityZero,
    )
    from .modeling_operation_action_part_clip_clip_mode import ModelingOperationActionPartClipClipMode
    from .modeling_operation_action_part_contour_shade import ModelingOperationActionPartContourShade
    from .modeling_operation_action_part_contour_shade_shade import ModelingOperationActionPartContourShadeShade
    from .modeling_operation_action_part_contour_shade_shade_profile import (
        ModelingOperationActionPartContourShadeShadeProfile,
    )
    from .modeling_operation_action_part_draw_order import ModelingOperationActionPartDrawOrder
    from .modeling_operation_action_part_tint import ModelingOperationActionPartTint
    from .modeling_operation_action_part_tint_tint import ModelingOperationActionPartTintTint
    from .modeling_operation_action_part_tint_tint_mode import ModelingOperationActionPartTintTintMode
    from .modeling_operation_action_part_tint_tint_mode_one import ModelingOperationActionPartTintTintModeOne
    from .modeling_operation_action_part_tint_tint_mode_zero import ModelingOperationActionPartTintTintModeZero
    from .modeling_operation_action_part_visibility import ModelingOperationActionPartVisibility
    from .modeling_operation_action_role_confirm import ModelingOperationActionRoleConfirm
    from .modeling_operation_action_role_confirm_role import ModelingOperationActionRoleConfirmRole
    from .modeling_operation_action_role_confirm_role_eight import ModelingOperationActionRoleConfirmRoleEight
    from .modeling_operation_action_role_confirm_role_eleven import ModelingOperationActionRoleConfirmRoleEleven
    from .modeling_operation_action_role_confirm_role_fifteen import ModelingOperationActionRoleConfirmRoleFifteen
    from .modeling_operation_action_role_confirm_role_five import ModelingOperationActionRoleConfirmRoleFive
    from .modeling_operation_action_role_confirm_role_four import ModelingOperationActionRoleConfirmRoleFour
    from .modeling_operation_action_role_confirm_role_fourteen import ModelingOperationActionRoleConfirmRoleFourteen
    from .modeling_operation_action_role_confirm_role_nine import ModelingOperationActionRoleConfirmRoleNine
    from .modeling_operation_action_role_confirm_role_one import ModelingOperationActionRoleConfirmRoleOne
    from .modeling_operation_action_role_confirm_role_seven import ModelingOperationActionRoleConfirmRoleSeven
    from .modeling_operation_action_role_confirm_role_seventeen import ModelingOperationActionRoleConfirmRoleSeventeen
    from .modeling_operation_action_role_confirm_role_six import ModelingOperationActionRoleConfirmRoleSix
    from .modeling_operation_action_role_confirm_role_sixteen import ModelingOperationActionRoleConfirmRoleSixteen
    from .modeling_operation_action_role_confirm_role_ten import ModelingOperationActionRoleConfirmRoleTen
    from .modeling_operation_action_role_confirm_role_thirteen import ModelingOperationActionRoleConfirmRoleThirteen
    from .modeling_operation_action_role_confirm_role_three import ModelingOperationActionRoleConfirmRoleThree
    from .modeling_operation_action_role_confirm_role_twelve import ModelingOperationActionRoleConfirmRoleTwelve
    from .modeling_operation_action_role_confirm_role_two import ModelingOperationActionRoleConfirmRoleTwo
    from .modeling_operation_action_role_confirm_role_zero import ModelingOperationActionRoleConfirmRoleZero
    from .modeling_operation_action_role_reclassify import ModelingOperationActionRoleReclassify
    from .modeling_operation_action_role_reclassify_expected_role import (
        ModelingOperationActionRoleReclassifyExpectedRole,
    )
    from .modeling_operation_action_role_reclassify_expected_role_eight import (
        ModelingOperationActionRoleReclassifyExpectedRoleEight,
    )
    from .modeling_operation_action_role_reclassify_expected_role_eleven import (
        ModelingOperationActionRoleReclassifyExpectedRoleEleven,
    )
    from .modeling_operation_action_role_reclassify_expected_role_fifteen import (
        ModelingOperationActionRoleReclassifyExpectedRoleFifteen,
    )
    from .modeling_operation_action_role_reclassify_expected_role_five import (
        ModelingOperationActionRoleReclassifyExpectedRoleFive,
    )
    from .modeling_operation_action_role_reclassify_expected_role_four import (
        ModelingOperationActionRoleReclassifyExpectedRoleFour,
    )
    from .modeling_operation_action_role_reclassify_expected_role_fourteen import (
        ModelingOperationActionRoleReclassifyExpectedRoleFourteen,
    )
    from .modeling_operation_action_role_reclassify_expected_role_nine import (
        ModelingOperationActionRoleReclassifyExpectedRoleNine,
    )
    from .modeling_operation_action_role_reclassify_expected_role_one import (
        ModelingOperationActionRoleReclassifyExpectedRoleOne,
    )
    from .modeling_operation_action_role_reclassify_expected_role_seven import (
        ModelingOperationActionRoleReclassifyExpectedRoleSeven,
    )
    from .modeling_operation_action_role_reclassify_expected_role_seventeen import (
        ModelingOperationActionRoleReclassifyExpectedRoleSeventeen,
    )
    from .modeling_operation_action_role_reclassify_expected_role_six import (
        ModelingOperationActionRoleReclassifyExpectedRoleSix,
    )
    from .modeling_operation_action_role_reclassify_expected_role_sixteen import (
        ModelingOperationActionRoleReclassifyExpectedRoleSixteen,
    )
    from .modeling_operation_action_role_reclassify_expected_role_ten import (
        ModelingOperationActionRoleReclassifyExpectedRoleTen,
    )
    from .modeling_operation_action_role_reclassify_expected_role_thirteen import (
        ModelingOperationActionRoleReclassifyExpectedRoleThirteen,
    )
    from .modeling_operation_action_role_reclassify_expected_role_three import (
        ModelingOperationActionRoleReclassifyExpectedRoleThree,
    )
    from .modeling_operation_action_role_reclassify_expected_role_twelve import (
        ModelingOperationActionRoleReclassifyExpectedRoleTwelve,
    )
    from .modeling_operation_action_role_reclassify_expected_role_two import (
        ModelingOperationActionRoleReclassifyExpectedRoleTwo,
    )
    from .modeling_operation_action_role_reclassify_expected_role_zero import (
        ModelingOperationActionRoleReclassifyExpectedRoleZero,
    )
    from .modeling_operation_action_role_reclassify_role import ModelingOperationActionRoleReclassifyRole
    from .modeling_operation_action_role_reclassify_role_eight import ModelingOperationActionRoleReclassifyRoleEight
    from .modeling_operation_action_role_reclassify_role_eleven import ModelingOperationActionRoleReclassifyRoleEleven
    from .modeling_operation_action_role_reclassify_role_fifteen import ModelingOperationActionRoleReclassifyRoleFifteen
    from .modeling_operation_action_role_reclassify_role_five import ModelingOperationActionRoleReclassifyRoleFive
    from .modeling_operation_action_role_reclassify_role_four import ModelingOperationActionRoleReclassifyRoleFour
    from .modeling_operation_action_role_reclassify_role_fourteen import (
        ModelingOperationActionRoleReclassifyRoleFourteen,
    )
    from .modeling_operation_action_role_reclassify_role_nine import ModelingOperationActionRoleReclassifyRoleNine
    from .modeling_operation_action_role_reclassify_role_one import ModelingOperationActionRoleReclassifyRoleOne
    from .modeling_operation_action_role_reclassify_role_seven import ModelingOperationActionRoleReclassifyRoleSeven
    from .modeling_operation_action_role_reclassify_role_seventeen import (
        ModelingOperationActionRoleReclassifyRoleSeventeen,
    )
    from .modeling_operation_action_role_reclassify_role_six import ModelingOperationActionRoleReclassifyRoleSix
    from .modeling_operation_action_role_reclassify_role_sixteen import ModelingOperationActionRoleReclassifyRoleSixteen
    from .modeling_operation_action_role_reclassify_role_ten import ModelingOperationActionRoleReclassifyRoleTen
    from .modeling_operation_action_role_reclassify_role_thirteen import (
        ModelingOperationActionRoleReclassifyRoleThirteen,
    )
    from .modeling_operation_action_role_reclassify_role_three import ModelingOperationActionRoleReclassifyRoleThree
    from .modeling_operation_action_role_reclassify_role_twelve import ModelingOperationActionRoleReclassifyRoleTwelve
    from .modeling_operation_action_role_reclassify_role_two import ModelingOperationActionRoleReclassifyRoleTwo
    from .modeling_operation_action_role_reclassify_role_zero import ModelingOperationActionRoleReclassifyRoleZero
    from .modeling_operation_action_symmetry_artmesh_bindings import ModelingOperationActionSymmetryArtmeshBindings
    from .modeling_operation_action_symmetry_artmesh_bindings_links_item import (
        ModelingOperationActionSymmetryArtmeshBindingsLinksItem,
    )
    from .modeling_operation_action_symmetry_artmesh_bindings_links_item_axis import (
        ModelingOperationActionSymmetryArtmeshBindingsLinksItemAxis,
    )
    from .modeling_operation_action_symmetry_artmesh_bindings_links_item_kind import (
        ModelingOperationActionSymmetryArtmeshBindingsLinksItemKind,
    )
    from .modeling_operation_action_symmetry_artmesh_bindings_links_item_kind_one import (
        ModelingOperationActionSymmetryArtmeshBindingsLinksItemKindOne,
    )
    from .modeling_operation_action_symmetry_artmesh_bindings_links_item_kind_three import (
        ModelingOperationActionSymmetryArtmeshBindingsLinksItemKindThree,
    )
    from .modeling_operation_action_symmetry_artmesh_bindings_links_item_kind_two import (
        ModelingOperationActionSymmetryArtmeshBindingsLinksItemKindTwo,
    )
    from .modeling_operation_action_symmetry_artmesh_bindings_links_item_kind_zero import (
        ModelingOperationActionSymmetryArtmeshBindingsLinksItemKindZero,
    )
    from .modeling_operation_action_symmetry_contract import ModelingOperationActionSymmetryContract
    from .modeling_operation_action_symmetry_contract_contract import ModelingOperationActionSymmetryContractContract
    from .modeling_operation_action_symmetry_contract_contract_axis import (
        ModelingOperationActionSymmetryContractContractAxis,
    )
    from .modeling_operation_action_symmetry_contract_contract_links_item import (
        ModelingOperationActionSymmetryContractContractLinksItem,
    )
    from .modeling_operation_action_symmetry_contract_contract_links_item_axis import (
        ModelingOperationActionSymmetryContractContractLinksItemAxis,
    )
    from .modeling_operation_action_symmetry_contract_contract_links_item_kind import (
        ModelingOperationActionSymmetryContractContractLinksItemKind,
    )
    from .modeling_operation_action_symmetry_contract_contract_links_item_kind_one import (
        ModelingOperationActionSymmetryContractContractLinksItemKindOne,
    )
    from .modeling_operation_action_symmetry_contract_contract_links_item_kind_three import (
        ModelingOperationActionSymmetryContractContractLinksItemKindThree,
    )
    from .modeling_operation_action_symmetry_contract_contract_links_item_kind_two import (
        ModelingOperationActionSymmetryContractContractLinksItemKindTwo,
    )
    from .modeling_operation_action_symmetry_contract_contract_links_item_kind_zero import (
        ModelingOperationActionSymmetryContractContractLinksItemKindZero,
    )
    from .modeling_operation_action_transform import ModelingOperationActionTransform
    from .modeling_operation_action_transform_operator import ModelingOperationActionTransformOperator
    from .modeling_operation_action_transform_operator_one import ModelingOperationActionTransformOperatorOne
    from .modeling_operation_action_transform_operator_two import ModelingOperationActionTransformOperatorTwo
    from .modeling_operation_action_transform_operator_zero import ModelingOperationActionTransformOperatorZero
    from .modeling_operation_action_transform_property import ModelingOperationActionTransformProperty
    from .modeling_operation_action_transform_property_five import ModelingOperationActionTransformPropertyFive
    from .modeling_operation_action_transform_property_four import ModelingOperationActionTransformPropertyFour
    from .modeling_operation_action_transform_property_one import ModelingOperationActionTransformPropertyOne
    from .modeling_operation_action_transform_property_three import ModelingOperationActionTransformPropertyThree
    from .modeling_operation_action_transform_property_two import ModelingOperationActionTransformPropertyTwo
    from .modeling_operation_action_transform_property_zero import ModelingOperationActionTransformPropertyZero
    from .modeling_operation_action_warp_pin_binding_key import ModelingOperationActionWarpPinBindingKey
    from .modeling_operation_action_warp_pin_binding_key_curve import ModelingOperationActionWarpPinBindingKeyCurve
    from .modeling_operation_action_warp_pin_binding_key_curve_control_points_item import (
        ModelingOperationActionWarpPinBindingKeyCurveControlPointsItem,
    )
    from .modeling_operation_action_warp_pin_binding_key_interpolation import (
        ModelingOperationActionWarpPinBindingKeyInterpolation,
    )
    from .modeling_operation_action_warp_pin_binding_key_interpolation_four import (
        ModelingOperationActionWarpPinBindingKeyInterpolationFour,
    )
    from .modeling_operation_action_warp_pin_binding_key_interpolation_one import (
        ModelingOperationActionWarpPinBindingKeyInterpolationOne,
    )
    from .modeling_operation_action_warp_pin_binding_key_interpolation_three import (
        ModelingOperationActionWarpPinBindingKeyInterpolationThree,
    )
    from .modeling_operation_action_warp_pin_binding_key_interpolation_two import (
        ModelingOperationActionWarpPinBindingKeyInterpolationTwo,
    )
    from .modeling_operation_action_warp_pin_binding_key_interpolation_zero import (
        ModelingOperationActionWarpPinBindingKeyInterpolationZero,
    )
    from .modeling_operation_action_warp_pin_binding_key_property import (
        ModelingOperationActionWarpPinBindingKeyProperty,
    )
    from .modeling_operation_action_warp_pin_binding_key_property_one import (
        ModelingOperationActionWarpPinBindingKeyPropertyOne,
    )
    from .modeling_operation_action_warp_pin_binding_key_property_zero import (
        ModelingOperationActionWarpPinBindingKeyPropertyZero,
    )
    from .modeling_operation_target import ModelingOperationTarget
    from .modeling_operation_target_roles_item import ModelingOperationTargetRolesItem
    from .modeling_operation_target_roles_item_eight import ModelingOperationTargetRolesItemEight
    from .modeling_operation_target_roles_item_eleven import ModelingOperationTargetRolesItemEleven
    from .modeling_operation_target_roles_item_fifteen import ModelingOperationTargetRolesItemFifteen
    from .modeling_operation_target_roles_item_five import ModelingOperationTargetRolesItemFive
    from .modeling_operation_target_roles_item_four import ModelingOperationTargetRolesItemFour
    from .modeling_operation_target_roles_item_fourteen import ModelingOperationTargetRolesItemFourteen
    from .modeling_operation_target_roles_item_nine import ModelingOperationTargetRolesItemNine
    from .modeling_operation_target_roles_item_one import ModelingOperationTargetRolesItemOne
    from .modeling_operation_target_roles_item_seven import ModelingOperationTargetRolesItemSeven
    from .modeling_operation_target_roles_item_seventeen import ModelingOperationTargetRolesItemSeventeen
    from .modeling_operation_target_roles_item_six import ModelingOperationTargetRolesItemSix
    from .modeling_operation_target_roles_item_sixteen import ModelingOperationTargetRolesItemSixteen
    from .modeling_operation_target_roles_item_ten import ModelingOperationTargetRolesItemTen
    from .modeling_operation_target_roles_item_thirteen import ModelingOperationTargetRolesItemThirteen
    from .modeling_operation_target_roles_item_three import ModelingOperationTargetRolesItemThree
    from .modeling_operation_target_roles_item_twelve import ModelingOperationTargetRolesItemTwelve
    from .modeling_operation_target_roles_item_two import ModelingOperationTargetRolesItemTwo
    from .modeling_operation_target_roles_item_zero import ModelingOperationTargetRolesItemZero
    from .motion_clip import MotionClip
    from .motion_clip_format import MotionClipFormat
    from .motion_clip_tracks_item import MotionClipTracksItem
    from .motion_clip_tracks_item_keys_item import MotionClipTracksItemKeysItem
    from .motion_clip_tracks_item_keys_item_segment import MotionClipTracksItemKeysItemSegment
    from .motion_clip_tracks_item_keys_item_segment_control1 import MotionClipTracksItemKeysItemSegmentControl1
    from .motion_clip_tracks_item_keys_item_segment_control1control1 import (
        MotionClipTracksItemKeysItemSegmentControl1Control1,
    )
    from .motion_clip_tracks_item_keys_item_segment_control1control2 import (
        MotionClipTracksItemKeysItemSegmentControl1Control2,
    )
    from .motion_clip_tracks_item_keys_item_segment_control1kind import MotionClipTracksItemKeysItemSegmentControl1Kind
    from .motion_clip_tracks_item_keys_item_segment_zero import MotionClipTracksItemKeysItemSegmentZero
    from .motion_clip_tracks_item_keys_item_segment_zero_kind import MotionClipTracksItemKeysItemSegmentZeroKind
    from .motion_clip_tracks_item_keys_item_segment_zero_kind_one import MotionClipTracksItemKeysItemSegmentZeroKindOne
    from .motion_clip_tracks_item_keys_item_segment_zero_kind_two import MotionClipTracksItemKeysItemSegmentZeroKindTwo
    from .motion_clip_tracks_item_keys_item_segment_zero_kind_zero import (
        MotionClipTracksItemKeysItemSegmentZeroKindZero,
    )
    from .motion_request import MotionRequest
    from .motion_request_clip import MotionRequestClip
    from .motion_request_clip_action import MotionRequestClipAction
    from .motion_request_clip_clip import MotionRequestClipClip
    from .motion_request_clip_clip_format import MotionRequestClipClipFormat
    from .motion_request_clip_clip_tracks_item import MotionRequestClipClipTracksItem
    from .motion_request_clip_clip_tracks_item_keys_item import MotionRequestClipClipTracksItemKeysItem
    from .motion_request_clip_clip_tracks_item_keys_item_segment import MotionRequestClipClipTracksItemKeysItemSegment
    from .motion_request_clip_clip_tracks_item_keys_item_segment_control1 import (
        MotionRequestClipClipTracksItemKeysItemSegmentControl1,
    )
    from .motion_request_clip_clip_tracks_item_keys_item_segment_control1control1 import (
        MotionRequestClipClipTracksItemKeysItemSegmentControl1Control1,
    )
    from .motion_request_clip_clip_tracks_item_keys_item_segment_control1control2 import (
        MotionRequestClipClipTracksItemKeysItemSegmentControl1Control2,
    )
    from .motion_request_clip_clip_tracks_item_keys_item_segment_control1kind import (
        MotionRequestClipClipTracksItemKeysItemSegmentControl1Kind,
    )
    from .motion_request_clip_clip_tracks_item_keys_item_segment_zero import (
        MotionRequestClipClipTracksItemKeysItemSegmentZero,
    )
    from .motion_request_clip_clip_tracks_item_keys_item_segment_zero_kind import (
        MotionRequestClipClipTracksItemKeysItemSegmentZeroKind,
    )
    from .motion_request_clip_clip_tracks_item_keys_item_segment_zero_kind_one import (
        MotionRequestClipClipTracksItemKeysItemSegmentZeroKindOne,
    )
    from .motion_request_clip_clip_tracks_item_keys_item_segment_zero_kind_two import (
        MotionRequestClipClipTracksItemKeysItemSegmentZeroKindTwo,
    )
    from .motion_request_clip_clip_tracks_item_keys_item_segment_zero_kind_zero import (
        MotionRequestClipClipTracksItemKeysItemSegmentZeroKindZero,
    )
    from .motion_request_loop import MotionRequestLoop
    from .motion_request_loop_action import MotionRequestLoopAction
    from .motion_request_one import MotionRequestOne
    from .motion_request_one_action import MotionRequestOneAction
    from .motion_request_one_action_one import MotionRequestOneActionOne
    from .motion_request_one_action_three import MotionRequestOneActionThree
    from .motion_request_one_action_two import MotionRequestOneActionTwo
    from .motion_request_one_action_zero import MotionRequestOneActionZero
    from .motion_request_time import MotionRequestTime
    from .motion_request_time_action import MotionRequestTimeAction
    from .post_api_bridge_pose_request import (
        PostApiBridgePoseRequest,
        PostApiBridgePoseRequest_ClearParameterValues,
        PostApiBridgePoseRequest_SetParameterValues,
    )
    from .post_api_bridge_pose_request_clear_parameter_values import PostApiBridgePoseRequestClearParameterValues
    from .post_api_bridge_pose_request_clear_parameter_values_data import (
        PostApiBridgePoseRequestClearParameterValuesData,
    )
    from .post_api_bridge_pose_request_set_parameter_values import PostApiBridgePoseRequestSetParameterValues
    from .post_api_bridge_pose_request_set_parameter_values_data import PostApiBridgePoseRequestSetParameterValuesData
    from .post_api_bridge_pose_request_set_parameter_values_data_parameters_item import (
        PostApiBridgePoseRequestSetParameterValuesDataParametersItem,
    )
    from .post_api_bridge_read_request import (
        PostApiBridgeReadRequest,
        PostApiBridgeReadRequest_GetCurrentDocumentUid,
        PostApiBridgeReadRequest_GetCurrentEditMode,
        PostApiBridgeReadRequest_GetCurrentModelUid,
        PostApiBridgeReadRequest_GetDeformerStructure,
        PostApiBridgeReadRequest_GetDocument,
        PostApiBridgeReadRequest_GetDocuments,
        PostApiBridgeReadRequest_GetObject,
        PostApiBridgeReadRequest_GetParameterGroups,
        PostApiBridgeReadRequest_GetParameterValues,
        PostApiBridgeReadRequest_GetParameters,
        PostApiBridgeReadRequest_GetPartStructure,
        PostApiBridgeReadRequest_GetPhysicsInfo,
    )
    from .post_api_bridge_read_request_get_current_document_uid import PostApiBridgeReadRequestGetCurrentDocumentUid
    from .post_api_bridge_read_request_get_current_document_uid_data import (
        PostApiBridgeReadRequestGetCurrentDocumentUidData,
    )
    from .post_api_bridge_read_request_get_current_edit_mode import PostApiBridgeReadRequestGetCurrentEditMode
    from .post_api_bridge_read_request_get_current_edit_mode_data import PostApiBridgeReadRequestGetCurrentEditModeData
    from .post_api_bridge_read_request_get_current_model_uid import PostApiBridgeReadRequestGetCurrentModelUid
    from .post_api_bridge_read_request_get_current_model_uid_data import PostApiBridgeReadRequestGetCurrentModelUidData
    from .post_api_bridge_read_request_get_deformer_structure import PostApiBridgeReadRequestGetDeformerStructure
    from .post_api_bridge_read_request_get_deformer_structure_data import (
        PostApiBridgeReadRequestGetDeformerStructureData,
    )
    from .post_api_bridge_read_request_get_document import PostApiBridgeReadRequestGetDocument
    from .post_api_bridge_read_request_get_document_data import PostApiBridgeReadRequestGetDocumentData
    from .post_api_bridge_read_request_get_documents import PostApiBridgeReadRequestGetDocuments
    from .post_api_bridge_read_request_get_documents_data import PostApiBridgeReadRequestGetDocumentsData
    from .post_api_bridge_read_request_get_object import PostApiBridgeReadRequestGetObject
    from .post_api_bridge_read_request_get_object_data import PostApiBridgeReadRequestGetObjectData
    from .post_api_bridge_read_request_get_parameter_groups import PostApiBridgeReadRequestGetParameterGroups
    from .post_api_bridge_read_request_get_parameter_groups_data import PostApiBridgeReadRequestGetParameterGroupsData
    from .post_api_bridge_read_request_get_parameter_values import PostApiBridgeReadRequestGetParameterValues
    from .post_api_bridge_read_request_get_parameter_values_data import PostApiBridgeReadRequestGetParameterValuesData
    from .post_api_bridge_read_request_get_parameters import PostApiBridgeReadRequestGetParameters
    from .post_api_bridge_read_request_get_parameters_data import PostApiBridgeReadRequestGetParametersData
    from .post_api_bridge_read_request_get_part_structure import PostApiBridgeReadRequestGetPartStructure
    from .post_api_bridge_read_request_get_part_structure_data import PostApiBridgeReadRequestGetPartStructureData
    from .post_api_bridge_read_request_get_physics_info import PostApiBridgeReadRequestGetPhysicsInfo
    from .post_api_bridge_read_request_get_physics_info_data import PostApiBridgeReadRequestGetPhysicsInfoData
    from .post_api_playback_control_request_command import PostApiPlaybackControlRequestCommand
    from .post_api_playback_control_request_mode import PostApiPlaybackControlRequestMode
    from .post_api_playback_control_response import PostApiPlaybackControlResponse
    from .post_api_playback_control_response_playback import PostApiPlaybackControlResponsePlayback
    from .post_api_playback_control_response_playback_demo import PostApiPlaybackControlResponsePlaybackDemo
    from .post_api_playback_control_response_playback_demo_mode import PostApiPlaybackControlResponsePlaybackDemoMode
    from .post_api_playback_control_response_playback_motion import PostApiPlaybackControlResponsePlaybackMotion
    from .post_api_playback_motion_request import PostApiPlaybackMotionRequest
    from .post_api_playback_motion_request_clip import PostApiPlaybackMotionRequestClip
    from .post_api_playback_motion_request_clip_action import PostApiPlaybackMotionRequestClipAction
    from .post_api_playback_motion_request_clip_clip import PostApiPlaybackMotionRequestClipClip
    from .post_api_playback_motion_request_clip_clip_format import PostApiPlaybackMotionRequestClipClipFormat
    from .post_api_playback_motion_request_clip_clip_tracks_item import PostApiPlaybackMotionRequestClipClipTracksItem
    from .post_api_playback_motion_request_clip_clip_tracks_item_keys_item import (
        PostApiPlaybackMotionRequestClipClipTracksItemKeysItem,
    )
    from .post_api_playback_motion_request_clip_clip_tracks_item_keys_item_segment import (
        PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegment,
    )
    from .post_api_playback_motion_request_clip_clip_tracks_item_keys_item_segment_control1 import (
        PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentControl1,
    )
    from .post_api_playback_motion_request_clip_clip_tracks_item_keys_item_segment_control1control1 import (
        PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentControl1Control1,
    )
    from .post_api_playback_motion_request_clip_clip_tracks_item_keys_item_segment_control1control2 import (
        PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentControl1Control2,
    )
    from .post_api_playback_motion_request_clip_clip_tracks_item_keys_item_segment_control1kind import (
        PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentControl1Kind,
    )
    from .post_api_playback_motion_request_clip_clip_tracks_item_keys_item_segment_zero import (
        PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentZero,
    )
    from .post_api_playback_motion_request_clip_clip_tracks_item_keys_item_segment_zero_kind import (
        PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentZeroKind,
    )
    from .post_api_playback_motion_request_clip_clip_tracks_item_keys_item_segment_zero_kind_one import (
        PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentZeroKindOne,
    )
    from .post_api_playback_motion_request_clip_clip_tracks_item_keys_item_segment_zero_kind_two import (
        PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentZeroKindTwo,
    )
    from .post_api_playback_motion_request_clip_clip_tracks_item_keys_item_segment_zero_kind_zero import (
        PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentZeroKindZero,
    )
    from .post_api_playback_motion_request_loop import PostApiPlaybackMotionRequestLoop
    from .post_api_playback_motion_request_loop_action import PostApiPlaybackMotionRequestLoopAction
    from .post_api_playback_motion_request_one import PostApiPlaybackMotionRequestOne
    from .post_api_playback_motion_request_one_action import PostApiPlaybackMotionRequestOneAction
    from .post_api_playback_motion_request_one_action_one import PostApiPlaybackMotionRequestOneActionOne
    from .post_api_playback_motion_request_one_action_three import PostApiPlaybackMotionRequestOneActionThree
    from .post_api_playback_motion_request_one_action_two import PostApiPlaybackMotionRequestOneActionTwo
    from .post_api_playback_motion_request_one_action_zero import PostApiPlaybackMotionRequestOneActionZero
    from .post_api_playback_motion_request_time import PostApiPlaybackMotionRequestTime
    from .post_api_playback_motion_request_time_action import PostApiPlaybackMotionRequestTimeAction
    from .post_api_playback_motion_response import PostApiPlaybackMotionResponse
    from .post_api_playback_motion_response_playback import PostApiPlaybackMotionResponsePlayback
    from .post_api_playback_motion_response_playback_demo import PostApiPlaybackMotionResponsePlaybackDemo
    from .post_api_playback_motion_response_playback_demo_mode import PostApiPlaybackMotionResponsePlaybackDemoMode
    from .post_api_playback_motion_response_playback_motion import PostApiPlaybackMotionResponsePlaybackMotion
    from .post_api_playback_parameters_response import PostApiPlaybackParametersResponse
    from .post_api_playback_parameters_response_playback import PostApiPlaybackParametersResponsePlayback
    from .post_api_playback_parameters_response_playback_demo import PostApiPlaybackParametersResponsePlaybackDemo
    from .post_api_playback_parameters_response_playback_demo_mode import (
        PostApiPlaybackParametersResponsePlaybackDemoMode,
    )
    from .post_api_playback_parameters_response_playback_motion import PostApiPlaybackParametersResponsePlaybackMotion
    from .post_api_playback_reload_response import PostApiPlaybackReloadResponse
    from .post_api_playback_reload_response_playback import PostApiPlaybackReloadResponsePlayback
    from .post_api_playback_reload_response_playback_demo import PostApiPlaybackReloadResponsePlaybackDemo
    from .post_api_playback_reload_response_playback_demo_mode import PostApiPlaybackReloadResponsePlaybackDemoMode
    from .post_api_playback_reload_response_playback_motion import PostApiPlaybackReloadResponsePlaybackMotion
    from .qa_check_request import QaCheckRequest
    from .qa_check_request_motion_sweep import QaCheckRequestMotionSweep
    from .qa_check_request_motion_sweep_check_monotonic import QaCheckRequestMotionSweepCheckMonotonic
    from .qa_check_request_pose_samples_item import QaCheckRequestPoseSamplesItem
    from .transaction_request import TransactionRequest
    from .transaction_request_checkpoint_id import TransactionRequestCheckpointId
    from .transaction_request_checkpoint_id_kind import TransactionRequestCheckpointIdKind
    from .transaction_request_operations import TransactionRequestOperations
    from .transaction_request_operations_operations_item import TransactionRequestOperationsOperationsItem
    from .transaction_request_operations_operations_item_action import (
        TransactionRequestOperationsOperationsItemAction,
        TransactionRequestOperationsOperationsItemAction_ArtmeshBindingKey,
        TransactionRequestOperationsOperationsItemAction_ArtmeshBlendShape,
        TransactionRequestOperationsOperationsItemAction_ArtmeshGenerate,
        TransactionRequestOperationsOperationsItemAction_ArtmeshMirrorKey,
        TransactionRequestOperationsOperationsItemAction_ArtmeshMultiKey,
        TransactionRequestOperationsOperationsItemAction_ArtmeshOffset,
        TransactionRequestOperationsOperationsItemAction_ArtmeshQuality,
        TransactionRequestOperationsOperationsItemAction_ArtmeshRebuild,
        TransactionRequestOperationsOperationsItemAction_BindingKey,
        TransactionRequestOperationsOperationsItemAction_BlendShapeSet,
        TransactionRequestOperationsOperationsItemAction_DeformBrush,
        TransactionRequestOperationsOperationsItemAction_DeformerBindingKey,
        TransactionRequestOperationsOperationsItemAction_DeformerBindingRemove,
        TransactionRequestOperationsOperationsItemAction_DeformerCreate,
        TransactionRequestOperationsOperationsItemAction_DeformerKindSet,
        TransactionRequestOperationsOperationsItemAction_DeformerOrigin,
        TransactionRequestOperationsOperationsItemAction_DeformerParentSet,
        TransactionRequestOperationsOperationsItemAction_DeformerRotationMetadata,
        TransactionRequestOperationsOperationsItemAction_DeformerSplit,
        TransactionRequestOperationsOperationsItemAction_DeformerTargetsSet,
        TransactionRequestOperationsOperationsItemAction_DeformerTransform,
        TransactionRequestOperationsOperationsItemAction_ParameterAdd,
        TransactionRequestOperationsOperationsItemAction_PartAlphaReveal,
        TransactionRequestOperationsOperationsItemAction_PartBlendMode,
        TransactionRequestOperationsOperationsItemAction_PartClip,
        TransactionRequestOperationsOperationsItemAction_PartContourShade,
        TransactionRequestOperationsOperationsItemAction_PartDrawOrder,
        TransactionRequestOperationsOperationsItemAction_PartTint,
        TransactionRequestOperationsOperationsItemAction_PartVisibility,
        TransactionRequestOperationsOperationsItemAction_RoleConfirm,
        TransactionRequestOperationsOperationsItemAction_RoleReclassify,
        TransactionRequestOperationsOperationsItemAction_SymmetryArtmeshBindings,
        TransactionRequestOperationsOperationsItemAction_SymmetryContract,
        TransactionRequestOperationsOperationsItemAction_Transform,
        TransactionRequestOperationsOperationsItemAction_WarpPinBindingKey,
    )
    from .transaction_request_operations_operations_item_action_artmesh_binding_key import (
        TransactionRequestOperationsOperationsItemActionArtmeshBindingKey,
    )
    from .transaction_request_operations_operations_item_action_artmesh_binding_key_curve import (
        TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyCurve,
    )
    from .transaction_request_operations_operations_item_action_artmesh_binding_key_curve_control_points_item import (
        TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyCurveControlPointsItem,
    )
    from .transaction_request_operations_operations_item_action_artmesh_binding_key_interpolation import (
        TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyInterpolation,
    )
    from .transaction_request_operations_operations_item_action_artmesh_binding_key_interpolation_four import (
        TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyInterpolationFour,
    )
    from .transaction_request_operations_operations_item_action_artmesh_binding_key_interpolation_one import (
        TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyInterpolationOne,
    )
    from .transaction_request_operations_operations_item_action_artmesh_binding_key_interpolation_three import (
        TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyInterpolationThree,
    )
    from .transaction_request_operations_operations_item_action_artmesh_binding_key_interpolation_two import (
        TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyInterpolationTwo,
    )
    from .transaction_request_operations_operations_item_action_artmesh_binding_key_interpolation_zero import (
        TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyInterpolationZero,
    )
    from .transaction_request_operations_operations_item_action_artmesh_binding_key_offsets_item import (
        TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyOffsetsItem,
    )
    from .transaction_request_operations_operations_item_action_artmesh_blend_shape import (
        TransactionRequestOperationsOperationsItemActionArtmeshBlendShape,
    )
    from .transaction_request_operations_operations_item_action_artmesh_blend_shape_curve import (
        TransactionRequestOperationsOperationsItemActionArtmeshBlendShapeCurve,
    )
    from .transaction_request_operations_operations_item_action_artmesh_blend_shape_curve_control_points_item import (
        TransactionRequestOperationsOperationsItemActionArtmeshBlendShapeCurveControlPointsItem,
    )
    from .transaction_request_operations_operations_item_action_artmesh_blend_shape_interpolation import (
        TransactionRequestOperationsOperationsItemActionArtmeshBlendShapeInterpolation,
    )
    from .transaction_request_operations_operations_item_action_artmesh_blend_shape_interpolation_four import (
        TransactionRequestOperationsOperationsItemActionArtmeshBlendShapeInterpolationFour,
    )
    from .transaction_request_operations_operations_item_action_artmesh_blend_shape_interpolation_one import (
        TransactionRequestOperationsOperationsItemActionArtmeshBlendShapeInterpolationOne,
    )
    from .transaction_request_operations_operations_item_action_artmesh_blend_shape_interpolation_three import (
        TransactionRequestOperationsOperationsItemActionArtmeshBlendShapeInterpolationThree,
    )
    from .transaction_request_operations_operations_item_action_artmesh_blend_shape_interpolation_two import (
        TransactionRequestOperationsOperationsItemActionArtmeshBlendShapeInterpolationTwo,
    )
    from .transaction_request_operations_operations_item_action_artmesh_blend_shape_interpolation_zero import (
        TransactionRequestOperationsOperationsItemActionArtmeshBlendShapeInterpolationZero,
    )
    from .transaction_request_operations_operations_item_action_artmesh_blend_shape_offsets_item import (
        TransactionRequestOperationsOperationsItemActionArtmeshBlendShapeOffsetsItem,
    )
    from .transaction_request_operations_operations_item_action_artmesh_generate import (
        TransactionRequestOperationsOperationsItemActionArtmeshGenerate,
    )
    from .transaction_request_operations_operations_item_action_artmesh_generate_preset import (
        TransactionRequestOperationsOperationsItemActionArtmeshGeneratePreset,
    )
    from .transaction_request_operations_operations_item_action_artmesh_generate_preset_five import (
        TransactionRequestOperationsOperationsItemActionArtmeshGeneratePresetFive,
    )
    from .transaction_request_operations_operations_item_action_artmesh_generate_preset_four import (
        TransactionRequestOperationsOperationsItemActionArtmeshGeneratePresetFour,
    )
    from .transaction_request_operations_operations_item_action_artmesh_generate_preset_one import (
        TransactionRequestOperationsOperationsItemActionArtmeshGeneratePresetOne,
    )
    from .transaction_request_operations_operations_item_action_artmesh_generate_preset_three import (
        TransactionRequestOperationsOperationsItemActionArtmeshGeneratePresetThree,
    )
    from .transaction_request_operations_operations_item_action_artmesh_generate_preset_two import (
        TransactionRequestOperationsOperationsItemActionArtmeshGeneratePresetTwo,
    )
    from .transaction_request_operations_operations_item_action_artmesh_generate_preset_zero import (
        TransactionRequestOperationsOperationsItemActionArtmeshGeneratePresetZero,
    )
    from .transaction_request_operations_operations_item_action_artmesh_generate_quality import (
        TransactionRequestOperationsOperationsItemActionArtmeshGenerateQuality,
    )
    from .transaction_request_operations_operations_item_action_artmesh_generate_topology import (
        TransactionRequestOperationsOperationsItemActionArtmeshGenerateTopology,
    )
    from .transaction_request_operations_operations_item_action_artmesh_generate_topology_one import (
        TransactionRequestOperationsOperationsItemActionArtmeshGenerateTopologyOne,
    )
    from .transaction_request_operations_operations_item_action_artmesh_generate_topology_zero import (
        TransactionRequestOperationsOperationsItemActionArtmeshGenerateTopologyZero,
    )
    from .transaction_request_operations_operations_item_action_artmesh_mirror_key import (
        TransactionRequestOperationsOperationsItemActionArtmeshMirrorKey,
    )
    from .transaction_request_operations_operations_item_action_artmesh_mirror_key_curve import (
        TransactionRequestOperationsOperationsItemActionArtmeshMirrorKeyCurve,
    )
    from .transaction_request_operations_operations_item_action_artmesh_mirror_key_curve_control_points_item import (
        TransactionRequestOperationsOperationsItemActionArtmeshMirrorKeyCurveControlPointsItem,
    )
    from .transaction_request_operations_operations_item_action_artmesh_mirror_key_interpolation import (
        TransactionRequestOperationsOperationsItemActionArtmeshMirrorKeyInterpolation,
    )
    from .transaction_request_operations_operations_item_action_artmesh_mirror_key_interpolation_four import (
        TransactionRequestOperationsOperationsItemActionArtmeshMirrorKeyInterpolationFour,
    )
    from .transaction_request_operations_operations_item_action_artmesh_mirror_key_interpolation_one import (
        TransactionRequestOperationsOperationsItemActionArtmeshMirrorKeyInterpolationOne,
    )
    from .transaction_request_operations_operations_item_action_artmesh_mirror_key_interpolation_three import (
        TransactionRequestOperationsOperationsItemActionArtmeshMirrorKeyInterpolationThree,
    )
    from .transaction_request_operations_operations_item_action_artmesh_mirror_key_interpolation_two import (
        TransactionRequestOperationsOperationsItemActionArtmeshMirrorKeyInterpolationTwo,
    )
    from .transaction_request_operations_operations_item_action_artmesh_mirror_key_interpolation_zero import (
        TransactionRequestOperationsOperationsItemActionArtmeshMirrorKeyInterpolationZero,
    )
    from .transaction_request_operations_operations_item_action_artmesh_multi_key import (
        TransactionRequestOperationsOperationsItemActionArtmeshMultiKey,
    )
    from .transaction_request_operations_operations_item_action_artmesh_multi_key_curve import (
        TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyCurve,
    )
    from .transaction_request_operations_operations_item_action_artmesh_multi_key_curve_control_points_item import (
        TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyCurveControlPointsItem,
    )
    from .transaction_request_operations_operations_item_action_artmesh_multi_key_interpolation import (
        TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyInterpolation,
    )
    from .transaction_request_operations_operations_item_action_artmesh_multi_key_interpolation_four import (
        TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyInterpolationFour,
    )
    from .transaction_request_operations_operations_item_action_artmesh_multi_key_interpolation_one import (
        TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyInterpolationOne,
    )
    from .transaction_request_operations_operations_item_action_artmesh_multi_key_interpolation_three import (
        TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyInterpolationThree,
    )
    from .transaction_request_operations_operations_item_action_artmesh_multi_key_interpolation_two import (
        TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyInterpolationTwo,
    )
    from .transaction_request_operations_operations_item_action_artmesh_multi_key_interpolation_zero import (
        TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyInterpolationZero,
    )
    from .transaction_request_operations_operations_item_action_artmesh_multi_key_offsets_item import (
        TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyOffsetsItem,
    )
    from .transaction_request_operations_operations_item_action_artmesh_offset import (
        TransactionRequestOperationsOperationsItemActionArtmeshOffset,
    )
    from .transaction_request_operations_operations_item_action_artmesh_offset_uv import (
        TransactionRequestOperationsOperationsItemActionArtmeshOffsetUv,
    )
    from .transaction_request_operations_operations_item_action_artmesh_quality import (
        TransactionRequestOperationsOperationsItemActionArtmeshQuality,
    )
    from .transaction_request_operations_operations_item_action_artmesh_quality_quality import (
        TransactionRequestOperationsOperationsItemActionArtmeshQualityQuality,
    )
    from .transaction_request_operations_operations_item_action_artmesh_rebuild import (
        TransactionRequestOperationsOperationsItemActionArtmeshRebuild,
    )
    from .transaction_request_operations_operations_item_action_artmesh_rebuild_preset import (
        TransactionRequestOperationsOperationsItemActionArtmeshRebuildPreset,
    )
    from .transaction_request_operations_operations_item_action_artmesh_rebuild_preset_five import (
        TransactionRequestOperationsOperationsItemActionArtmeshRebuildPresetFive,
    )
    from .transaction_request_operations_operations_item_action_artmesh_rebuild_preset_four import (
        TransactionRequestOperationsOperationsItemActionArtmeshRebuildPresetFour,
    )
    from .transaction_request_operations_operations_item_action_artmesh_rebuild_preset_one import (
        TransactionRequestOperationsOperationsItemActionArtmeshRebuildPresetOne,
    )
    from .transaction_request_operations_operations_item_action_artmesh_rebuild_preset_three import (
        TransactionRequestOperationsOperationsItemActionArtmeshRebuildPresetThree,
    )
    from .transaction_request_operations_operations_item_action_artmesh_rebuild_preset_two import (
        TransactionRequestOperationsOperationsItemActionArtmeshRebuildPresetTwo,
    )
    from .transaction_request_operations_operations_item_action_artmesh_rebuild_preset_zero import (
        TransactionRequestOperationsOperationsItemActionArtmeshRebuildPresetZero,
    )
    from .transaction_request_operations_operations_item_action_artmesh_rebuild_quality import (
        TransactionRequestOperationsOperationsItemActionArtmeshRebuildQuality,
    )
    from .transaction_request_operations_operations_item_action_artmesh_rebuild_topology import (
        TransactionRequestOperationsOperationsItemActionArtmeshRebuildTopology,
    )
    from .transaction_request_operations_operations_item_action_artmesh_rebuild_topology_one import (
        TransactionRequestOperationsOperationsItemActionArtmeshRebuildTopologyOne,
    )
    from .transaction_request_operations_operations_item_action_artmesh_rebuild_topology_zero import (
        TransactionRequestOperationsOperationsItemActionArtmeshRebuildTopologyZero,
    )
    from .transaction_request_operations_operations_item_action_binding_key import (
        TransactionRequestOperationsOperationsItemActionBindingKey,
    )
    from .transaction_request_operations_operations_item_action_binding_key_curve import (
        TransactionRequestOperationsOperationsItemActionBindingKeyCurve,
    )
    from .transaction_request_operations_operations_item_action_binding_key_curve_control_points_item import (
        TransactionRequestOperationsOperationsItemActionBindingKeyCurveControlPointsItem,
    )
    from .transaction_request_operations_operations_item_action_binding_key_interpolation import (
        TransactionRequestOperationsOperationsItemActionBindingKeyInterpolation,
    )
    from .transaction_request_operations_operations_item_action_binding_key_interpolation_four import (
        TransactionRequestOperationsOperationsItemActionBindingKeyInterpolationFour,
    )
    from .transaction_request_operations_operations_item_action_binding_key_interpolation_one import (
        TransactionRequestOperationsOperationsItemActionBindingKeyInterpolationOne,
    )
    from .transaction_request_operations_operations_item_action_binding_key_interpolation_three import (
        TransactionRequestOperationsOperationsItemActionBindingKeyInterpolationThree,
    )
    from .transaction_request_operations_operations_item_action_binding_key_interpolation_two import (
        TransactionRequestOperationsOperationsItemActionBindingKeyInterpolationTwo,
    )
    from .transaction_request_operations_operations_item_action_binding_key_interpolation_zero import (
        TransactionRequestOperationsOperationsItemActionBindingKeyInterpolationZero,
    )
    from .transaction_request_operations_operations_item_action_binding_key_property import (
        TransactionRequestOperationsOperationsItemActionBindingKeyProperty,
    )
    from .transaction_request_operations_operations_item_action_binding_key_property_five import (
        TransactionRequestOperationsOperationsItemActionBindingKeyPropertyFive,
    )
    from .transaction_request_operations_operations_item_action_binding_key_property_four import (
        TransactionRequestOperationsOperationsItemActionBindingKeyPropertyFour,
    )
    from .transaction_request_operations_operations_item_action_binding_key_property_one import (
        TransactionRequestOperationsOperationsItemActionBindingKeyPropertyOne,
    )
    from .transaction_request_operations_operations_item_action_binding_key_property_three import (
        TransactionRequestOperationsOperationsItemActionBindingKeyPropertyThree,
    )
    from .transaction_request_operations_operations_item_action_binding_key_property_two import (
        TransactionRequestOperationsOperationsItemActionBindingKeyPropertyTwo,
    )
    from .transaction_request_operations_operations_item_action_binding_key_property_zero import (
        TransactionRequestOperationsOperationsItemActionBindingKeyPropertyZero,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSet,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShape,
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShape_ArtPath,
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShape_Deformer,
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShape_Glue,
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShape_Part,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_art_path import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPath,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_art_path_curve import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathCurve,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_art_path_curve_control_points_item import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathCurveControlPointsItem,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_art_path_interpolation import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathInterpolation,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_art_path_interpolation_four import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathInterpolationFour,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_art_path_interpolation_one import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathInterpolationOne,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_art_path_interpolation_three import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathInterpolationThree,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_art_path_interpolation_two import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathInterpolationTwo,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_art_path_interpolation_zero import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathInterpolationZero,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_art_path_points_item import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathPointsItem,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformer,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_curve import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerCurve,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_curve_control_points_item import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerCurveControlPointsItem,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_interpolation import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerInterpolation,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_interpolation_four import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerInterpolationFour,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_interpolation_one import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerInterpolationOne,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_interpolation_three import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerInterpolationThree,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_interpolation_two import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerInterpolationTwo,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_interpolation_zero import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerInterpolationZero,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_pins_item import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerPinsItem,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_shared_points_item import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerSharedPointsItem,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_transform import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerTransform,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_warp import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerWarp,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_glue import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeGlue,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_glue_curve import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeGlueCurve,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_glue_curve_control_points_item import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeGlueCurveControlPointsItem,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_glue_interpolation import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeGlueInterpolation,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_glue_interpolation_four import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeGlueInterpolationFour,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_glue_interpolation_one import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeGlueInterpolationOne,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_glue_interpolation_three import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeGlueInterpolationThree,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_glue_interpolation_two import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeGlueInterpolationTwo,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_glue_interpolation_zero import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeGlueInterpolationZero,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_part import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePart,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_part_curve import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartCurve,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_part_curve_control_points_item import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartCurveControlPointsItem,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_part_interpolation import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartInterpolation,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_part_interpolation_four import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartInterpolationFour,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_part_interpolation_one import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartInterpolationOne,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_part_interpolation_three import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartInterpolationThree,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_part_interpolation_two import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartInterpolationTwo,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_part_interpolation_zero import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartInterpolationZero,
    )
    from .transaction_request_operations_operations_item_action_blend_shape_set_shape_part_transform import (
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartTransform,
    )
    from .transaction_request_operations_operations_item_action_deform_brush import (
        TransactionRequestOperationsOperationsItemActionDeformBrush,
    )
    from .transaction_request_operations_operations_item_action_deform_brush_brush import (
        TransactionRequestOperationsOperationsItemActionDeformBrushBrush,
    )
    from .transaction_request_operations_operations_item_action_deform_brush_brush_destination import (
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestination,
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestination_Base,
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestination_BlendShape,
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestination_Keyform,
    )
    from .transaction_request_operations_operations_item_action_deform_brush_brush_destination_base import (
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBase,
    )
    from .transaction_request_operations_operations_item_action_deform_brush_brush_destination_blend_shape import (
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShape,
    )
    from .transaction_request_operations_operations_item_action_deform_brush_brush_destination_blend_shape_shape import (
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShapeShape,
    )
    from .transaction_request_operations_operations_item_action_deform_brush_brush_destination_blend_shape_shape_curve import (
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShapeShapeCurve,
    )
    from .transaction_request_operations_operations_item_action_deform_brush_brush_destination_blend_shape_shape_curve_control_points_item import (
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShapeShapeCurveControlPointsItem,
    )
    from .transaction_request_operations_operations_item_action_deform_brush_brush_destination_blend_shape_shape_interpolation import (
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShapeShapeInterpolation,
    )
    from .transaction_request_operations_operations_item_action_deform_brush_brush_destination_blend_shape_shape_interpolation_four import (
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShapeShapeInterpolationFour,
    )
    from .transaction_request_operations_operations_item_action_deform_brush_brush_destination_blend_shape_shape_interpolation_one import (
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShapeShapeInterpolationOne,
    )
    from .transaction_request_operations_operations_item_action_deform_brush_brush_destination_blend_shape_shape_interpolation_three import (
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShapeShapeInterpolationThree,
    )
    from .transaction_request_operations_operations_item_action_deform_brush_brush_destination_blend_shape_shape_interpolation_two import (
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShapeShapeInterpolationTwo,
    )
    from .transaction_request_operations_operations_item_action_deform_brush_brush_destination_blend_shape_shape_interpolation_zero import (
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShapeShapeInterpolationZero,
    )
    from .transaction_request_operations_operations_item_action_deform_brush_brush_destination_keyform import (
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationKeyform,
    )
    from .transaction_request_operations_operations_item_action_deform_brush_brush_effect import (
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffect,
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffect_Bend,
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffect_ContourFollow,
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffect_Inflate,
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffect_Pinch,
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffect_Relax,
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffect_Smooth,
    )
    from .transaction_request_operations_operations_item_action_deform_brush_brush_effect_bend import (
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffectBend,
    )
    from .transaction_request_operations_operations_item_action_deform_brush_brush_effect_contour_follow import (
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffectContourFollow,
    )
    from .transaction_request_operations_operations_item_action_deform_brush_brush_effect_inflate import (
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffectInflate,
    )
    from .transaction_request_operations_operations_item_action_deform_brush_brush_effect_pinch import (
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffectPinch,
    )
    from .transaction_request_operations_operations_item_action_deform_brush_brush_effect_relax import (
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffectRelax,
    )
    from .transaction_request_operations_operations_item_action_deform_brush_brush_effect_smooth import (
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffectSmooth,
    )
    from .transaction_request_operations_operations_item_action_deform_brush_brush_falloff import (
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushFalloff,
    )
    from .transaction_request_operations_operations_item_action_deform_brush_brush_falloff_one import (
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushFalloffOne,
    )
    from .transaction_request_operations_operations_item_action_deform_brush_brush_falloff_zero import (
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushFalloffZero,
    )
    from .transaction_request_operations_operations_item_action_deform_brush_brush_surface import (
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurface,
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurface_Artmesh,
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurface_SharedWarp,
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurface_WarpPins,
    )
    from .transaction_request_operations_operations_item_action_deform_brush_brush_surface_artmesh import (
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurfaceArtmesh,
    )
    from .transaction_request_operations_operations_item_action_deform_brush_brush_surface_artmesh_space import (
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurfaceArtmeshSpace,
    )
    from .transaction_request_operations_operations_item_action_deform_brush_brush_surface_shared_warp import (
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurfaceSharedWarp,
    )
    from .transaction_request_operations_operations_item_action_deform_brush_brush_surface_shared_warp_space import (
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurfaceSharedWarpSpace,
    )
    from .transaction_request_operations_operations_item_action_deform_brush_brush_surface_warp_pins import (
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurfaceWarpPins,
    )
    from .transaction_request_operations_operations_item_action_deform_brush_brush_surface_warp_pins_space import (
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurfaceWarpPinsSpace,
    )
    from .transaction_request_operations_operations_item_action_deformer_binding_key import (
        TransactionRequestOperationsOperationsItemActionDeformerBindingKey,
    )
    from .transaction_request_operations_operations_item_action_deformer_binding_key_curve import (
        TransactionRequestOperationsOperationsItemActionDeformerBindingKeyCurve,
    )
    from .transaction_request_operations_operations_item_action_deformer_binding_key_curve_control_points_item import (
        TransactionRequestOperationsOperationsItemActionDeformerBindingKeyCurveControlPointsItem,
    )
    from .transaction_request_operations_operations_item_action_deformer_binding_key_interpolation import (
        TransactionRequestOperationsOperationsItemActionDeformerBindingKeyInterpolation,
    )
    from .transaction_request_operations_operations_item_action_deformer_binding_key_interpolation_four import (
        TransactionRequestOperationsOperationsItemActionDeformerBindingKeyInterpolationFour,
    )
    from .transaction_request_operations_operations_item_action_deformer_binding_key_interpolation_one import (
        TransactionRequestOperationsOperationsItemActionDeformerBindingKeyInterpolationOne,
    )
    from .transaction_request_operations_operations_item_action_deformer_binding_key_interpolation_three import (
        TransactionRequestOperationsOperationsItemActionDeformerBindingKeyInterpolationThree,
    )
    from .transaction_request_operations_operations_item_action_deformer_binding_key_interpolation_two import (
        TransactionRequestOperationsOperationsItemActionDeformerBindingKeyInterpolationTwo,
    )
    from .transaction_request_operations_operations_item_action_deformer_binding_key_interpolation_zero import (
        TransactionRequestOperationsOperationsItemActionDeformerBindingKeyInterpolationZero,
    )
    from .transaction_request_operations_operations_item_action_deformer_binding_key_property import (
        TransactionRequestOperationsOperationsItemActionDeformerBindingKeyProperty,
    )
    from .transaction_request_operations_operations_item_action_deformer_binding_key_property_eight import (
        TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertyEight,
    )
    from .transaction_request_operations_operations_item_action_deformer_binding_key_property_five import (
        TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertyFive,
    )
    from .transaction_request_operations_operations_item_action_deformer_binding_key_property_four import (
        TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertyFour,
    )
    from .transaction_request_operations_operations_item_action_deformer_binding_key_property_nine import (
        TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertyNine,
    )
    from .transaction_request_operations_operations_item_action_deformer_binding_key_property_one import (
        TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertyOne,
    )
    from .transaction_request_operations_operations_item_action_deformer_binding_key_property_seven import (
        TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertySeven,
    )
    from .transaction_request_operations_operations_item_action_deformer_binding_key_property_six import (
        TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertySix,
    )
    from .transaction_request_operations_operations_item_action_deformer_binding_key_property_three import (
        TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertyThree,
    )
    from .transaction_request_operations_operations_item_action_deformer_binding_key_property_two import (
        TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertyTwo,
    )
    from .transaction_request_operations_operations_item_action_deformer_binding_key_property_zero import (
        TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertyZero,
    )
    from .transaction_request_operations_operations_item_action_deformer_binding_remove import (
        TransactionRequestOperationsOperationsItemActionDeformerBindingRemove,
    )
    from .transaction_request_operations_operations_item_action_deformer_binding_remove_property import (
        TransactionRequestOperationsOperationsItemActionDeformerBindingRemoveProperty,
    )
    from .transaction_request_operations_operations_item_action_deformer_binding_remove_property_eight import (
        TransactionRequestOperationsOperationsItemActionDeformerBindingRemovePropertyEight,
    )
    from .transaction_request_operations_operations_item_action_deformer_binding_remove_property_five import (
        TransactionRequestOperationsOperationsItemActionDeformerBindingRemovePropertyFive,
    )
    from .transaction_request_operations_operations_item_action_deformer_binding_remove_property_four import (
        TransactionRequestOperationsOperationsItemActionDeformerBindingRemovePropertyFour,
    )
    from .transaction_request_operations_operations_item_action_deformer_binding_remove_property_nine import (
        TransactionRequestOperationsOperationsItemActionDeformerBindingRemovePropertyNine,
    )
    from .transaction_request_operations_operations_item_action_deformer_binding_remove_property_one import (
        TransactionRequestOperationsOperationsItemActionDeformerBindingRemovePropertyOne,
    )
    from .transaction_request_operations_operations_item_action_deformer_binding_remove_property_seven import (
        TransactionRequestOperationsOperationsItemActionDeformerBindingRemovePropertySeven,
    )
    from .transaction_request_operations_operations_item_action_deformer_binding_remove_property_six import (
        TransactionRequestOperationsOperationsItemActionDeformerBindingRemovePropertySix,
    )
    from .transaction_request_operations_operations_item_action_deformer_binding_remove_property_three import (
        TransactionRequestOperationsOperationsItemActionDeformerBindingRemovePropertyThree,
    )
    from .transaction_request_operations_operations_item_action_deformer_binding_remove_property_two import (
        TransactionRequestOperationsOperationsItemActionDeformerBindingRemovePropertyTwo,
    )
    from .transaction_request_operations_operations_item_action_deformer_binding_remove_property_zero import (
        TransactionRequestOperationsOperationsItemActionDeformerBindingRemovePropertyZero,
    )
    from .transaction_request_operations_operations_item_action_deformer_create import (
        TransactionRequestOperationsOperationsItemActionDeformerCreate,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformer,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItem,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_composition import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemComposition,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_composition_one import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemCompositionOne,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_composition_zero import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemCompositionZero,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_curve import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemCurve,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_curve_control_points_item import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemCurveControlPointsItem,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_interpolation import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemInterpolation,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_interpolation_four import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemInterpolationFour,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_interpolation_one import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemInterpolationOne,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_interpolation_three import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemInterpolationThree,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_interpolation_two import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemInterpolationTwo,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_interpolation_zero import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemInterpolationZero,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_keys_item import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemKeysItem,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_property import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemProperty,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_property_eight import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemPropertyEight,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_property_five import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemPropertyFive,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_property_four import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemPropertyFour,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_property_nine import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemPropertyNine,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_property_one import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemPropertyOne,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_property_seven import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemPropertySeven,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_property_six import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemPropertySix,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_property_three import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemPropertyThree,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_property_two import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemPropertyTwo,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_property_zero import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemPropertyZero,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItem,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item_curve import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemCurve,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item_curve_control_points_item import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemCurveControlPointsItem,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item_interpolation import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemInterpolation,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item_interpolation_four import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemInterpolationFour,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item_interpolation_one import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemInterpolationOne,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item_interpolation_three import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemInterpolationThree,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item_interpolation_two import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemInterpolationTwo,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item_interpolation_zero import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemInterpolationZero,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item_kind import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemKind,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item_pins_item import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemPinsItem,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item_shared_points_item import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemSharedPointsItem,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item_transform import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemTransform,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item_warp import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemWarp,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_kind import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerKind,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_kind_one import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerKindOne,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_kind_two import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerKindTwo,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_kind_zero import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerKindZero,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItem,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_composition import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemComposition,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_composition_one import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemCompositionOne,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_composition_zero import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemCompositionZero,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_curve import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemCurve,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_curve_control_points_item import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemCurveControlPointsItem,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_interpolation import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemInterpolation,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_interpolation_four import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemInterpolationFour,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_interpolation_one import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemInterpolationOne,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_interpolation_three import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemInterpolationThree,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_interpolation_two import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemInterpolationTwo,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_interpolation_zero import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemInterpolationZero,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_keyforms_item import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemKeyformsItem,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_property import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemProperty,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_property_eight import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertyEight,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_property_eleven import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertyEleven,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_property_five import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertyFive,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_property_four import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertyFour,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_property_nine import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertyNine,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_property_one import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertyOne,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_property_seven import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertySeven,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_property_six import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertySix,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_property_ten import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertyTen,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_property_three import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertyThree,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_property_two import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertyTwo,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_property_zero import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertyZero,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_origin import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerOrigin,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadata,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata_angle_range import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataAngleRange,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata_angle_unit import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataAngleUnit,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata_parent_composition import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataParentComposition,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata_parent_composition_one import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataParentCompositionOne,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata_parent_composition_zero import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataParentCompositionZero,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata_pivot import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataPivot,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata_pivot_space import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataPivotSpace,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata_pivot_space_one import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataPivotSpaceOne,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata_pivot_space_zero import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataPivotSpaceZero,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata_shape_preservation import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataShapePreservation,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata_shape_preservation_one import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataShapePreservationOne,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata_shape_preservation_two import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataShapePreservationTwo,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata_shape_preservation_zero import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataShapePreservationZero,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarp,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_bounds import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpBounds,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_control_points_item import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItem,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItem,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_curve import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemCurve,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_curve_control_points_item import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemCurveControlPointsItem,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_interpolation import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolation,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_interpolation_four import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolationFour,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_interpolation_one import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolationOne,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_interpolation_three import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolationThree,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_interpolation_two import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolationTwo,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_interpolation_zero import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolationZero,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_keys_item import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemKeysItem,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_property import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemProperty,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_property_one import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemPropertyOne,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_property_zero import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemPropertyZero,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_grid import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpGrid,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_transform import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerTransform,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarp,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_grid import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpGrid,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pin_blend_mode import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinBlendMode,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pin_blend_mode_one import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinBlendModeOne,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pin_blend_mode_zero import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinBlendModeZero,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItem,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_bindings_item import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItem,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_bindings_item_curve import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemCurve,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_bindings_item_curve_control_points_item import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemCurveControlPointsItem,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_bindings_item_interpolation import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolation,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_bindings_item_interpolation_four import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolationFour,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_bindings_item_interpolation_one import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolationOne,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_bindings_item_interpolation_three import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolationThree,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_bindings_item_interpolation_two import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolationTwo,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_bindings_item_interpolation_zero import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolationZero,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_bindings_item_keys_item import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemKeysItem,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_bindings_item_property import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemProperty,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_bindings_item_property_one import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemPropertyOne,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_bindings_item_property_zero import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemPropertyZero,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_multi_bindings_item import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItem,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_curve import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemCurve,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_curve_control_points_item import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemCurveControlPointsItem,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_interpolation import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolation,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_interpolation_four import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolationFour,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_interpolation_one import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolationOne,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_interpolation_three import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolationThree,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_interpolation_two import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolationTwo,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_interpolation_zero import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolationZero,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_keyforms_item import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemKeyformsItem,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_property import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemProperty,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_property_one import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemPropertyOne,
    )
    from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_property_zero import (
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemPropertyZero,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSet,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_kind import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetKind,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_kind_one import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetKindOne,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_kind_two import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetKindTwo,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_kind_zero import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetKindZero,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_warp import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarp,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_grid import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpGrid,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pin_blend_mode import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinBlendMode,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pin_blend_mode_one import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinBlendModeOne,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pin_blend_mode_zero import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinBlendModeZero,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItem,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_bindings_item import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItem,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_bindings_item_curve import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemCurve,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_bindings_item_curve_control_points_item import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemCurveControlPointsItem,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_bindings_item_interpolation import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemInterpolation,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_bindings_item_interpolation_four import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemInterpolationFour,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_bindings_item_interpolation_one import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemInterpolationOne,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_bindings_item_interpolation_three import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemInterpolationThree,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_bindings_item_interpolation_two import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemInterpolationTwo,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_bindings_item_interpolation_zero import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemInterpolationZero,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_bindings_item_keys_item import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemKeysItem,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_bindings_item_property import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemProperty,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_bindings_item_property_one import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemPropertyOne,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_bindings_item_property_zero import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemPropertyZero,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_multi_bindings_item import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItem,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_multi_bindings_item_curve import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemCurve,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_multi_bindings_item_curve_control_points_item import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemCurveControlPointsItem,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_multi_bindings_item_interpolation import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolation,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_multi_bindings_item_interpolation_four import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolationFour,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_multi_bindings_item_interpolation_one import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolationOne,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_multi_bindings_item_interpolation_three import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolationThree,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_multi_bindings_item_interpolation_two import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolationTwo,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_multi_bindings_item_interpolation_zero import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolationZero,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_multi_bindings_item_keyforms_item import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemKeyformsItem,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_multi_bindings_item_property import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemProperty,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_multi_bindings_item_property_one import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemPropertyOne,
    )
    from .transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_multi_bindings_item_property_zero import (
        TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemPropertyZero,
    )
    from .transaction_request_operations_operations_item_action_deformer_origin import (
        TransactionRequestOperationsOperationsItemActionDeformerOrigin,
    )
    from .transaction_request_operations_operations_item_action_deformer_parent_set import (
        TransactionRequestOperationsOperationsItemActionDeformerParentSet,
    )
    from .transaction_request_operations_operations_item_action_deformer_rotation_metadata import (
        TransactionRequestOperationsOperationsItemActionDeformerRotationMetadata,
    )
    from .transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata import (
        TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadata,
    )
    from .transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata_angle_range import (
        TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataAngleRange,
    )
    from .transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata_angle_unit import (
        TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataAngleUnit,
    )
    from .transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata_parent_composition import (
        TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataParentComposition,
    )
    from .transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata_parent_composition_one import (
        TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataParentCompositionOne,
    )
    from .transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata_parent_composition_zero import (
        TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataParentCompositionZero,
    )
    from .transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata_pivot import (
        TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataPivot,
    )
    from .transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata_pivot_space import (
        TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataPivotSpace,
    )
    from .transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata_pivot_space_one import (
        TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataPivotSpaceOne,
    )
    from .transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata_pivot_space_zero import (
        TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataPivotSpaceZero,
    )
    from .transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata_shape_preservation import (
        TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataShapePreservation,
    )
    from .transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata_shape_preservation_one import (
        TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataShapePreservationOne,
    )
    from .transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata_shape_preservation_two import (
        TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataShapePreservationTwo,
    )
    from .transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata_shape_preservation_zero import (
        TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataShapePreservationZero,
    )
    from .transaction_request_operations_operations_item_action_deformer_split import (
        TransactionRequestOperationsOperationsItemActionDeformerSplit,
    )
    from .transaction_request_operations_operations_item_action_deformer_targets_set import (
        TransactionRequestOperationsOperationsItemActionDeformerTargetsSet,
    )
    from .transaction_request_operations_operations_item_action_deformer_targets_set_mode import (
        TransactionRequestOperationsOperationsItemActionDeformerTargetsSetMode,
    )
    from .transaction_request_operations_operations_item_action_deformer_targets_set_mode_one import (
        TransactionRequestOperationsOperationsItemActionDeformerTargetsSetModeOne,
    )
    from .transaction_request_operations_operations_item_action_deformer_targets_set_mode_zero import (
        TransactionRequestOperationsOperationsItemActionDeformerTargetsSetModeZero,
    )
    from .transaction_request_operations_operations_item_action_deformer_transform import (
        TransactionRequestOperationsOperationsItemActionDeformerTransform,
    )
    from .transaction_request_operations_operations_item_action_deformer_transform_operator import (
        TransactionRequestOperationsOperationsItemActionDeformerTransformOperator,
    )
    from .transaction_request_operations_operations_item_action_deformer_transform_operator_one import (
        TransactionRequestOperationsOperationsItemActionDeformerTransformOperatorOne,
    )
    from .transaction_request_operations_operations_item_action_deformer_transform_operator_two import (
        TransactionRequestOperationsOperationsItemActionDeformerTransformOperatorTwo,
    )
    from .transaction_request_operations_operations_item_action_deformer_transform_operator_zero import (
        TransactionRequestOperationsOperationsItemActionDeformerTransformOperatorZero,
    )
    from .transaction_request_operations_operations_item_action_deformer_transform_property import (
        TransactionRequestOperationsOperationsItemActionDeformerTransformProperty,
    )
    from .transaction_request_operations_operations_item_action_deformer_transform_property_five import (
        TransactionRequestOperationsOperationsItemActionDeformerTransformPropertyFive,
    )
    from .transaction_request_operations_operations_item_action_deformer_transform_property_four import (
        TransactionRequestOperationsOperationsItemActionDeformerTransformPropertyFour,
    )
    from .transaction_request_operations_operations_item_action_deformer_transform_property_one import (
        TransactionRequestOperationsOperationsItemActionDeformerTransformPropertyOne,
    )
    from .transaction_request_operations_operations_item_action_deformer_transform_property_three import (
        TransactionRequestOperationsOperationsItemActionDeformerTransformPropertyThree,
    )
    from .transaction_request_operations_operations_item_action_deformer_transform_property_two import (
        TransactionRequestOperationsOperationsItemActionDeformerTransformPropertyTwo,
    )
    from .transaction_request_operations_operations_item_action_deformer_transform_property_zero import (
        TransactionRequestOperationsOperationsItemActionDeformerTransformPropertyZero,
    )
    from .transaction_request_operations_operations_item_action_parameter_add import (
        TransactionRequestOperationsOperationsItemActionParameterAdd,
    )
    from .transaction_request_operations_operations_item_action_parameter_add_parameter import (
        TransactionRequestOperationsOperationsItemActionParameterAddParameter,
    )
    from .transaction_request_operations_operations_item_action_part_alpha_reveal import (
        TransactionRequestOperationsOperationsItemActionPartAlphaReveal,
    )
    from .transaction_request_operations_operations_item_action_part_alpha_reveal_reveal import (
        TransactionRequestOperationsOperationsItemActionPartAlphaRevealReveal,
    )
    from .transaction_request_operations_operations_item_action_part_blend_mode import (
        TransactionRequestOperationsOperationsItemActionPartBlendMode,
    )
    from .transaction_request_operations_operations_item_action_part_blend_mode_mode import (
        TransactionRequestOperationsOperationsItemActionPartBlendModeMode,
    )
    from .transaction_request_operations_operations_item_action_part_blend_mode_mode_one import (
        TransactionRequestOperationsOperationsItemActionPartBlendModeModeOne,
    )
    from .transaction_request_operations_operations_item_action_part_blend_mode_mode_three import (
        TransactionRequestOperationsOperationsItemActionPartBlendModeModeThree,
    )
    from .transaction_request_operations_operations_item_action_part_blend_mode_mode_two import (
        TransactionRequestOperationsOperationsItemActionPartBlendModeModeTwo,
    )
    from .transaction_request_operations_operations_item_action_part_blend_mode_mode_zero import (
        TransactionRequestOperationsOperationsItemActionPartBlendModeModeZero,
    )
    from .transaction_request_operations_operations_item_action_part_clip import (
        TransactionRequestOperationsOperationsItemActionPartClip,
    )
    from .transaction_request_operations_operations_item_action_part_clip_clip import (
        TransactionRequestOperationsOperationsItemActionPartClipClip,
    )
    from .transaction_request_operations_operations_item_action_part_clip_clip_mask_opacity import (
        TransactionRequestOperationsOperationsItemActionPartClipClipMaskOpacity,
    )
    from .transaction_request_operations_operations_item_action_part_clip_clip_mask_opacity_one import (
        TransactionRequestOperationsOperationsItemActionPartClipClipMaskOpacityOne,
    )
    from .transaction_request_operations_operations_item_action_part_clip_clip_mask_opacity_zero import (
        TransactionRequestOperationsOperationsItemActionPartClipClipMaskOpacityZero,
    )
    from .transaction_request_operations_operations_item_action_part_clip_clip_mode import (
        TransactionRequestOperationsOperationsItemActionPartClipClipMode,
    )
    from .transaction_request_operations_operations_item_action_part_contour_shade import (
        TransactionRequestOperationsOperationsItemActionPartContourShade,
    )
    from .transaction_request_operations_operations_item_action_part_contour_shade_shade import (
        TransactionRequestOperationsOperationsItemActionPartContourShadeShade,
    )
    from .transaction_request_operations_operations_item_action_part_contour_shade_shade_profile import (
        TransactionRequestOperationsOperationsItemActionPartContourShadeShadeProfile,
    )
    from .transaction_request_operations_operations_item_action_part_draw_order import (
        TransactionRequestOperationsOperationsItemActionPartDrawOrder,
    )
    from .transaction_request_operations_operations_item_action_part_tint import (
        TransactionRequestOperationsOperationsItemActionPartTint,
    )
    from .transaction_request_operations_operations_item_action_part_tint_tint import (
        TransactionRequestOperationsOperationsItemActionPartTintTint,
    )
    from .transaction_request_operations_operations_item_action_part_tint_tint_mode import (
        TransactionRequestOperationsOperationsItemActionPartTintTintMode,
    )
    from .transaction_request_operations_operations_item_action_part_tint_tint_mode_one import (
        TransactionRequestOperationsOperationsItemActionPartTintTintModeOne,
    )
    from .transaction_request_operations_operations_item_action_part_tint_tint_mode_zero import (
        TransactionRequestOperationsOperationsItemActionPartTintTintModeZero,
    )
    from .transaction_request_operations_operations_item_action_part_visibility import (
        TransactionRequestOperationsOperationsItemActionPartVisibility,
    )
    from .transaction_request_operations_operations_item_action_role_confirm import (
        TransactionRequestOperationsOperationsItemActionRoleConfirm,
    )
    from .transaction_request_operations_operations_item_action_role_confirm_role import (
        TransactionRequestOperationsOperationsItemActionRoleConfirmRole,
    )
    from .transaction_request_operations_operations_item_action_role_confirm_role_eight import (
        TransactionRequestOperationsOperationsItemActionRoleConfirmRoleEight,
    )
    from .transaction_request_operations_operations_item_action_role_confirm_role_eleven import (
        TransactionRequestOperationsOperationsItemActionRoleConfirmRoleEleven,
    )
    from .transaction_request_operations_operations_item_action_role_confirm_role_fifteen import (
        TransactionRequestOperationsOperationsItemActionRoleConfirmRoleFifteen,
    )
    from .transaction_request_operations_operations_item_action_role_confirm_role_five import (
        TransactionRequestOperationsOperationsItemActionRoleConfirmRoleFive,
    )
    from .transaction_request_operations_operations_item_action_role_confirm_role_four import (
        TransactionRequestOperationsOperationsItemActionRoleConfirmRoleFour,
    )
    from .transaction_request_operations_operations_item_action_role_confirm_role_fourteen import (
        TransactionRequestOperationsOperationsItemActionRoleConfirmRoleFourteen,
    )
    from .transaction_request_operations_operations_item_action_role_confirm_role_nine import (
        TransactionRequestOperationsOperationsItemActionRoleConfirmRoleNine,
    )
    from .transaction_request_operations_operations_item_action_role_confirm_role_one import (
        TransactionRequestOperationsOperationsItemActionRoleConfirmRoleOne,
    )
    from .transaction_request_operations_operations_item_action_role_confirm_role_seven import (
        TransactionRequestOperationsOperationsItemActionRoleConfirmRoleSeven,
    )
    from .transaction_request_operations_operations_item_action_role_confirm_role_seventeen import (
        TransactionRequestOperationsOperationsItemActionRoleConfirmRoleSeventeen,
    )
    from .transaction_request_operations_operations_item_action_role_confirm_role_six import (
        TransactionRequestOperationsOperationsItemActionRoleConfirmRoleSix,
    )
    from .transaction_request_operations_operations_item_action_role_confirm_role_sixteen import (
        TransactionRequestOperationsOperationsItemActionRoleConfirmRoleSixteen,
    )
    from .transaction_request_operations_operations_item_action_role_confirm_role_ten import (
        TransactionRequestOperationsOperationsItemActionRoleConfirmRoleTen,
    )
    from .transaction_request_operations_operations_item_action_role_confirm_role_thirteen import (
        TransactionRequestOperationsOperationsItemActionRoleConfirmRoleThirteen,
    )
    from .transaction_request_operations_operations_item_action_role_confirm_role_three import (
        TransactionRequestOperationsOperationsItemActionRoleConfirmRoleThree,
    )
    from .transaction_request_operations_operations_item_action_role_confirm_role_twelve import (
        TransactionRequestOperationsOperationsItemActionRoleConfirmRoleTwelve,
    )
    from .transaction_request_operations_operations_item_action_role_confirm_role_two import (
        TransactionRequestOperationsOperationsItemActionRoleConfirmRoleTwo,
    )
    from .transaction_request_operations_operations_item_action_role_confirm_role_zero import (
        TransactionRequestOperationsOperationsItemActionRoleConfirmRoleZero,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify import (
        TransactionRequestOperationsOperationsItemActionRoleReclassify,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_expected_role import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRole,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_expected_role_eight import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleEight,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_expected_role_eleven import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleEleven,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_expected_role_fifteen import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleFifteen,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_expected_role_five import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleFive,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_expected_role_four import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleFour,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_expected_role_fourteen import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleFourteen,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_expected_role_nine import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleNine,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_expected_role_one import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleOne,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_expected_role_seven import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleSeven,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_expected_role_seventeen import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleSeventeen,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_expected_role_six import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleSix,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_expected_role_sixteen import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleSixteen,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_expected_role_ten import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleTen,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_expected_role_thirteen import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleThirteen,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_expected_role_three import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleThree,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_expected_role_twelve import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleTwelve,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_expected_role_two import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleTwo,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_expected_role_zero import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleZero,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_role import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyRole,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_role_eight import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleEight,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_role_eleven import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleEleven,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_role_fifteen import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleFifteen,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_role_five import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleFive,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_role_four import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleFour,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_role_fourteen import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleFourteen,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_role_nine import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleNine,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_role_one import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleOne,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_role_seven import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleSeven,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_role_seventeen import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleSeventeen,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_role_six import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleSix,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_role_sixteen import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleSixteen,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_role_ten import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleTen,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_role_thirteen import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleThirteen,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_role_three import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleThree,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_role_twelve import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleTwelve,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_role_two import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleTwo,
    )
    from .transaction_request_operations_operations_item_action_role_reclassify_role_zero import (
        TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleZero,
    )
    from .transaction_request_operations_operations_item_action_symmetry_artmesh_bindings import (
        TransactionRequestOperationsOperationsItemActionSymmetryArtmeshBindings,
    )
    from .transaction_request_operations_operations_item_action_symmetry_artmesh_bindings_links_item import (
        TransactionRequestOperationsOperationsItemActionSymmetryArtmeshBindingsLinksItem,
    )
    from .transaction_request_operations_operations_item_action_symmetry_artmesh_bindings_links_item_axis import (
        TransactionRequestOperationsOperationsItemActionSymmetryArtmeshBindingsLinksItemAxis,
    )
    from .transaction_request_operations_operations_item_action_symmetry_artmesh_bindings_links_item_kind import (
        TransactionRequestOperationsOperationsItemActionSymmetryArtmeshBindingsLinksItemKind,
    )
    from .transaction_request_operations_operations_item_action_symmetry_artmesh_bindings_links_item_kind_one import (
        TransactionRequestOperationsOperationsItemActionSymmetryArtmeshBindingsLinksItemKindOne,
    )
    from .transaction_request_operations_operations_item_action_symmetry_artmesh_bindings_links_item_kind_three import (
        TransactionRequestOperationsOperationsItemActionSymmetryArtmeshBindingsLinksItemKindThree,
    )
    from .transaction_request_operations_operations_item_action_symmetry_artmesh_bindings_links_item_kind_two import (
        TransactionRequestOperationsOperationsItemActionSymmetryArtmeshBindingsLinksItemKindTwo,
    )
    from .transaction_request_operations_operations_item_action_symmetry_artmesh_bindings_links_item_kind_zero import (
        TransactionRequestOperationsOperationsItemActionSymmetryArtmeshBindingsLinksItemKindZero,
    )
    from .transaction_request_operations_operations_item_action_symmetry_contract import (
        TransactionRequestOperationsOperationsItemActionSymmetryContract,
    )
    from .transaction_request_operations_operations_item_action_symmetry_contract_contract import (
        TransactionRequestOperationsOperationsItemActionSymmetryContractContract,
    )
    from .transaction_request_operations_operations_item_action_symmetry_contract_contract_axis import (
        TransactionRequestOperationsOperationsItemActionSymmetryContractContractAxis,
    )
    from .transaction_request_operations_operations_item_action_symmetry_contract_contract_links_item import (
        TransactionRequestOperationsOperationsItemActionSymmetryContractContractLinksItem,
    )
    from .transaction_request_operations_operations_item_action_symmetry_contract_contract_links_item_axis import (
        TransactionRequestOperationsOperationsItemActionSymmetryContractContractLinksItemAxis,
    )
    from .transaction_request_operations_operations_item_action_symmetry_contract_contract_links_item_kind import (
        TransactionRequestOperationsOperationsItemActionSymmetryContractContractLinksItemKind,
    )
    from .transaction_request_operations_operations_item_action_symmetry_contract_contract_links_item_kind_one import (
        TransactionRequestOperationsOperationsItemActionSymmetryContractContractLinksItemKindOne,
    )
    from .transaction_request_operations_operations_item_action_symmetry_contract_contract_links_item_kind_three import (
        TransactionRequestOperationsOperationsItemActionSymmetryContractContractLinksItemKindThree,
    )
    from .transaction_request_operations_operations_item_action_symmetry_contract_contract_links_item_kind_two import (
        TransactionRequestOperationsOperationsItemActionSymmetryContractContractLinksItemKindTwo,
    )
    from .transaction_request_operations_operations_item_action_symmetry_contract_contract_links_item_kind_zero import (
        TransactionRequestOperationsOperationsItemActionSymmetryContractContractLinksItemKindZero,
    )
    from .transaction_request_operations_operations_item_action_transform import (
        TransactionRequestOperationsOperationsItemActionTransform,
    )
    from .transaction_request_operations_operations_item_action_transform_operator import (
        TransactionRequestOperationsOperationsItemActionTransformOperator,
    )
    from .transaction_request_operations_operations_item_action_transform_operator_one import (
        TransactionRequestOperationsOperationsItemActionTransformOperatorOne,
    )
    from .transaction_request_operations_operations_item_action_transform_operator_two import (
        TransactionRequestOperationsOperationsItemActionTransformOperatorTwo,
    )
    from .transaction_request_operations_operations_item_action_transform_operator_zero import (
        TransactionRequestOperationsOperationsItemActionTransformOperatorZero,
    )
    from .transaction_request_operations_operations_item_action_transform_property import (
        TransactionRequestOperationsOperationsItemActionTransformProperty,
    )
    from .transaction_request_operations_operations_item_action_transform_property_five import (
        TransactionRequestOperationsOperationsItemActionTransformPropertyFive,
    )
    from .transaction_request_operations_operations_item_action_transform_property_four import (
        TransactionRequestOperationsOperationsItemActionTransformPropertyFour,
    )
    from .transaction_request_operations_operations_item_action_transform_property_one import (
        TransactionRequestOperationsOperationsItemActionTransformPropertyOne,
    )
    from .transaction_request_operations_operations_item_action_transform_property_three import (
        TransactionRequestOperationsOperationsItemActionTransformPropertyThree,
    )
    from .transaction_request_operations_operations_item_action_transform_property_two import (
        TransactionRequestOperationsOperationsItemActionTransformPropertyTwo,
    )
    from .transaction_request_operations_operations_item_action_transform_property_zero import (
        TransactionRequestOperationsOperationsItemActionTransformPropertyZero,
    )
    from .transaction_request_operations_operations_item_action_warp_pin_binding_key import (
        TransactionRequestOperationsOperationsItemActionWarpPinBindingKey,
    )
    from .transaction_request_operations_operations_item_action_warp_pin_binding_key_curve import (
        TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyCurve,
    )
    from .transaction_request_operations_operations_item_action_warp_pin_binding_key_curve_control_points_item import (
        TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyCurveControlPointsItem,
    )
    from .transaction_request_operations_operations_item_action_warp_pin_binding_key_interpolation import (
        TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyInterpolation,
    )
    from .transaction_request_operations_operations_item_action_warp_pin_binding_key_interpolation_four import (
        TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyInterpolationFour,
    )
    from .transaction_request_operations_operations_item_action_warp_pin_binding_key_interpolation_one import (
        TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyInterpolationOne,
    )
    from .transaction_request_operations_operations_item_action_warp_pin_binding_key_interpolation_three import (
        TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyInterpolationThree,
    )
    from .transaction_request_operations_operations_item_action_warp_pin_binding_key_interpolation_two import (
        TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyInterpolationTwo,
    )
    from .transaction_request_operations_operations_item_action_warp_pin_binding_key_interpolation_zero import (
        TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyInterpolationZero,
    )
    from .transaction_request_operations_operations_item_action_warp_pin_binding_key_property import (
        TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyProperty,
    )
    from .transaction_request_operations_operations_item_action_warp_pin_binding_key_property_one import (
        TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyPropertyOne,
    )
    from .transaction_request_operations_operations_item_action_warp_pin_binding_key_property_zero import (
        TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyPropertyZero,
    )
    from .transaction_request_operations_operations_item_target import TransactionRequestOperationsOperationsItemTarget
    from .transaction_request_operations_operations_item_target_roles_item import (
        TransactionRequestOperationsOperationsItemTargetRolesItem,
    )
    from .transaction_request_operations_operations_item_target_roles_item_eight import (
        TransactionRequestOperationsOperationsItemTargetRolesItemEight,
    )
    from .transaction_request_operations_operations_item_target_roles_item_eleven import (
        TransactionRequestOperationsOperationsItemTargetRolesItemEleven,
    )
    from .transaction_request_operations_operations_item_target_roles_item_fifteen import (
        TransactionRequestOperationsOperationsItemTargetRolesItemFifteen,
    )
    from .transaction_request_operations_operations_item_target_roles_item_five import (
        TransactionRequestOperationsOperationsItemTargetRolesItemFive,
    )
    from .transaction_request_operations_operations_item_target_roles_item_four import (
        TransactionRequestOperationsOperationsItemTargetRolesItemFour,
    )
    from .transaction_request_operations_operations_item_target_roles_item_fourteen import (
        TransactionRequestOperationsOperationsItemTargetRolesItemFourteen,
    )
    from .transaction_request_operations_operations_item_target_roles_item_nine import (
        TransactionRequestOperationsOperationsItemTargetRolesItemNine,
    )
    from .transaction_request_operations_operations_item_target_roles_item_one import (
        TransactionRequestOperationsOperationsItemTargetRolesItemOne,
    )
    from .transaction_request_operations_operations_item_target_roles_item_seven import (
        TransactionRequestOperationsOperationsItemTargetRolesItemSeven,
    )
    from .transaction_request_operations_operations_item_target_roles_item_seventeen import (
        TransactionRequestOperationsOperationsItemTargetRolesItemSeventeen,
    )
    from .transaction_request_operations_operations_item_target_roles_item_six import (
        TransactionRequestOperationsOperationsItemTargetRolesItemSix,
    )
    from .transaction_request_operations_operations_item_target_roles_item_sixteen import (
        TransactionRequestOperationsOperationsItemTargetRolesItemSixteen,
    )
    from .transaction_request_operations_operations_item_target_roles_item_ten import (
        TransactionRequestOperationsOperationsItemTargetRolesItemTen,
    )
    from .transaction_request_operations_operations_item_target_roles_item_thirteen import (
        TransactionRequestOperationsOperationsItemTargetRolesItemThirteen,
    )
    from .transaction_request_operations_operations_item_target_roles_item_three import (
        TransactionRequestOperationsOperationsItemTargetRolesItemThree,
    )
    from .transaction_request_operations_operations_item_target_roles_item_twelve import (
        TransactionRequestOperationsOperationsItemTargetRolesItemTwelve,
    )
    from .transaction_request_operations_operations_item_target_roles_item_two import (
        TransactionRequestOperationsOperationsItemTargetRolesItemTwo,
    )
    from .transaction_request_operations_operations_item_target_roles_item_zero import (
        TransactionRequestOperationsOperationsItemTargetRolesItemZero,
    )
    from .transaction_request_operations_qa import TransactionRequestOperationsQa
    from .transaction_request_operations_qa_motion_sweep import TransactionRequestOperationsQaMotionSweep
    from .transaction_request_operations_qa_motion_sweep_check_monotonic import (
        TransactionRequestOperationsQaMotionSweepCheckMonotonic,
    )
    from .transaction_request_operations_qa_pose_samples_item import TransactionRequestOperationsQaPoseSamplesItem
    from .transaction_request_rig import TransactionRequestRig
    from .transaction_request_rig_kind import TransactionRequestRigKind
_dynamic_imports: typing.Dict[str, str] = {
    "GetApiPlaybackMotionResponse": ".get_api_playback_motion_response",
    "GetApiPlaybackMotionResponsePlayback": ".get_api_playback_motion_response_playback",
    "GetApiPlaybackMotionResponsePlaybackDemo": ".get_api_playback_motion_response_playback_demo",
    "GetApiPlaybackMotionResponsePlaybackDemoMode": ".get_api_playback_motion_response_playback_demo_mode",
    "GetApiPlaybackMotionResponsePlaybackMotion": ".get_api_playback_motion_response_playback_motion",
    "GetApiPlaybackResponse": ".get_api_playback_response",
    "GetApiPlaybackResponsePlayback": ".get_api_playback_response_playback",
    "GetApiPlaybackResponsePlaybackDemo": ".get_api_playback_response_playback_demo",
    "GetApiPlaybackResponsePlaybackDemoMode": ".get_api_playback_response_playback_demo_mode",
    "GetApiPlaybackResponsePlaybackMotion": ".get_api_playback_response_playback_motion",
    "ModelingOperation": ".modeling_operation",
    "ModelingOperationAction": ".modeling_operation_action",
    "ModelingOperationActionArtmeshBindingKey": ".modeling_operation_action_artmesh_binding_key",
    "ModelingOperationActionArtmeshBindingKeyCurve": ".modeling_operation_action_artmesh_binding_key_curve",
    "ModelingOperationActionArtmeshBindingKeyCurveControlPointsItem": ".modeling_operation_action_artmesh_binding_key_curve_control_points_item",
    "ModelingOperationActionArtmeshBindingKeyInterpolation": ".modeling_operation_action_artmesh_binding_key_interpolation",
    "ModelingOperationActionArtmeshBindingKeyInterpolationFour": ".modeling_operation_action_artmesh_binding_key_interpolation_four",
    "ModelingOperationActionArtmeshBindingKeyInterpolationOne": ".modeling_operation_action_artmesh_binding_key_interpolation_one",
    "ModelingOperationActionArtmeshBindingKeyInterpolationThree": ".modeling_operation_action_artmesh_binding_key_interpolation_three",
    "ModelingOperationActionArtmeshBindingKeyInterpolationTwo": ".modeling_operation_action_artmesh_binding_key_interpolation_two",
    "ModelingOperationActionArtmeshBindingKeyInterpolationZero": ".modeling_operation_action_artmesh_binding_key_interpolation_zero",
    "ModelingOperationActionArtmeshBindingKeyOffsetsItem": ".modeling_operation_action_artmesh_binding_key_offsets_item",
    "ModelingOperationActionArtmeshBlendShape": ".modeling_operation_action_artmesh_blend_shape",
    "ModelingOperationActionArtmeshBlendShapeCurve": ".modeling_operation_action_artmesh_blend_shape_curve",
    "ModelingOperationActionArtmeshBlendShapeCurveControlPointsItem": ".modeling_operation_action_artmesh_blend_shape_curve_control_points_item",
    "ModelingOperationActionArtmeshBlendShapeInterpolation": ".modeling_operation_action_artmesh_blend_shape_interpolation",
    "ModelingOperationActionArtmeshBlendShapeInterpolationFour": ".modeling_operation_action_artmesh_blend_shape_interpolation_four",
    "ModelingOperationActionArtmeshBlendShapeInterpolationOne": ".modeling_operation_action_artmesh_blend_shape_interpolation_one",
    "ModelingOperationActionArtmeshBlendShapeInterpolationThree": ".modeling_operation_action_artmesh_blend_shape_interpolation_three",
    "ModelingOperationActionArtmeshBlendShapeInterpolationTwo": ".modeling_operation_action_artmesh_blend_shape_interpolation_two",
    "ModelingOperationActionArtmeshBlendShapeInterpolationZero": ".modeling_operation_action_artmesh_blend_shape_interpolation_zero",
    "ModelingOperationActionArtmeshBlendShapeOffsetsItem": ".modeling_operation_action_artmesh_blend_shape_offsets_item",
    "ModelingOperationActionArtmeshGenerate": ".modeling_operation_action_artmesh_generate",
    "ModelingOperationActionArtmeshGeneratePreset": ".modeling_operation_action_artmesh_generate_preset",
    "ModelingOperationActionArtmeshGeneratePresetFive": ".modeling_operation_action_artmesh_generate_preset_five",
    "ModelingOperationActionArtmeshGeneratePresetFour": ".modeling_operation_action_artmesh_generate_preset_four",
    "ModelingOperationActionArtmeshGeneratePresetOne": ".modeling_operation_action_artmesh_generate_preset_one",
    "ModelingOperationActionArtmeshGeneratePresetThree": ".modeling_operation_action_artmesh_generate_preset_three",
    "ModelingOperationActionArtmeshGeneratePresetTwo": ".modeling_operation_action_artmesh_generate_preset_two",
    "ModelingOperationActionArtmeshGeneratePresetZero": ".modeling_operation_action_artmesh_generate_preset_zero",
    "ModelingOperationActionArtmeshGenerateQuality": ".modeling_operation_action_artmesh_generate_quality",
    "ModelingOperationActionArtmeshGenerateTopology": ".modeling_operation_action_artmesh_generate_topology",
    "ModelingOperationActionArtmeshGenerateTopologyOne": ".modeling_operation_action_artmesh_generate_topology_one",
    "ModelingOperationActionArtmeshGenerateTopologyZero": ".modeling_operation_action_artmesh_generate_topology_zero",
    "ModelingOperationActionArtmeshMirrorKey": ".modeling_operation_action_artmesh_mirror_key",
    "ModelingOperationActionArtmeshMirrorKeyCurve": ".modeling_operation_action_artmesh_mirror_key_curve",
    "ModelingOperationActionArtmeshMirrorKeyCurveControlPointsItem": ".modeling_operation_action_artmesh_mirror_key_curve_control_points_item",
    "ModelingOperationActionArtmeshMirrorKeyInterpolation": ".modeling_operation_action_artmesh_mirror_key_interpolation",
    "ModelingOperationActionArtmeshMirrorKeyInterpolationFour": ".modeling_operation_action_artmesh_mirror_key_interpolation_four",
    "ModelingOperationActionArtmeshMirrorKeyInterpolationOne": ".modeling_operation_action_artmesh_mirror_key_interpolation_one",
    "ModelingOperationActionArtmeshMirrorKeyInterpolationThree": ".modeling_operation_action_artmesh_mirror_key_interpolation_three",
    "ModelingOperationActionArtmeshMirrorKeyInterpolationTwo": ".modeling_operation_action_artmesh_mirror_key_interpolation_two",
    "ModelingOperationActionArtmeshMirrorKeyInterpolationZero": ".modeling_operation_action_artmesh_mirror_key_interpolation_zero",
    "ModelingOperationActionArtmeshMultiKey": ".modeling_operation_action_artmesh_multi_key",
    "ModelingOperationActionArtmeshMultiKeyCurve": ".modeling_operation_action_artmesh_multi_key_curve",
    "ModelingOperationActionArtmeshMultiKeyCurveControlPointsItem": ".modeling_operation_action_artmesh_multi_key_curve_control_points_item",
    "ModelingOperationActionArtmeshMultiKeyInterpolation": ".modeling_operation_action_artmesh_multi_key_interpolation",
    "ModelingOperationActionArtmeshMultiKeyInterpolationFour": ".modeling_operation_action_artmesh_multi_key_interpolation_four",
    "ModelingOperationActionArtmeshMultiKeyInterpolationOne": ".modeling_operation_action_artmesh_multi_key_interpolation_one",
    "ModelingOperationActionArtmeshMultiKeyInterpolationThree": ".modeling_operation_action_artmesh_multi_key_interpolation_three",
    "ModelingOperationActionArtmeshMultiKeyInterpolationTwo": ".modeling_operation_action_artmesh_multi_key_interpolation_two",
    "ModelingOperationActionArtmeshMultiKeyInterpolationZero": ".modeling_operation_action_artmesh_multi_key_interpolation_zero",
    "ModelingOperationActionArtmeshMultiKeyOffsetsItem": ".modeling_operation_action_artmesh_multi_key_offsets_item",
    "ModelingOperationActionArtmeshOffset": ".modeling_operation_action_artmesh_offset",
    "ModelingOperationActionArtmeshOffsetUv": ".modeling_operation_action_artmesh_offset_uv",
    "ModelingOperationActionArtmeshQuality": ".modeling_operation_action_artmesh_quality",
    "ModelingOperationActionArtmeshQualityQuality": ".modeling_operation_action_artmesh_quality_quality",
    "ModelingOperationActionArtmeshRebuild": ".modeling_operation_action_artmesh_rebuild",
    "ModelingOperationActionArtmeshRebuildPreset": ".modeling_operation_action_artmesh_rebuild_preset",
    "ModelingOperationActionArtmeshRebuildPresetFive": ".modeling_operation_action_artmesh_rebuild_preset_five",
    "ModelingOperationActionArtmeshRebuildPresetFour": ".modeling_operation_action_artmesh_rebuild_preset_four",
    "ModelingOperationActionArtmeshRebuildPresetOne": ".modeling_operation_action_artmesh_rebuild_preset_one",
    "ModelingOperationActionArtmeshRebuildPresetThree": ".modeling_operation_action_artmesh_rebuild_preset_three",
    "ModelingOperationActionArtmeshRebuildPresetTwo": ".modeling_operation_action_artmesh_rebuild_preset_two",
    "ModelingOperationActionArtmeshRebuildPresetZero": ".modeling_operation_action_artmesh_rebuild_preset_zero",
    "ModelingOperationActionArtmeshRebuildQuality": ".modeling_operation_action_artmesh_rebuild_quality",
    "ModelingOperationActionArtmeshRebuildTopology": ".modeling_operation_action_artmesh_rebuild_topology",
    "ModelingOperationActionArtmeshRebuildTopologyOne": ".modeling_operation_action_artmesh_rebuild_topology_one",
    "ModelingOperationActionArtmeshRebuildTopologyZero": ".modeling_operation_action_artmesh_rebuild_topology_zero",
    "ModelingOperationActionBindingKey": ".modeling_operation_action_binding_key",
    "ModelingOperationActionBindingKeyCurve": ".modeling_operation_action_binding_key_curve",
    "ModelingOperationActionBindingKeyCurveControlPointsItem": ".modeling_operation_action_binding_key_curve_control_points_item",
    "ModelingOperationActionBindingKeyInterpolation": ".modeling_operation_action_binding_key_interpolation",
    "ModelingOperationActionBindingKeyInterpolationFour": ".modeling_operation_action_binding_key_interpolation_four",
    "ModelingOperationActionBindingKeyInterpolationOne": ".modeling_operation_action_binding_key_interpolation_one",
    "ModelingOperationActionBindingKeyInterpolationThree": ".modeling_operation_action_binding_key_interpolation_three",
    "ModelingOperationActionBindingKeyInterpolationTwo": ".modeling_operation_action_binding_key_interpolation_two",
    "ModelingOperationActionBindingKeyInterpolationZero": ".modeling_operation_action_binding_key_interpolation_zero",
    "ModelingOperationActionBindingKeyProperty": ".modeling_operation_action_binding_key_property",
    "ModelingOperationActionBindingKeyPropertyFive": ".modeling_operation_action_binding_key_property_five",
    "ModelingOperationActionBindingKeyPropertyFour": ".modeling_operation_action_binding_key_property_four",
    "ModelingOperationActionBindingKeyPropertyOne": ".modeling_operation_action_binding_key_property_one",
    "ModelingOperationActionBindingKeyPropertyThree": ".modeling_operation_action_binding_key_property_three",
    "ModelingOperationActionBindingKeyPropertyTwo": ".modeling_operation_action_binding_key_property_two",
    "ModelingOperationActionBindingKeyPropertyZero": ".modeling_operation_action_binding_key_property_zero",
    "ModelingOperationActionBlendShapeSet": ".modeling_operation_action_blend_shape_set",
    "ModelingOperationActionBlendShapeSetShape": ".modeling_operation_action_blend_shape_set_shape",
    "ModelingOperationActionBlendShapeSetShapeArtPath": ".modeling_operation_action_blend_shape_set_shape_art_path",
    "ModelingOperationActionBlendShapeSetShapeArtPathCurve": ".modeling_operation_action_blend_shape_set_shape_art_path_curve",
    "ModelingOperationActionBlendShapeSetShapeArtPathCurveControlPointsItem": ".modeling_operation_action_blend_shape_set_shape_art_path_curve_control_points_item",
    "ModelingOperationActionBlendShapeSetShapeArtPathInterpolation": ".modeling_operation_action_blend_shape_set_shape_art_path_interpolation",
    "ModelingOperationActionBlendShapeSetShapeArtPathInterpolationFour": ".modeling_operation_action_blend_shape_set_shape_art_path_interpolation_four",
    "ModelingOperationActionBlendShapeSetShapeArtPathInterpolationOne": ".modeling_operation_action_blend_shape_set_shape_art_path_interpolation_one",
    "ModelingOperationActionBlendShapeSetShapeArtPathInterpolationThree": ".modeling_operation_action_blend_shape_set_shape_art_path_interpolation_three",
    "ModelingOperationActionBlendShapeSetShapeArtPathInterpolationTwo": ".modeling_operation_action_blend_shape_set_shape_art_path_interpolation_two",
    "ModelingOperationActionBlendShapeSetShapeArtPathInterpolationZero": ".modeling_operation_action_blend_shape_set_shape_art_path_interpolation_zero",
    "ModelingOperationActionBlendShapeSetShapeArtPathPointsItem": ".modeling_operation_action_blend_shape_set_shape_art_path_points_item",
    "ModelingOperationActionBlendShapeSetShapeDeformer": ".modeling_operation_action_blend_shape_set_shape_deformer",
    "ModelingOperationActionBlendShapeSetShapeDeformerCurve": ".modeling_operation_action_blend_shape_set_shape_deformer_curve",
    "ModelingOperationActionBlendShapeSetShapeDeformerCurveControlPointsItem": ".modeling_operation_action_blend_shape_set_shape_deformer_curve_control_points_item",
    "ModelingOperationActionBlendShapeSetShapeDeformerInterpolation": ".modeling_operation_action_blend_shape_set_shape_deformer_interpolation",
    "ModelingOperationActionBlendShapeSetShapeDeformerInterpolationFour": ".modeling_operation_action_blend_shape_set_shape_deformer_interpolation_four",
    "ModelingOperationActionBlendShapeSetShapeDeformerInterpolationOne": ".modeling_operation_action_blend_shape_set_shape_deformer_interpolation_one",
    "ModelingOperationActionBlendShapeSetShapeDeformerInterpolationThree": ".modeling_operation_action_blend_shape_set_shape_deformer_interpolation_three",
    "ModelingOperationActionBlendShapeSetShapeDeformerInterpolationTwo": ".modeling_operation_action_blend_shape_set_shape_deformer_interpolation_two",
    "ModelingOperationActionBlendShapeSetShapeDeformerInterpolationZero": ".modeling_operation_action_blend_shape_set_shape_deformer_interpolation_zero",
    "ModelingOperationActionBlendShapeSetShapeDeformerPinsItem": ".modeling_operation_action_blend_shape_set_shape_deformer_pins_item",
    "ModelingOperationActionBlendShapeSetShapeDeformerSharedPointsItem": ".modeling_operation_action_blend_shape_set_shape_deformer_shared_points_item",
    "ModelingOperationActionBlendShapeSetShapeDeformerTransform": ".modeling_operation_action_blend_shape_set_shape_deformer_transform",
    "ModelingOperationActionBlendShapeSetShapeDeformerWarp": ".modeling_operation_action_blend_shape_set_shape_deformer_warp",
    "ModelingOperationActionBlendShapeSetShapeGlue": ".modeling_operation_action_blend_shape_set_shape_glue",
    "ModelingOperationActionBlendShapeSetShapeGlueCurve": ".modeling_operation_action_blend_shape_set_shape_glue_curve",
    "ModelingOperationActionBlendShapeSetShapeGlueCurveControlPointsItem": ".modeling_operation_action_blend_shape_set_shape_glue_curve_control_points_item",
    "ModelingOperationActionBlendShapeSetShapeGlueInterpolation": ".modeling_operation_action_blend_shape_set_shape_glue_interpolation",
    "ModelingOperationActionBlendShapeSetShapeGlueInterpolationFour": ".modeling_operation_action_blend_shape_set_shape_glue_interpolation_four",
    "ModelingOperationActionBlendShapeSetShapeGlueInterpolationOne": ".modeling_operation_action_blend_shape_set_shape_glue_interpolation_one",
    "ModelingOperationActionBlendShapeSetShapeGlueInterpolationThree": ".modeling_operation_action_blend_shape_set_shape_glue_interpolation_three",
    "ModelingOperationActionBlendShapeSetShapeGlueInterpolationTwo": ".modeling_operation_action_blend_shape_set_shape_glue_interpolation_two",
    "ModelingOperationActionBlendShapeSetShapeGlueInterpolationZero": ".modeling_operation_action_blend_shape_set_shape_glue_interpolation_zero",
    "ModelingOperationActionBlendShapeSetShapePart": ".modeling_operation_action_blend_shape_set_shape_part",
    "ModelingOperationActionBlendShapeSetShapePartCurve": ".modeling_operation_action_blend_shape_set_shape_part_curve",
    "ModelingOperationActionBlendShapeSetShapePartCurveControlPointsItem": ".modeling_operation_action_blend_shape_set_shape_part_curve_control_points_item",
    "ModelingOperationActionBlendShapeSetShapePartInterpolation": ".modeling_operation_action_blend_shape_set_shape_part_interpolation",
    "ModelingOperationActionBlendShapeSetShapePartInterpolationFour": ".modeling_operation_action_blend_shape_set_shape_part_interpolation_four",
    "ModelingOperationActionBlendShapeSetShapePartInterpolationOne": ".modeling_operation_action_blend_shape_set_shape_part_interpolation_one",
    "ModelingOperationActionBlendShapeSetShapePartInterpolationThree": ".modeling_operation_action_blend_shape_set_shape_part_interpolation_three",
    "ModelingOperationActionBlendShapeSetShapePartInterpolationTwo": ".modeling_operation_action_blend_shape_set_shape_part_interpolation_two",
    "ModelingOperationActionBlendShapeSetShapePartInterpolationZero": ".modeling_operation_action_blend_shape_set_shape_part_interpolation_zero",
    "ModelingOperationActionBlendShapeSetShapePartTransform": ".modeling_operation_action_blend_shape_set_shape_part_transform",
    "ModelingOperationActionBlendShapeSetShape_ArtPath": ".modeling_operation_action_blend_shape_set_shape",
    "ModelingOperationActionBlendShapeSetShape_Deformer": ".modeling_operation_action_blend_shape_set_shape",
    "ModelingOperationActionBlendShapeSetShape_Glue": ".modeling_operation_action_blend_shape_set_shape",
    "ModelingOperationActionBlendShapeSetShape_Part": ".modeling_operation_action_blend_shape_set_shape",
    "ModelingOperationActionDeformBrush": ".modeling_operation_action_deform_brush",
    "ModelingOperationActionDeformBrushBrush": ".modeling_operation_action_deform_brush_brush",
    "ModelingOperationActionDeformBrushBrushDestination": ".modeling_operation_action_deform_brush_brush_destination",
    "ModelingOperationActionDeformBrushBrushDestinationBase": ".modeling_operation_action_deform_brush_brush_destination_base",
    "ModelingOperationActionDeformBrushBrushDestinationBlendShape": ".modeling_operation_action_deform_brush_brush_destination_blend_shape",
    "ModelingOperationActionDeformBrushBrushDestinationBlendShapeShape": ".modeling_operation_action_deform_brush_brush_destination_blend_shape_shape",
    "ModelingOperationActionDeformBrushBrushDestinationBlendShapeShapeCurve": ".modeling_operation_action_deform_brush_brush_destination_blend_shape_shape_curve",
    "ModelingOperationActionDeformBrushBrushDestinationBlendShapeShapeCurveControlPointsItem": ".modeling_operation_action_deform_brush_brush_destination_blend_shape_shape_curve_control_points_item",
    "ModelingOperationActionDeformBrushBrushDestinationBlendShapeShapeInterpolation": ".modeling_operation_action_deform_brush_brush_destination_blend_shape_shape_interpolation",
    "ModelingOperationActionDeformBrushBrushDestinationBlendShapeShapeInterpolationFour": ".modeling_operation_action_deform_brush_brush_destination_blend_shape_shape_interpolation_four",
    "ModelingOperationActionDeformBrushBrushDestinationBlendShapeShapeInterpolationOne": ".modeling_operation_action_deform_brush_brush_destination_blend_shape_shape_interpolation_one",
    "ModelingOperationActionDeformBrushBrushDestinationBlendShapeShapeInterpolationThree": ".modeling_operation_action_deform_brush_brush_destination_blend_shape_shape_interpolation_three",
    "ModelingOperationActionDeformBrushBrushDestinationBlendShapeShapeInterpolationTwo": ".modeling_operation_action_deform_brush_brush_destination_blend_shape_shape_interpolation_two",
    "ModelingOperationActionDeformBrushBrushDestinationBlendShapeShapeInterpolationZero": ".modeling_operation_action_deform_brush_brush_destination_blend_shape_shape_interpolation_zero",
    "ModelingOperationActionDeformBrushBrushDestinationKeyform": ".modeling_operation_action_deform_brush_brush_destination_keyform",
    "ModelingOperationActionDeformBrushBrushDestination_Base": ".modeling_operation_action_deform_brush_brush_destination",
    "ModelingOperationActionDeformBrushBrushDestination_BlendShape": ".modeling_operation_action_deform_brush_brush_destination",
    "ModelingOperationActionDeformBrushBrushDestination_Keyform": ".modeling_operation_action_deform_brush_brush_destination",
    "ModelingOperationActionDeformBrushBrushEffect": ".modeling_operation_action_deform_brush_brush_effect",
    "ModelingOperationActionDeformBrushBrushEffectBend": ".modeling_operation_action_deform_brush_brush_effect_bend",
    "ModelingOperationActionDeformBrushBrushEffectContourFollow": ".modeling_operation_action_deform_brush_brush_effect_contour_follow",
    "ModelingOperationActionDeformBrushBrushEffectInflate": ".modeling_operation_action_deform_brush_brush_effect_inflate",
    "ModelingOperationActionDeformBrushBrushEffectPinch": ".modeling_operation_action_deform_brush_brush_effect_pinch",
    "ModelingOperationActionDeformBrushBrushEffectRelax": ".modeling_operation_action_deform_brush_brush_effect_relax",
    "ModelingOperationActionDeformBrushBrushEffectSmooth": ".modeling_operation_action_deform_brush_brush_effect_smooth",
    "ModelingOperationActionDeformBrushBrushEffect_Bend": ".modeling_operation_action_deform_brush_brush_effect",
    "ModelingOperationActionDeformBrushBrushEffect_ContourFollow": ".modeling_operation_action_deform_brush_brush_effect",
    "ModelingOperationActionDeformBrushBrushEffect_Inflate": ".modeling_operation_action_deform_brush_brush_effect",
    "ModelingOperationActionDeformBrushBrushEffect_Pinch": ".modeling_operation_action_deform_brush_brush_effect",
    "ModelingOperationActionDeformBrushBrushEffect_Relax": ".modeling_operation_action_deform_brush_brush_effect",
    "ModelingOperationActionDeformBrushBrushEffect_Smooth": ".modeling_operation_action_deform_brush_brush_effect",
    "ModelingOperationActionDeformBrushBrushFalloff": ".modeling_operation_action_deform_brush_brush_falloff",
    "ModelingOperationActionDeformBrushBrushFalloffOne": ".modeling_operation_action_deform_brush_brush_falloff_one",
    "ModelingOperationActionDeformBrushBrushFalloffZero": ".modeling_operation_action_deform_brush_brush_falloff_zero",
    "ModelingOperationActionDeformBrushBrushSurface": ".modeling_operation_action_deform_brush_brush_surface",
    "ModelingOperationActionDeformBrushBrushSurfaceArtmesh": ".modeling_operation_action_deform_brush_brush_surface_artmesh",
    "ModelingOperationActionDeformBrushBrushSurfaceArtmeshSpace": ".modeling_operation_action_deform_brush_brush_surface_artmesh_space",
    "ModelingOperationActionDeformBrushBrushSurfaceSharedWarp": ".modeling_operation_action_deform_brush_brush_surface_shared_warp",
    "ModelingOperationActionDeformBrushBrushSurfaceSharedWarpSpace": ".modeling_operation_action_deform_brush_brush_surface_shared_warp_space",
    "ModelingOperationActionDeformBrushBrushSurfaceWarpPins": ".modeling_operation_action_deform_brush_brush_surface_warp_pins",
    "ModelingOperationActionDeformBrushBrushSurfaceWarpPinsSpace": ".modeling_operation_action_deform_brush_brush_surface_warp_pins_space",
    "ModelingOperationActionDeformBrushBrushSurface_Artmesh": ".modeling_operation_action_deform_brush_brush_surface",
    "ModelingOperationActionDeformBrushBrushSurface_SharedWarp": ".modeling_operation_action_deform_brush_brush_surface",
    "ModelingOperationActionDeformBrushBrushSurface_WarpPins": ".modeling_operation_action_deform_brush_brush_surface",
    "ModelingOperationActionDeformerBindingKey": ".modeling_operation_action_deformer_binding_key",
    "ModelingOperationActionDeformerBindingKeyCurve": ".modeling_operation_action_deformer_binding_key_curve",
    "ModelingOperationActionDeformerBindingKeyCurveControlPointsItem": ".modeling_operation_action_deformer_binding_key_curve_control_points_item",
    "ModelingOperationActionDeformerBindingKeyInterpolation": ".modeling_operation_action_deformer_binding_key_interpolation",
    "ModelingOperationActionDeformerBindingKeyInterpolationFour": ".modeling_operation_action_deformer_binding_key_interpolation_four",
    "ModelingOperationActionDeformerBindingKeyInterpolationOne": ".modeling_operation_action_deformer_binding_key_interpolation_one",
    "ModelingOperationActionDeformerBindingKeyInterpolationThree": ".modeling_operation_action_deformer_binding_key_interpolation_three",
    "ModelingOperationActionDeformerBindingKeyInterpolationTwo": ".modeling_operation_action_deformer_binding_key_interpolation_two",
    "ModelingOperationActionDeformerBindingKeyInterpolationZero": ".modeling_operation_action_deformer_binding_key_interpolation_zero",
    "ModelingOperationActionDeformerBindingKeyProperty": ".modeling_operation_action_deformer_binding_key_property",
    "ModelingOperationActionDeformerBindingKeyPropertyEight": ".modeling_operation_action_deformer_binding_key_property_eight",
    "ModelingOperationActionDeformerBindingKeyPropertyFive": ".modeling_operation_action_deformer_binding_key_property_five",
    "ModelingOperationActionDeformerBindingKeyPropertyFour": ".modeling_operation_action_deformer_binding_key_property_four",
    "ModelingOperationActionDeformerBindingKeyPropertyNine": ".modeling_operation_action_deformer_binding_key_property_nine",
    "ModelingOperationActionDeformerBindingKeyPropertyOne": ".modeling_operation_action_deformer_binding_key_property_one",
    "ModelingOperationActionDeformerBindingKeyPropertySeven": ".modeling_operation_action_deformer_binding_key_property_seven",
    "ModelingOperationActionDeformerBindingKeyPropertySix": ".modeling_operation_action_deformer_binding_key_property_six",
    "ModelingOperationActionDeformerBindingKeyPropertyThree": ".modeling_operation_action_deformer_binding_key_property_three",
    "ModelingOperationActionDeformerBindingKeyPropertyTwo": ".modeling_operation_action_deformer_binding_key_property_two",
    "ModelingOperationActionDeformerBindingKeyPropertyZero": ".modeling_operation_action_deformer_binding_key_property_zero",
    "ModelingOperationActionDeformerBindingRemove": ".modeling_operation_action_deformer_binding_remove",
    "ModelingOperationActionDeformerBindingRemoveProperty": ".modeling_operation_action_deformer_binding_remove_property",
    "ModelingOperationActionDeformerBindingRemovePropertyEight": ".modeling_operation_action_deformer_binding_remove_property_eight",
    "ModelingOperationActionDeformerBindingRemovePropertyFive": ".modeling_operation_action_deformer_binding_remove_property_five",
    "ModelingOperationActionDeformerBindingRemovePropertyFour": ".modeling_operation_action_deformer_binding_remove_property_four",
    "ModelingOperationActionDeformerBindingRemovePropertyNine": ".modeling_operation_action_deformer_binding_remove_property_nine",
    "ModelingOperationActionDeformerBindingRemovePropertyOne": ".modeling_operation_action_deformer_binding_remove_property_one",
    "ModelingOperationActionDeformerBindingRemovePropertySeven": ".modeling_operation_action_deformer_binding_remove_property_seven",
    "ModelingOperationActionDeformerBindingRemovePropertySix": ".modeling_operation_action_deformer_binding_remove_property_six",
    "ModelingOperationActionDeformerBindingRemovePropertyThree": ".modeling_operation_action_deformer_binding_remove_property_three",
    "ModelingOperationActionDeformerBindingRemovePropertyTwo": ".modeling_operation_action_deformer_binding_remove_property_two",
    "ModelingOperationActionDeformerBindingRemovePropertyZero": ".modeling_operation_action_deformer_binding_remove_property_zero",
    "ModelingOperationActionDeformerCreate": ".modeling_operation_action_deformer_create",
    "ModelingOperationActionDeformerCreateDeformer": ".modeling_operation_action_deformer_create_deformer",
    "ModelingOperationActionDeformerCreateDeformerBindingsItem": ".modeling_operation_action_deformer_create_deformer_bindings_item",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemComposition": ".modeling_operation_action_deformer_create_deformer_bindings_item_composition",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemCompositionOne": ".modeling_operation_action_deformer_create_deformer_bindings_item_composition_one",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemCompositionZero": ".modeling_operation_action_deformer_create_deformer_bindings_item_composition_zero",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemCurve": ".modeling_operation_action_deformer_create_deformer_bindings_item_curve",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemCurveControlPointsItem": ".modeling_operation_action_deformer_create_deformer_bindings_item_curve_control_points_item",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemInterpolation": ".modeling_operation_action_deformer_create_deformer_bindings_item_interpolation",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemInterpolationFour": ".modeling_operation_action_deformer_create_deformer_bindings_item_interpolation_four",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemInterpolationOne": ".modeling_operation_action_deformer_create_deformer_bindings_item_interpolation_one",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemInterpolationThree": ".modeling_operation_action_deformer_create_deformer_bindings_item_interpolation_three",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemInterpolationTwo": ".modeling_operation_action_deformer_create_deformer_bindings_item_interpolation_two",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemInterpolationZero": ".modeling_operation_action_deformer_create_deformer_bindings_item_interpolation_zero",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemKeysItem": ".modeling_operation_action_deformer_create_deformer_bindings_item_keys_item",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemProperty": ".modeling_operation_action_deformer_create_deformer_bindings_item_property",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemPropertyEight": ".modeling_operation_action_deformer_create_deformer_bindings_item_property_eight",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemPropertyFive": ".modeling_operation_action_deformer_create_deformer_bindings_item_property_five",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemPropertyFour": ".modeling_operation_action_deformer_create_deformer_bindings_item_property_four",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemPropertyNine": ".modeling_operation_action_deformer_create_deformer_bindings_item_property_nine",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemPropertyOne": ".modeling_operation_action_deformer_create_deformer_bindings_item_property_one",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemPropertySeven": ".modeling_operation_action_deformer_create_deformer_bindings_item_property_seven",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemPropertySix": ".modeling_operation_action_deformer_create_deformer_bindings_item_property_six",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemPropertyThree": ".modeling_operation_action_deformer_create_deformer_bindings_item_property_three",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemPropertyTwo": ".modeling_operation_action_deformer_create_deformer_bindings_item_property_two",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemPropertyZero": ".modeling_operation_action_deformer_create_deformer_bindings_item_property_zero",
    "ModelingOperationActionDeformerCreateDeformerBlendShapesItem": ".modeling_operation_action_deformer_create_deformer_blend_shapes_item",
    "ModelingOperationActionDeformerCreateDeformerBlendShapesItemCurve": ".modeling_operation_action_deformer_create_deformer_blend_shapes_item_curve",
    "ModelingOperationActionDeformerCreateDeformerBlendShapesItemCurveControlPointsItem": ".modeling_operation_action_deformer_create_deformer_blend_shapes_item_curve_control_points_item",
    "ModelingOperationActionDeformerCreateDeformerBlendShapesItemInterpolation": ".modeling_operation_action_deformer_create_deformer_blend_shapes_item_interpolation",
    "ModelingOperationActionDeformerCreateDeformerBlendShapesItemInterpolationFour": ".modeling_operation_action_deformer_create_deformer_blend_shapes_item_interpolation_four",
    "ModelingOperationActionDeformerCreateDeformerBlendShapesItemInterpolationOne": ".modeling_operation_action_deformer_create_deformer_blend_shapes_item_interpolation_one",
    "ModelingOperationActionDeformerCreateDeformerBlendShapesItemInterpolationThree": ".modeling_operation_action_deformer_create_deformer_blend_shapes_item_interpolation_three",
    "ModelingOperationActionDeformerCreateDeformerBlendShapesItemInterpolationTwo": ".modeling_operation_action_deformer_create_deformer_blend_shapes_item_interpolation_two",
    "ModelingOperationActionDeformerCreateDeformerBlendShapesItemInterpolationZero": ".modeling_operation_action_deformer_create_deformer_blend_shapes_item_interpolation_zero",
    "ModelingOperationActionDeformerCreateDeformerBlendShapesItemKind": ".modeling_operation_action_deformer_create_deformer_blend_shapes_item_kind",
    "ModelingOperationActionDeformerCreateDeformerBlendShapesItemPinsItem": ".modeling_operation_action_deformer_create_deformer_blend_shapes_item_pins_item",
    "ModelingOperationActionDeformerCreateDeformerBlendShapesItemSharedPointsItem": ".modeling_operation_action_deformer_create_deformer_blend_shapes_item_shared_points_item",
    "ModelingOperationActionDeformerCreateDeformerBlendShapesItemTransform": ".modeling_operation_action_deformer_create_deformer_blend_shapes_item_transform",
    "ModelingOperationActionDeformerCreateDeformerBlendShapesItemWarp": ".modeling_operation_action_deformer_create_deformer_blend_shapes_item_warp",
    "ModelingOperationActionDeformerCreateDeformerKind": ".modeling_operation_action_deformer_create_deformer_kind",
    "ModelingOperationActionDeformerCreateDeformerKindOne": ".modeling_operation_action_deformer_create_deformer_kind_one",
    "ModelingOperationActionDeformerCreateDeformerKindTwo": ".modeling_operation_action_deformer_create_deformer_kind_two",
    "ModelingOperationActionDeformerCreateDeformerKindZero": ".modeling_operation_action_deformer_create_deformer_kind_zero",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItem": ".modeling_operation_action_deformer_create_deformer_multi_bindings_item",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemComposition": ".modeling_operation_action_deformer_create_deformer_multi_bindings_item_composition",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemCompositionOne": ".modeling_operation_action_deformer_create_deformer_multi_bindings_item_composition_one",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemCompositionZero": ".modeling_operation_action_deformer_create_deformer_multi_bindings_item_composition_zero",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemCurve": ".modeling_operation_action_deformer_create_deformer_multi_bindings_item_curve",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemCurveControlPointsItem": ".modeling_operation_action_deformer_create_deformer_multi_bindings_item_curve_control_points_item",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemInterpolation": ".modeling_operation_action_deformer_create_deformer_multi_bindings_item_interpolation",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemInterpolationFour": ".modeling_operation_action_deformer_create_deformer_multi_bindings_item_interpolation_four",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemInterpolationOne": ".modeling_operation_action_deformer_create_deformer_multi_bindings_item_interpolation_one",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemInterpolationThree": ".modeling_operation_action_deformer_create_deformer_multi_bindings_item_interpolation_three",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemInterpolationTwo": ".modeling_operation_action_deformer_create_deformer_multi_bindings_item_interpolation_two",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemInterpolationZero": ".modeling_operation_action_deformer_create_deformer_multi_bindings_item_interpolation_zero",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemKeyformsItem": ".modeling_operation_action_deformer_create_deformer_multi_bindings_item_keyforms_item",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemProperty": ".modeling_operation_action_deformer_create_deformer_multi_bindings_item_property",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertyEight": ".modeling_operation_action_deformer_create_deformer_multi_bindings_item_property_eight",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertyEleven": ".modeling_operation_action_deformer_create_deformer_multi_bindings_item_property_eleven",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertyFive": ".modeling_operation_action_deformer_create_deformer_multi_bindings_item_property_five",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertyFour": ".modeling_operation_action_deformer_create_deformer_multi_bindings_item_property_four",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertyNine": ".modeling_operation_action_deformer_create_deformer_multi_bindings_item_property_nine",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertyOne": ".modeling_operation_action_deformer_create_deformer_multi_bindings_item_property_one",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertySeven": ".modeling_operation_action_deformer_create_deformer_multi_bindings_item_property_seven",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertySix": ".modeling_operation_action_deformer_create_deformer_multi_bindings_item_property_six",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertyTen": ".modeling_operation_action_deformer_create_deformer_multi_bindings_item_property_ten",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertyThree": ".modeling_operation_action_deformer_create_deformer_multi_bindings_item_property_three",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertyTwo": ".modeling_operation_action_deformer_create_deformer_multi_bindings_item_property_two",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertyZero": ".modeling_operation_action_deformer_create_deformer_multi_bindings_item_property_zero",
    "ModelingOperationActionDeformerCreateDeformerOrigin": ".modeling_operation_action_deformer_create_deformer_origin",
    "ModelingOperationActionDeformerCreateDeformerRotationMetadata": ".modeling_operation_action_deformer_create_deformer_rotation_metadata",
    "ModelingOperationActionDeformerCreateDeformerRotationMetadataAngleRange": ".modeling_operation_action_deformer_create_deformer_rotation_metadata_angle_range",
    "ModelingOperationActionDeformerCreateDeformerRotationMetadataAngleUnit": ".modeling_operation_action_deformer_create_deformer_rotation_metadata_angle_unit",
    "ModelingOperationActionDeformerCreateDeformerRotationMetadataParentComposition": ".modeling_operation_action_deformer_create_deformer_rotation_metadata_parent_composition",
    "ModelingOperationActionDeformerCreateDeformerRotationMetadataParentCompositionOne": ".modeling_operation_action_deformer_create_deformer_rotation_metadata_parent_composition_one",
    "ModelingOperationActionDeformerCreateDeformerRotationMetadataParentCompositionZero": ".modeling_operation_action_deformer_create_deformer_rotation_metadata_parent_composition_zero",
    "ModelingOperationActionDeformerCreateDeformerRotationMetadataPivot": ".modeling_operation_action_deformer_create_deformer_rotation_metadata_pivot",
    "ModelingOperationActionDeformerCreateDeformerRotationMetadataPivotSpace": ".modeling_operation_action_deformer_create_deformer_rotation_metadata_pivot_space",
    "ModelingOperationActionDeformerCreateDeformerRotationMetadataPivotSpaceOne": ".modeling_operation_action_deformer_create_deformer_rotation_metadata_pivot_space_one",
    "ModelingOperationActionDeformerCreateDeformerRotationMetadataPivotSpaceZero": ".modeling_operation_action_deformer_create_deformer_rotation_metadata_pivot_space_zero",
    "ModelingOperationActionDeformerCreateDeformerRotationMetadataShapePreservation": ".modeling_operation_action_deformer_create_deformer_rotation_metadata_shape_preservation",
    "ModelingOperationActionDeformerCreateDeformerRotationMetadataShapePreservationOne": ".modeling_operation_action_deformer_create_deformer_rotation_metadata_shape_preservation_one",
    "ModelingOperationActionDeformerCreateDeformerRotationMetadataShapePreservationTwo": ".modeling_operation_action_deformer_create_deformer_rotation_metadata_shape_preservation_two",
    "ModelingOperationActionDeformerCreateDeformerRotationMetadataShapePreservationZero": ".modeling_operation_action_deformer_create_deformer_rotation_metadata_shape_preservation_zero",
    "ModelingOperationActionDeformerCreateDeformerSharedWarp": ".modeling_operation_action_deformer_create_deformer_shared_warp",
    "ModelingOperationActionDeformerCreateDeformerSharedWarpBounds": ".modeling_operation_action_deformer_create_deformer_shared_warp_bounds",
    "ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItem": ".modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item",
    "ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItem": ".modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item",
    "ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemCurve": ".modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_curve",
    "ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemCurveControlPointsItem": ".modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_curve_control_points_item",
    "ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolation": ".modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_interpolation",
    "ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolationFour": ".modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_interpolation_four",
    "ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolationOne": ".modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_interpolation_one",
    "ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolationThree": ".modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_interpolation_three",
    "ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolationTwo": ".modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_interpolation_two",
    "ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolationZero": ".modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_interpolation_zero",
    "ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemKeysItem": ".modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_keys_item",
    "ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemProperty": ".modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_property",
    "ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemPropertyOne": ".modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_property_one",
    "ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemPropertyZero": ".modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_property_zero",
    "ModelingOperationActionDeformerCreateDeformerSharedWarpGrid": ".modeling_operation_action_deformer_create_deformer_shared_warp_grid",
    "ModelingOperationActionDeformerCreateDeformerTransform": ".modeling_operation_action_deformer_create_deformer_transform",
    "ModelingOperationActionDeformerCreateDeformerWarp": ".modeling_operation_action_deformer_create_deformer_warp",
    "ModelingOperationActionDeformerCreateDeformerWarpGrid": ".modeling_operation_action_deformer_create_deformer_warp_grid",
    "ModelingOperationActionDeformerCreateDeformerWarpPinBlendMode": ".modeling_operation_action_deformer_create_deformer_warp_pin_blend_mode",
    "ModelingOperationActionDeformerCreateDeformerWarpPinBlendModeOne": ".modeling_operation_action_deformer_create_deformer_warp_pin_blend_mode_one",
    "ModelingOperationActionDeformerCreateDeformerWarpPinBlendModeZero": ".modeling_operation_action_deformer_create_deformer_warp_pin_blend_mode_zero",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItem": ".modeling_operation_action_deformer_create_deformer_warp_pins_item",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItem": ".modeling_operation_action_deformer_create_deformer_warp_pins_item_bindings_item",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemCurve": ".modeling_operation_action_deformer_create_deformer_warp_pins_item_bindings_item_curve",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemCurveControlPointsItem": ".modeling_operation_action_deformer_create_deformer_warp_pins_item_bindings_item_curve_control_points_item",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolation": ".modeling_operation_action_deformer_create_deformer_warp_pins_item_bindings_item_interpolation",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolationFour": ".modeling_operation_action_deformer_create_deformer_warp_pins_item_bindings_item_interpolation_four",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolationOne": ".modeling_operation_action_deformer_create_deformer_warp_pins_item_bindings_item_interpolation_one",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolationThree": ".modeling_operation_action_deformer_create_deformer_warp_pins_item_bindings_item_interpolation_three",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolationTwo": ".modeling_operation_action_deformer_create_deformer_warp_pins_item_bindings_item_interpolation_two",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolationZero": ".modeling_operation_action_deformer_create_deformer_warp_pins_item_bindings_item_interpolation_zero",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemKeysItem": ".modeling_operation_action_deformer_create_deformer_warp_pins_item_bindings_item_keys_item",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemProperty": ".modeling_operation_action_deformer_create_deformer_warp_pins_item_bindings_item_property",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemPropertyOne": ".modeling_operation_action_deformer_create_deformer_warp_pins_item_bindings_item_property_one",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemPropertyZero": ".modeling_operation_action_deformer_create_deformer_warp_pins_item_bindings_item_property_zero",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItem": ".modeling_operation_action_deformer_create_deformer_warp_pins_item_multi_bindings_item",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemCurve": ".modeling_operation_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_curve",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemCurveControlPointsItem": ".modeling_operation_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_curve_control_points_item",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolation": ".modeling_operation_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_interpolation",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolationFour": ".modeling_operation_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_interpolation_four",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolationOne": ".modeling_operation_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_interpolation_one",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolationThree": ".modeling_operation_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_interpolation_three",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolationTwo": ".modeling_operation_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_interpolation_two",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolationZero": ".modeling_operation_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_interpolation_zero",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemKeyformsItem": ".modeling_operation_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_keyforms_item",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemProperty": ".modeling_operation_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_property",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemPropertyOne": ".modeling_operation_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_property_one",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemPropertyZero": ".modeling_operation_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_property_zero",
    "ModelingOperationActionDeformerKindSet": ".modeling_operation_action_deformer_kind_set",
    "ModelingOperationActionDeformerKindSetKind": ".modeling_operation_action_deformer_kind_set_kind",
    "ModelingOperationActionDeformerKindSetKindOne": ".modeling_operation_action_deformer_kind_set_kind_one",
    "ModelingOperationActionDeformerKindSetKindTwo": ".modeling_operation_action_deformer_kind_set_kind_two",
    "ModelingOperationActionDeformerKindSetKindZero": ".modeling_operation_action_deformer_kind_set_kind_zero",
    "ModelingOperationActionDeformerKindSetWarp": ".modeling_operation_action_deformer_kind_set_warp",
    "ModelingOperationActionDeformerKindSetWarpGrid": ".modeling_operation_action_deformer_kind_set_warp_grid",
    "ModelingOperationActionDeformerKindSetWarpPinBlendMode": ".modeling_operation_action_deformer_kind_set_warp_pin_blend_mode",
    "ModelingOperationActionDeformerKindSetWarpPinBlendModeOne": ".modeling_operation_action_deformer_kind_set_warp_pin_blend_mode_one",
    "ModelingOperationActionDeformerKindSetWarpPinBlendModeZero": ".modeling_operation_action_deformer_kind_set_warp_pin_blend_mode_zero",
    "ModelingOperationActionDeformerKindSetWarpPinsItem": ".modeling_operation_action_deformer_kind_set_warp_pins_item",
    "ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItem": ".modeling_operation_action_deformer_kind_set_warp_pins_item_bindings_item",
    "ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemCurve": ".modeling_operation_action_deformer_kind_set_warp_pins_item_bindings_item_curve",
    "ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemCurveControlPointsItem": ".modeling_operation_action_deformer_kind_set_warp_pins_item_bindings_item_curve_control_points_item",
    "ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemInterpolation": ".modeling_operation_action_deformer_kind_set_warp_pins_item_bindings_item_interpolation",
    "ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemInterpolationFour": ".modeling_operation_action_deformer_kind_set_warp_pins_item_bindings_item_interpolation_four",
    "ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemInterpolationOne": ".modeling_operation_action_deformer_kind_set_warp_pins_item_bindings_item_interpolation_one",
    "ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemInterpolationThree": ".modeling_operation_action_deformer_kind_set_warp_pins_item_bindings_item_interpolation_three",
    "ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemInterpolationTwo": ".modeling_operation_action_deformer_kind_set_warp_pins_item_bindings_item_interpolation_two",
    "ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemInterpolationZero": ".modeling_operation_action_deformer_kind_set_warp_pins_item_bindings_item_interpolation_zero",
    "ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemKeysItem": ".modeling_operation_action_deformer_kind_set_warp_pins_item_bindings_item_keys_item",
    "ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemProperty": ".modeling_operation_action_deformer_kind_set_warp_pins_item_bindings_item_property",
    "ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemPropertyOne": ".modeling_operation_action_deformer_kind_set_warp_pins_item_bindings_item_property_one",
    "ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemPropertyZero": ".modeling_operation_action_deformer_kind_set_warp_pins_item_bindings_item_property_zero",
    "ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItem": ".modeling_operation_action_deformer_kind_set_warp_pins_item_multi_bindings_item",
    "ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemCurve": ".modeling_operation_action_deformer_kind_set_warp_pins_item_multi_bindings_item_curve",
    "ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemCurveControlPointsItem": ".modeling_operation_action_deformer_kind_set_warp_pins_item_multi_bindings_item_curve_control_points_item",
    "ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolation": ".modeling_operation_action_deformer_kind_set_warp_pins_item_multi_bindings_item_interpolation",
    "ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolationFour": ".modeling_operation_action_deformer_kind_set_warp_pins_item_multi_bindings_item_interpolation_four",
    "ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolationOne": ".modeling_operation_action_deformer_kind_set_warp_pins_item_multi_bindings_item_interpolation_one",
    "ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolationThree": ".modeling_operation_action_deformer_kind_set_warp_pins_item_multi_bindings_item_interpolation_three",
    "ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolationTwo": ".modeling_operation_action_deformer_kind_set_warp_pins_item_multi_bindings_item_interpolation_two",
    "ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolationZero": ".modeling_operation_action_deformer_kind_set_warp_pins_item_multi_bindings_item_interpolation_zero",
    "ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemKeyformsItem": ".modeling_operation_action_deformer_kind_set_warp_pins_item_multi_bindings_item_keyforms_item",
    "ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemProperty": ".modeling_operation_action_deformer_kind_set_warp_pins_item_multi_bindings_item_property",
    "ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemPropertyOne": ".modeling_operation_action_deformer_kind_set_warp_pins_item_multi_bindings_item_property_one",
    "ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemPropertyZero": ".modeling_operation_action_deformer_kind_set_warp_pins_item_multi_bindings_item_property_zero",
    "ModelingOperationActionDeformerOrigin": ".modeling_operation_action_deformer_origin",
    "ModelingOperationActionDeformerParentSet": ".modeling_operation_action_deformer_parent_set",
    "ModelingOperationActionDeformerRotationMetadata": ".modeling_operation_action_deformer_rotation_metadata",
    "ModelingOperationActionDeformerRotationMetadataMetadata": ".modeling_operation_action_deformer_rotation_metadata_metadata",
    "ModelingOperationActionDeformerRotationMetadataMetadataAngleRange": ".modeling_operation_action_deformer_rotation_metadata_metadata_angle_range",
    "ModelingOperationActionDeformerRotationMetadataMetadataAngleUnit": ".modeling_operation_action_deformer_rotation_metadata_metadata_angle_unit",
    "ModelingOperationActionDeformerRotationMetadataMetadataParentComposition": ".modeling_operation_action_deformer_rotation_metadata_metadata_parent_composition",
    "ModelingOperationActionDeformerRotationMetadataMetadataParentCompositionOne": ".modeling_operation_action_deformer_rotation_metadata_metadata_parent_composition_one",
    "ModelingOperationActionDeformerRotationMetadataMetadataParentCompositionZero": ".modeling_operation_action_deformer_rotation_metadata_metadata_parent_composition_zero",
    "ModelingOperationActionDeformerRotationMetadataMetadataPivot": ".modeling_operation_action_deformer_rotation_metadata_metadata_pivot",
    "ModelingOperationActionDeformerRotationMetadataMetadataPivotSpace": ".modeling_operation_action_deformer_rotation_metadata_metadata_pivot_space",
    "ModelingOperationActionDeformerRotationMetadataMetadataPivotSpaceOne": ".modeling_operation_action_deformer_rotation_metadata_metadata_pivot_space_one",
    "ModelingOperationActionDeformerRotationMetadataMetadataPivotSpaceZero": ".modeling_operation_action_deformer_rotation_metadata_metadata_pivot_space_zero",
    "ModelingOperationActionDeformerRotationMetadataMetadataShapePreservation": ".modeling_operation_action_deformer_rotation_metadata_metadata_shape_preservation",
    "ModelingOperationActionDeformerRotationMetadataMetadataShapePreservationOne": ".modeling_operation_action_deformer_rotation_metadata_metadata_shape_preservation_one",
    "ModelingOperationActionDeformerRotationMetadataMetadataShapePreservationTwo": ".modeling_operation_action_deformer_rotation_metadata_metadata_shape_preservation_two",
    "ModelingOperationActionDeformerRotationMetadataMetadataShapePreservationZero": ".modeling_operation_action_deformer_rotation_metadata_metadata_shape_preservation_zero",
    "ModelingOperationActionDeformerSplit": ".modeling_operation_action_deformer_split",
    "ModelingOperationActionDeformerTargetsSet": ".modeling_operation_action_deformer_targets_set",
    "ModelingOperationActionDeformerTargetsSetMode": ".modeling_operation_action_deformer_targets_set_mode",
    "ModelingOperationActionDeformerTargetsSetModeOne": ".modeling_operation_action_deformer_targets_set_mode_one",
    "ModelingOperationActionDeformerTargetsSetModeZero": ".modeling_operation_action_deformer_targets_set_mode_zero",
    "ModelingOperationActionDeformerTransform": ".modeling_operation_action_deformer_transform",
    "ModelingOperationActionDeformerTransformOperator": ".modeling_operation_action_deformer_transform_operator",
    "ModelingOperationActionDeformerTransformOperatorOne": ".modeling_operation_action_deformer_transform_operator_one",
    "ModelingOperationActionDeformerTransformOperatorTwo": ".modeling_operation_action_deformer_transform_operator_two",
    "ModelingOperationActionDeformerTransformOperatorZero": ".modeling_operation_action_deformer_transform_operator_zero",
    "ModelingOperationActionDeformerTransformProperty": ".modeling_operation_action_deformer_transform_property",
    "ModelingOperationActionDeformerTransformPropertyFive": ".modeling_operation_action_deformer_transform_property_five",
    "ModelingOperationActionDeformerTransformPropertyFour": ".modeling_operation_action_deformer_transform_property_four",
    "ModelingOperationActionDeformerTransformPropertyOne": ".modeling_operation_action_deformer_transform_property_one",
    "ModelingOperationActionDeformerTransformPropertyThree": ".modeling_operation_action_deformer_transform_property_three",
    "ModelingOperationActionDeformerTransformPropertyTwo": ".modeling_operation_action_deformer_transform_property_two",
    "ModelingOperationActionDeformerTransformPropertyZero": ".modeling_operation_action_deformer_transform_property_zero",
    "ModelingOperationActionParameterAdd": ".modeling_operation_action_parameter_add",
    "ModelingOperationActionParameterAddParameter": ".modeling_operation_action_parameter_add_parameter",
    "ModelingOperationActionPartAlphaReveal": ".modeling_operation_action_part_alpha_reveal",
    "ModelingOperationActionPartAlphaRevealReveal": ".modeling_operation_action_part_alpha_reveal_reveal",
    "ModelingOperationActionPartBlendMode": ".modeling_operation_action_part_blend_mode",
    "ModelingOperationActionPartBlendModeMode": ".modeling_operation_action_part_blend_mode_mode",
    "ModelingOperationActionPartBlendModeModeOne": ".modeling_operation_action_part_blend_mode_mode_one",
    "ModelingOperationActionPartBlendModeModeThree": ".modeling_operation_action_part_blend_mode_mode_three",
    "ModelingOperationActionPartBlendModeModeTwo": ".modeling_operation_action_part_blend_mode_mode_two",
    "ModelingOperationActionPartBlendModeModeZero": ".modeling_operation_action_part_blend_mode_mode_zero",
    "ModelingOperationActionPartClip": ".modeling_operation_action_part_clip",
    "ModelingOperationActionPartClipClip": ".modeling_operation_action_part_clip_clip",
    "ModelingOperationActionPartClipClipMaskOpacity": ".modeling_operation_action_part_clip_clip_mask_opacity",
    "ModelingOperationActionPartClipClipMaskOpacityOne": ".modeling_operation_action_part_clip_clip_mask_opacity_one",
    "ModelingOperationActionPartClipClipMaskOpacityZero": ".modeling_operation_action_part_clip_clip_mask_opacity_zero",
    "ModelingOperationActionPartClipClipMode": ".modeling_operation_action_part_clip_clip_mode",
    "ModelingOperationActionPartContourShade": ".modeling_operation_action_part_contour_shade",
    "ModelingOperationActionPartContourShadeShade": ".modeling_operation_action_part_contour_shade_shade",
    "ModelingOperationActionPartContourShadeShadeProfile": ".modeling_operation_action_part_contour_shade_shade_profile",
    "ModelingOperationActionPartDrawOrder": ".modeling_operation_action_part_draw_order",
    "ModelingOperationActionPartTint": ".modeling_operation_action_part_tint",
    "ModelingOperationActionPartTintTint": ".modeling_operation_action_part_tint_tint",
    "ModelingOperationActionPartTintTintMode": ".modeling_operation_action_part_tint_tint_mode",
    "ModelingOperationActionPartTintTintModeOne": ".modeling_operation_action_part_tint_tint_mode_one",
    "ModelingOperationActionPartTintTintModeZero": ".modeling_operation_action_part_tint_tint_mode_zero",
    "ModelingOperationActionPartVisibility": ".modeling_operation_action_part_visibility",
    "ModelingOperationActionRoleConfirm": ".modeling_operation_action_role_confirm",
    "ModelingOperationActionRoleConfirmRole": ".modeling_operation_action_role_confirm_role",
    "ModelingOperationActionRoleConfirmRoleEight": ".modeling_operation_action_role_confirm_role_eight",
    "ModelingOperationActionRoleConfirmRoleEleven": ".modeling_operation_action_role_confirm_role_eleven",
    "ModelingOperationActionRoleConfirmRoleFifteen": ".modeling_operation_action_role_confirm_role_fifteen",
    "ModelingOperationActionRoleConfirmRoleFive": ".modeling_operation_action_role_confirm_role_five",
    "ModelingOperationActionRoleConfirmRoleFour": ".modeling_operation_action_role_confirm_role_four",
    "ModelingOperationActionRoleConfirmRoleFourteen": ".modeling_operation_action_role_confirm_role_fourteen",
    "ModelingOperationActionRoleConfirmRoleNine": ".modeling_operation_action_role_confirm_role_nine",
    "ModelingOperationActionRoleConfirmRoleOne": ".modeling_operation_action_role_confirm_role_one",
    "ModelingOperationActionRoleConfirmRoleSeven": ".modeling_operation_action_role_confirm_role_seven",
    "ModelingOperationActionRoleConfirmRoleSeventeen": ".modeling_operation_action_role_confirm_role_seventeen",
    "ModelingOperationActionRoleConfirmRoleSix": ".modeling_operation_action_role_confirm_role_six",
    "ModelingOperationActionRoleConfirmRoleSixteen": ".modeling_operation_action_role_confirm_role_sixteen",
    "ModelingOperationActionRoleConfirmRoleTen": ".modeling_operation_action_role_confirm_role_ten",
    "ModelingOperationActionRoleConfirmRoleThirteen": ".modeling_operation_action_role_confirm_role_thirteen",
    "ModelingOperationActionRoleConfirmRoleThree": ".modeling_operation_action_role_confirm_role_three",
    "ModelingOperationActionRoleConfirmRoleTwelve": ".modeling_operation_action_role_confirm_role_twelve",
    "ModelingOperationActionRoleConfirmRoleTwo": ".modeling_operation_action_role_confirm_role_two",
    "ModelingOperationActionRoleConfirmRoleZero": ".modeling_operation_action_role_confirm_role_zero",
    "ModelingOperationActionRoleReclassify": ".modeling_operation_action_role_reclassify",
    "ModelingOperationActionRoleReclassifyExpectedRole": ".modeling_operation_action_role_reclassify_expected_role",
    "ModelingOperationActionRoleReclassifyExpectedRoleEight": ".modeling_operation_action_role_reclassify_expected_role_eight",
    "ModelingOperationActionRoleReclassifyExpectedRoleEleven": ".modeling_operation_action_role_reclassify_expected_role_eleven",
    "ModelingOperationActionRoleReclassifyExpectedRoleFifteen": ".modeling_operation_action_role_reclassify_expected_role_fifteen",
    "ModelingOperationActionRoleReclassifyExpectedRoleFive": ".modeling_operation_action_role_reclassify_expected_role_five",
    "ModelingOperationActionRoleReclassifyExpectedRoleFour": ".modeling_operation_action_role_reclassify_expected_role_four",
    "ModelingOperationActionRoleReclassifyExpectedRoleFourteen": ".modeling_operation_action_role_reclassify_expected_role_fourteen",
    "ModelingOperationActionRoleReclassifyExpectedRoleNine": ".modeling_operation_action_role_reclassify_expected_role_nine",
    "ModelingOperationActionRoleReclassifyExpectedRoleOne": ".modeling_operation_action_role_reclassify_expected_role_one",
    "ModelingOperationActionRoleReclassifyExpectedRoleSeven": ".modeling_operation_action_role_reclassify_expected_role_seven",
    "ModelingOperationActionRoleReclassifyExpectedRoleSeventeen": ".modeling_operation_action_role_reclassify_expected_role_seventeen",
    "ModelingOperationActionRoleReclassifyExpectedRoleSix": ".modeling_operation_action_role_reclassify_expected_role_six",
    "ModelingOperationActionRoleReclassifyExpectedRoleSixteen": ".modeling_operation_action_role_reclassify_expected_role_sixteen",
    "ModelingOperationActionRoleReclassifyExpectedRoleTen": ".modeling_operation_action_role_reclassify_expected_role_ten",
    "ModelingOperationActionRoleReclassifyExpectedRoleThirteen": ".modeling_operation_action_role_reclassify_expected_role_thirteen",
    "ModelingOperationActionRoleReclassifyExpectedRoleThree": ".modeling_operation_action_role_reclassify_expected_role_three",
    "ModelingOperationActionRoleReclassifyExpectedRoleTwelve": ".modeling_operation_action_role_reclassify_expected_role_twelve",
    "ModelingOperationActionRoleReclassifyExpectedRoleTwo": ".modeling_operation_action_role_reclassify_expected_role_two",
    "ModelingOperationActionRoleReclassifyExpectedRoleZero": ".modeling_operation_action_role_reclassify_expected_role_zero",
    "ModelingOperationActionRoleReclassifyRole": ".modeling_operation_action_role_reclassify_role",
    "ModelingOperationActionRoleReclassifyRoleEight": ".modeling_operation_action_role_reclassify_role_eight",
    "ModelingOperationActionRoleReclassifyRoleEleven": ".modeling_operation_action_role_reclassify_role_eleven",
    "ModelingOperationActionRoleReclassifyRoleFifteen": ".modeling_operation_action_role_reclassify_role_fifteen",
    "ModelingOperationActionRoleReclassifyRoleFive": ".modeling_operation_action_role_reclassify_role_five",
    "ModelingOperationActionRoleReclassifyRoleFour": ".modeling_operation_action_role_reclassify_role_four",
    "ModelingOperationActionRoleReclassifyRoleFourteen": ".modeling_operation_action_role_reclassify_role_fourteen",
    "ModelingOperationActionRoleReclassifyRoleNine": ".modeling_operation_action_role_reclassify_role_nine",
    "ModelingOperationActionRoleReclassifyRoleOne": ".modeling_operation_action_role_reclassify_role_one",
    "ModelingOperationActionRoleReclassifyRoleSeven": ".modeling_operation_action_role_reclassify_role_seven",
    "ModelingOperationActionRoleReclassifyRoleSeventeen": ".modeling_operation_action_role_reclassify_role_seventeen",
    "ModelingOperationActionRoleReclassifyRoleSix": ".modeling_operation_action_role_reclassify_role_six",
    "ModelingOperationActionRoleReclassifyRoleSixteen": ".modeling_operation_action_role_reclassify_role_sixteen",
    "ModelingOperationActionRoleReclassifyRoleTen": ".modeling_operation_action_role_reclassify_role_ten",
    "ModelingOperationActionRoleReclassifyRoleThirteen": ".modeling_operation_action_role_reclassify_role_thirteen",
    "ModelingOperationActionRoleReclassifyRoleThree": ".modeling_operation_action_role_reclassify_role_three",
    "ModelingOperationActionRoleReclassifyRoleTwelve": ".modeling_operation_action_role_reclassify_role_twelve",
    "ModelingOperationActionRoleReclassifyRoleTwo": ".modeling_operation_action_role_reclassify_role_two",
    "ModelingOperationActionRoleReclassifyRoleZero": ".modeling_operation_action_role_reclassify_role_zero",
    "ModelingOperationActionSymmetryArtmeshBindings": ".modeling_operation_action_symmetry_artmesh_bindings",
    "ModelingOperationActionSymmetryArtmeshBindingsLinksItem": ".modeling_operation_action_symmetry_artmesh_bindings_links_item",
    "ModelingOperationActionSymmetryArtmeshBindingsLinksItemAxis": ".modeling_operation_action_symmetry_artmesh_bindings_links_item_axis",
    "ModelingOperationActionSymmetryArtmeshBindingsLinksItemKind": ".modeling_operation_action_symmetry_artmesh_bindings_links_item_kind",
    "ModelingOperationActionSymmetryArtmeshBindingsLinksItemKindOne": ".modeling_operation_action_symmetry_artmesh_bindings_links_item_kind_one",
    "ModelingOperationActionSymmetryArtmeshBindingsLinksItemKindThree": ".modeling_operation_action_symmetry_artmesh_bindings_links_item_kind_three",
    "ModelingOperationActionSymmetryArtmeshBindingsLinksItemKindTwo": ".modeling_operation_action_symmetry_artmesh_bindings_links_item_kind_two",
    "ModelingOperationActionSymmetryArtmeshBindingsLinksItemKindZero": ".modeling_operation_action_symmetry_artmesh_bindings_links_item_kind_zero",
    "ModelingOperationActionSymmetryContract": ".modeling_operation_action_symmetry_contract",
    "ModelingOperationActionSymmetryContractContract": ".modeling_operation_action_symmetry_contract_contract",
    "ModelingOperationActionSymmetryContractContractAxis": ".modeling_operation_action_symmetry_contract_contract_axis",
    "ModelingOperationActionSymmetryContractContractLinksItem": ".modeling_operation_action_symmetry_contract_contract_links_item",
    "ModelingOperationActionSymmetryContractContractLinksItemAxis": ".modeling_operation_action_symmetry_contract_contract_links_item_axis",
    "ModelingOperationActionSymmetryContractContractLinksItemKind": ".modeling_operation_action_symmetry_contract_contract_links_item_kind",
    "ModelingOperationActionSymmetryContractContractLinksItemKindOne": ".modeling_operation_action_symmetry_contract_contract_links_item_kind_one",
    "ModelingOperationActionSymmetryContractContractLinksItemKindThree": ".modeling_operation_action_symmetry_contract_contract_links_item_kind_three",
    "ModelingOperationActionSymmetryContractContractLinksItemKindTwo": ".modeling_operation_action_symmetry_contract_contract_links_item_kind_two",
    "ModelingOperationActionSymmetryContractContractLinksItemKindZero": ".modeling_operation_action_symmetry_contract_contract_links_item_kind_zero",
    "ModelingOperationActionTransform": ".modeling_operation_action_transform",
    "ModelingOperationActionTransformOperator": ".modeling_operation_action_transform_operator",
    "ModelingOperationActionTransformOperatorOne": ".modeling_operation_action_transform_operator_one",
    "ModelingOperationActionTransformOperatorTwo": ".modeling_operation_action_transform_operator_two",
    "ModelingOperationActionTransformOperatorZero": ".modeling_operation_action_transform_operator_zero",
    "ModelingOperationActionTransformProperty": ".modeling_operation_action_transform_property",
    "ModelingOperationActionTransformPropertyFive": ".modeling_operation_action_transform_property_five",
    "ModelingOperationActionTransformPropertyFour": ".modeling_operation_action_transform_property_four",
    "ModelingOperationActionTransformPropertyOne": ".modeling_operation_action_transform_property_one",
    "ModelingOperationActionTransformPropertyThree": ".modeling_operation_action_transform_property_three",
    "ModelingOperationActionTransformPropertyTwo": ".modeling_operation_action_transform_property_two",
    "ModelingOperationActionTransformPropertyZero": ".modeling_operation_action_transform_property_zero",
    "ModelingOperationActionWarpPinBindingKey": ".modeling_operation_action_warp_pin_binding_key",
    "ModelingOperationActionWarpPinBindingKeyCurve": ".modeling_operation_action_warp_pin_binding_key_curve",
    "ModelingOperationActionWarpPinBindingKeyCurveControlPointsItem": ".modeling_operation_action_warp_pin_binding_key_curve_control_points_item",
    "ModelingOperationActionWarpPinBindingKeyInterpolation": ".modeling_operation_action_warp_pin_binding_key_interpolation",
    "ModelingOperationActionWarpPinBindingKeyInterpolationFour": ".modeling_operation_action_warp_pin_binding_key_interpolation_four",
    "ModelingOperationActionWarpPinBindingKeyInterpolationOne": ".modeling_operation_action_warp_pin_binding_key_interpolation_one",
    "ModelingOperationActionWarpPinBindingKeyInterpolationThree": ".modeling_operation_action_warp_pin_binding_key_interpolation_three",
    "ModelingOperationActionWarpPinBindingKeyInterpolationTwo": ".modeling_operation_action_warp_pin_binding_key_interpolation_two",
    "ModelingOperationActionWarpPinBindingKeyInterpolationZero": ".modeling_operation_action_warp_pin_binding_key_interpolation_zero",
    "ModelingOperationActionWarpPinBindingKeyProperty": ".modeling_operation_action_warp_pin_binding_key_property",
    "ModelingOperationActionWarpPinBindingKeyPropertyOne": ".modeling_operation_action_warp_pin_binding_key_property_one",
    "ModelingOperationActionWarpPinBindingKeyPropertyZero": ".modeling_operation_action_warp_pin_binding_key_property_zero",
    "ModelingOperationAction_ArtmeshBindingKey": ".modeling_operation_action",
    "ModelingOperationAction_ArtmeshBlendShape": ".modeling_operation_action",
    "ModelingOperationAction_ArtmeshGenerate": ".modeling_operation_action",
    "ModelingOperationAction_ArtmeshMirrorKey": ".modeling_operation_action",
    "ModelingOperationAction_ArtmeshMultiKey": ".modeling_operation_action",
    "ModelingOperationAction_ArtmeshOffset": ".modeling_operation_action",
    "ModelingOperationAction_ArtmeshQuality": ".modeling_operation_action",
    "ModelingOperationAction_ArtmeshRebuild": ".modeling_operation_action",
    "ModelingOperationAction_BindingKey": ".modeling_operation_action",
    "ModelingOperationAction_BlendShapeSet": ".modeling_operation_action",
    "ModelingOperationAction_DeformBrush": ".modeling_operation_action",
    "ModelingOperationAction_DeformerBindingKey": ".modeling_operation_action",
    "ModelingOperationAction_DeformerBindingRemove": ".modeling_operation_action",
    "ModelingOperationAction_DeformerCreate": ".modeling_operation_action",
    "ModelingOperationAction_DeformerKindSet": ".modeling_operation_action",
    "ModelingOperationAction_DeformerOrigin": ".modeling_operation_action",
    "ModelingOperationAction_DeformerParentSet": ".modeling_operation_action",
    "ModelingOperationAction_DeformerRotationMetadata": ".modeling_operation_action",
    "ModelingOperationAction_DeformerSplit": ".modeling_operation_action",
    "ModelingOperationAction_DeformerTargetsSet": ".modeling_operation_action",
    "ModelingOperationAction_DeformerTransform": ".modeling_operation_action",
    "ModelingOperationAction_ParameterAdd": ".modeling_operation_action",
    "ModelingOperationAction_PartAlphaReveal": ".modeling_operation_action",
    "ModelingOperationAction_PartBlendMode": ".modeling_operation_action",
    "ModelingOperationAction_PartClip": ".modeling_operation_action",
    "ModelingOperationAction_PartContourShade": ".modeling_operation_action",
    "ModelingOperationAction_PartDrawOrder": ".modeling_operation_action",
    "ModelingOperationAction_PartTint": ".modeling_operation_action",
    "ModelingOperationAction_PartVisibility": ".modeling_operation_action",
    "ModelingOperationAction_RoleConfirm": ".modeling_operation_action",
    "ModelingOperationAction_RoleReclassify": ".modeling_operation_action",
    "ModelingOperationAction_SymmetryArtmeshBindings": ".modeling_operation_action",
    "ModelingOperationAction_SymmetryContract": ".modeling_operation_action",
    "ModelingOperationAction_Transform": ".modeling_operation_action",
    "ModelingOperationAction_WarpPinBindingKey": ".modeling_operation_action",
    "ModelingOperationTarget": ".modeling_operation_target",
    "ModelingOperationTargetRolesItem": ".modeling_operation_target_roles_item",
    "ModelingOperationTargetRolesItemEight": ".modeling_operation_target_roles_item_eight",
    "ModelingOperationTargetRolesItemEleven": ".modeling_operation_target_roles_item_eleven",
    "ModelingOperationTargetRolesItemFifteen": ".modeling_operation_target_roles_item_fifteen",
    "ModelingOperationTargetRolesItemFive": ".modeling_operation_target_roles_item_five",
    "ModelingOperationTargetRolesItemFour": ".modeling_operation_target_roles_item_four",
    "ModelingOperationTargetRolesItemFourteen": ".modeling_operation_target_roles_item_fourteen",
    "ModelingOperationTargetRolesItemNine": ".modeling_operation_target_roles_item_nine",
    "ModelingOperationTargetRolesItemOne": ".modeling_operation_target_roles_item_one",
    "ModelingOperationTargetRolesItemSeven": ".modeling_operation_target_roles_item_seven",
    "ModelingOperationTargetRolesItemSeventeen": ".modeling_operation_target_roles_item_seventeen",
    "ModelingOperationTargetRolesItemSix": ".modeling_operation_target_roles_item_six",
    "ModelingOperationTargetRolesItemSixteen": ".modeling_operation_target_roles_item_sixteen",
    "ModelingOperationTargetRolesItemTen": ".modeling_operation_target_roles_item_ten",
    "ModelingOperationTargetRolesItemThirteen": ".modeling_operation_target_roles_item_thirteen",
    "ModelingOperationTargetRolesItemThree": ".modeling_operation_target_roles_item_three",
    "ModelingOperationTargetRolesItemTwelve": ".modeling_operation_target_roles_item_twelve",
    "ModelingOperationTargetRolesItemTwo": ".modeling_operation_target_roles_item_two",
    "ModelingOperationTargetRolesItemZero": ".modeling_operation_target_roles_item_zero",
    "MotionClip": ".motion_clip",
    "MotionClipFormat": ".motion_clip_format",
    "MotionClipTracksItem": ".motion_clip_tracks_item",
    "MotionClipTracksItemKeysItem": ".motion_clip_tracks_item_keys_item",
    "MotionClipTracksItemKeysItemSegment": ".motion_clip_tracks_item_keys_item_segment",
    "MotionClipTracksItemKeysItemSegmentControl1": ".motion_clip_tracks_item_keys_item_segment_control1",
    "MotionClipTracksItemKeysItemSegmentControl1Control1": ".motion_clip_tracks_item_keys_item_segment_control1control1",
    "MotionClipTracksItemKeysItemSegmentControl1Control2": ".motion_clip_tracks_item_keys_item_segment_control1control2",
    "MotionClipTracksItemKeysItemSegmentControl1Kind": ".motion_clip_tracks_item_keys_item_segment_control1kind",
    "MotionClipTracksItemKeysItemSegmentZero": ".motion_clip_tracks_item_keys_item_segment_zero",
    "MotionClipTracksItemKeysItemSegmentZeroKind": ".motion_clip_tracks_item_keys_item_segment_zero_kind",
    "MotionClipTracksItemKeysItemSegmentZeroKindOne": ".motion_clip_tracks_item_keys_item_segment_zero_kind_one",
    "MotionClipTracksItemKeysItemSegmentZeroKindTwo": ".motion_clip_tracks_item_keys_item_segment_zero_kind_two",
    "MotionClipTracksItemKeysItemSegmentZeroKindZero": ".motion_clip_tracks_item_keys_item_segment_zero_kind_zero",
    "MotionRequest": ".motion_request",
    "MotionRequestClip": ".motion_request_clip",
    "MotionRequestClipAction": ".motion_request_clip_action",
    "MotionRequestClipClip": ".motion_request_clip_clip",
    "MotionRequestClipClipFormat": ".motion_request_clip_clip_format",
    "MotionRequestClipClipTracksItem": ".motion_request_clip_clip_tracks_item",
    "MotionRequestClipClipTracksItemKeysItem": ".motion_request_clip_clip_tracks_item_keys_item",
    "MotionRequestClipClipTracksItemKeysItemSegment": ".motion_request_clip_clip_tracks_item_keys_item_segment",
    "MotionRequestClipClipTracksItemKeysItemSegmentControl1": ".motion_request_clip_clip_tracks_item_keys_item_segment_control1",
    "MotionRequestClipClipTracksItemKeysItemSegmentControl1Control1": ".motion_request_clip_clip_tracks_item_keys_item_segment_control1control1",
    "MotionRequestClipClipTracksItemKeysItemSegmentControl1Control2": ".motion_request_clip_clip_tracks_item_keys_item_segment_control1control2",
    "MotionRequestClipClipTracksItemKeysItemSegmentControl1Kind": ".motion_request_clip_clip_tracks_item_keys_item_segment_control1kind",
    "MotionRequestClipClipTracksItemKeysItemSegmentZero": ".motion_request_clip_clip_tracks_item_keys_item_segment_zero",
    "MotionRequestClipClipTracksItemKeysItemSegmentZeroKind": ".motion_request_clip_clip_tracks_item_keys_item_segment_zero_kind",
    "MotionRequestClipClipTracksItemKeysItemSegmentZeroKindOne": ".motion_request_clip_clip_tracks_item_keys_item_segment_zero_kind_one",
    "MotionRequestClipClipTracksItemKeysItemSegmentZeroKindTwo": ".motion_request_clip_clip_tracks_item_keys_item_segment_zero_kind_two",
    "MotionRequestClipClipTracksItemKeysItemSegmentZeroKindZero": ".motion_request_clip_clip_tracks_item_keys_item_segment_zero_kind_zero",
    "MotionRequestLoop": ".motion_request_loop",
    "MotionRequestLoopAction": ".motion_request_loop_action",
    "MotionRequestOne": ".motion_request_one",
    "MotionRequestOneAction": ".motion_request_one_action",
    "MotionRequestOneActionOne": ".motion_request_one_action_one",
    "MotionRequestOneActionThree": ".motion_request_one_action_three",
    "MotionRequestOneActionTwo": ".motion_request_one_action_two",
    "MotionRequestOneActionZero": ".motion_request_one_action_zero",
    "MotionRequestTime": ".motion_request_time",
    "MotionRequestTimeAction": ".motion_request_time_action",
    "PostApiBridgePoseRequest": ".post_api_bridge_pose_request",
    "PostApiBridgePoseRequestClearParameterValues": ".post_api_bridge_pose_request_clear_parameter_values",
    "PostApiBridgePoseRequestClearParameterValuesData": ".post_api_bridge_pose_request_clear_parameter_values_data",
    "PostApiBridgePoseRequestSetParameterValues": ".post_api_bridge_pose_request_set_parameter_values",
    "PostApiBridgePoseRequestSetParameterValuesData": ".post_api_bridge_pose_request_set_parameter_values_data",
    "PostApiBridgePoseRequestSetParameterValuesDataParametersItem": ".post_api_bridge_pose_request_set_parameter_values_data_parameters_item",
    "PostApiBridgePoseRequest_ClearParameterValues": ".post_api_bridge_pose_request",
    "PostApiBridgePoseRequest_SetParameterValues": ".post_api_bridge_pose_request",
    "PostApiBridgeReadRequest": ".post_api_bridge_read_request",
    "PostApiBridgeReadRequestGetCurrentDocumentUid": ".post_api_bridge_read_request_get_current_document_uid",
    "PostApiBridgeReadRequestGetCurrentDocumentUidData": ".post_api_bridge_read_request_get_current_document_uid_data",
    "PostApiBridgeReadRequestGetCurrentEditMode": ".post_api_bridge_read_request_get_current_edit_mode",
    "PostApiBridgeReadRequestGetCurrentEditModeData": ".post_api_bridge_read_request_get_current_edit_mode_data",
    "PostApiBridgeReadRequestGetCurrentModelUid": ".post_api_bridge_read_request_get_current_model_uid",
    "PostApiBridgeReadRequestGetCurrentModelUidData": ".post_api_bridge_read_request_get_current_model_uid_data",
    "PostApiBridgeReadRequestGetDeformerStructure": ".post_api_bridge_read_request_get_deformer_structure",
    "PostApiBridgeReadRequestGetDeformerStructureData": ".post_api_bridge_read_request_get_deformer_structure_data",
    "PostApiBridgeReadRequestGetDocument": ".post_api_bridge_read_request_get_document",
    "PostApiBridgeReadRequestGetDocumentData": ".post_api_bridge_read_request_get_document_data",
    "PostApiBridgeReadRequestGetDocuments": ".post_api_bridge_read_request_get_documents",
    "PostApiBridgeReadRequestGetDocumentsData": ".post_api_bridge_read_request_get_documents_data",
    "PostApiBridgeReadRequestGetObject": ".post_api_bridge_read_request_get_object",
    "PostApiBridgeReadRequestGetObjectData": ".post_api_bridge_read_request_get_object_data",
    "PostApiBridgeReadRequestGetParameterGroups": ".post_api_bridge_read_request_get_parameter_groups",
    "PostApiBridgeReadRequestGetParameterGroupsData": ".post_api_bridge_read_request_get_parameter_groups_data",
    "PostApiBridgeReadRequestGetParameterValues": ".post_api_bridge_read_request_get_parameter_values",
    "PostApiBridgeReadRequestGetParameterValuesData": ".post_api_bridge_read_request_get_parameter_values_data",
    "PostApiBridgeReadRequestGetParameters": ".post_api_bridge_read_request_get_parameters",
    "PostApiBridgeReadRequestGetParametersData": ".post_api_bridge_read_request_get_parameters_data",
    "PostApiBridgeReadRequestGetPartStructure": ".post_api_bridge_read_request_get_part_structure",
    "PostApiBridgeReadRequestGetPartStructureData": ".post_api_bridge_read_request_get_part_structure_data",
    "PostApiBridgeReadRequestGetPhysicsInfo": ".post_api_bridge_read_request_get_physics_info",
    "PostApiBridgeReadRequestGetPhysicsInfoData": ".post_api_bridge_read_request_get_physics_info_data",
    "PostApiBridgeReadRequest_GetCurrentDocumentUid": ".post_api_bridge_read_request",
    "PostApiBridgeReadRequest_GetCurrentEditMode": ".post_api_bridge_read_request",
    "PostApiBridgeReadRequest_GetCurrentModelUid": ".post_api_bridge_read_request",
    "PostApiBridgeReadRequest_GetDeformerStructure": ".post_api_bridge_read_request",
    "PostApiBridgeReadRequest_GetDocument": ".post_api_bridge_read_request",
    "PostApiBridgeReadRequest_GetDocuments": ".post_api_bridge_read_request",
    "PostApiBridgeReadRequest_GetObject": ".post_api_bridge_read_request",
    "PostApiBridgeReadRequest_GetParameterGroups": ".post_api_bridge_read_request",
    "PostApiBridgeReadRequest_GetParameterValues": ".post_api_bridge_read_request",
    "PostApiBridgeReadRequest_GetParameters": ".post_api_bridge_read_request",
    "PostApiBridgeReadRequest_GetPartStructure": ".post_api_bridge_read_request",
    "PostApiBridgeReadRequest_GetPhysicsInfo": ".post_api_bridge_read_request",
    "PostApiPlaybackControlRequestCommand": ".post_api_playback_control_request_command",
    "PostApiPlaybackControlRequestMode": ".post_api_playback_control_request_mode",
    "PostApiPlaybackControlResponse": ".post_api_playback_control_response",
    "PostApiPlaybackControlResponsePlayback": ".post_api_playback_control_response_playback",
    "PostApiPlaybackControlResponsePlaybackDemo": ".post_api_playback_control_response_playback_demo",
    "PostApiPlaybackControlResponsePlaybackDemoMode": ".post_api_playback_control_response_playback_demo_mode",
    "PostApiPlaybackControlResponsePlaybackMotion": ".post_api_playback_control_response_playback_motion",
    "PostApiPlaybackMotionRequest": ".post_api_playback_motion_request",
    "PostApiPlaybackMotionRequestClip": ".post_api_playback_motion_request_clip",
    "PostApiPlaybackMotionRequestClipAction": ".post_api_playback_motion_request_clip_action",
    "PostApiPlaybackMotionRequestClipClip": ".post_api_playback_motion_request_clip_clip",
    "PostApiPlaybackMotionRequestClipClipFormat": ".post_api_playback_motion_request_clip_clip_format",
    "PostApiPlaybackMotionRequestClipClipTracksItem": ".post_api_playback_motion_request_clip_clip_tracks_item",
    "PostApiPlaybackMotionRequestClipClipTracksItemKeysItem": ".post_api_playback_motion_request_clip_clip_tracks_item_keys_item",
    "PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegment": ".post_api_playback_motion_request_clip_clip_tracks_item_keys_item_segment",
    "PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentControl1": ".post_api_playback_motion_request_clip_clip_tracks_item_keys_item_segment_control1",
    "PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentControl1Control1": ".post_api_playback_motion_request_clip_clip_tracks_item_keys_item_segment_control1control1",
    "PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentControl1Control2": ".post_api_playback_motion_request_clip_clip_tracks_item_keys_item_segment_control1control2",
    "PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentControl1Kind": ".post_api_playback_motion_request_clip_clip_tracks_item_keys_item_segment_control1kind",
    "PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentZero": ".post_api_playback_motion_request_clip_clip_tracks_item_keys_item_segment_zero",
    "PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentZeroKind": ".post_api_playback_motion_request_clip_clip_tracks_item_keys_item_segment_zero_kind",
    "PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentZeroKindOne": ".post_api_playback_motion_request_clip_clip_tracks_item_keys_item_segment_zero_kind_one",
    "PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentZeroKindTwo": ".post_api_playback_motion_request_clip_clip_tracks_item_keys_item_segment_zero_kind_two",
    "PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentZeroKindZero": ".post_api_playback_motion_request_clip_clip_tracks_item_keys_item_segment_zero_kind_zero",
    "PostApiPlaybackMotionRequestLoop": ".post_api_playback_motion_request_loop",
    "PostApiPlaybackMotionRequestLoopAction": ".post_api_playback_motion_request_loop_action",
    "PostApiPlaybackMotionRequestOne": ".post_api_playback_motion_request_one",
    "PostApiPlaybackMotionRequestOneAction": ".post_api_playback_motion_request_one_action",
    "PostApiPlaybackMotionRequestOneActionOne": ".post_api_playback_motion_request_one_action_one",
    "PostApiPlaybackMotionRequestOneActionThree": ".post_api_playback_motion_request_one_action_three",
    "PostApiPlaybackMotionRequestOneActionTwo": ".post_api_playback_motion_request_one_action_two",
    "PostApiPlaybackMotionRequestOneActionZero": ".post_api_playback_motion_request_one_action_zero",
    "PostApiPlaybackMotionRequestTime": ".post_api_playback_motion_request_time",
    "PostApiPlaybackMotionRequestTimeAction": ".post_api_playback_motion_request_time_action",
    "PostApiPlaybackMotionResponse": ".post_api_playback_motion_response",
    "PostApiPlaybackMotionResponsePlayback": ".post_api_playback_motion_response_playback",
    "PostApiPlaybackMotionResponsePlaybackDemo": ".post_api_playback_motion_response_playback_demo",
    "PostApiPlaybackMotionResponsePlaybackDemoMode": ".post_api_playback_motion_response_playback_demo_mode",
    "PostApiPlaybackMotionResponsePlaybackMotion": ".post_api_playback_motion_response_playback_motion",
    "PostApiPlaybackParametersResponse": ".post_api_playback_parameters_response",
    "PostApiPlaybackParametersResponsePlayback": ".post_api_playback_parameters_response_playback",
    "PostApiPlaybackParametersResponsePlaybackDemo": ".post_api_playback_parameters_response_playback_demo",
    "PostApiPlaybackParametersResponsePlaybackDemoMode": ".post_api_playback_parameters_response_playback_demo_mode",
    "PostApiPlaybackParametersResponsePlaybackMotion": ".post_api_playback_parameters_response_playback_motion",
    "PostApiPlaybackReloadResponse": ".post_api_playback_reload_response",
    "PostApiPlaybackReloadResponsePlayback": ".post_api_playback_reload_response_playback",
    "PostApiPlaybackReloadResponsePlaybackDemo": ".post_api_playback_reload_response_playback_demo",
    "PostApiPlaybackReloadResponsePlaybackDemoMode": ".post_api_playback_reload_response_playback_demo_mode",
    "PostApiPlaybackReloadResponsePlaybackMotion": ".post_api_playback_reload_response_playback_motion",
    "QaCheckRequest": ".qa_check_request",
    "QaCheckRequestMotionSweep": ".qa_check_request_motion_sweep",
    "QaCheckRequestMotionSweepCheckMonotonic": ".qa_check_request_motion_sweep_check_monotonic",
    "QaCheckRequestPoseSamplesItem": ".qa_check_request_pose_samples_item",
    "TransactionRequest": ".transaction_request",
    "TransactionRequestCheckpointId": ".transaction_request_checkpoint_id",
    "TransactionRequestCheckpointIdKind": ".transaction_request_checkpoint_id_kind",
    "TransactionRequestOperations": ".transaction_request_operations",
    "TransactionRequestOperationsOperationsItem": ".transaction_request_operations_operations_item",
    "TransactionRequestOperationsOperationsItemAction": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemActionArtmeshBindingKey": ".transaction_request_operations_operations_item_action_artmesh_binding_key",
    "TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyCurve": ".transaction_request_operations_operations_item_action_artmesh_binding_key_curve",
    "TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyCurveControlPointsItem": ".transaction_request_operations_operations_item_action_artmesh_binding_key_curve_control_points_item",
    "TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyInterpolation": ".transaction_request_operations_operations_item_action_artmesh_binding_key_interpolation",
    "TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyInterpolationFour": ".transaction_request_operations_operations_item_action_artmesh_binding_key_interpolation_four",
    "TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyInterpolationOne": ".transaction_request_operations_operations_item_action_artmesh_binding_key_interpolation_one",
    "TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyInterpolationThree": ".transaction_request_operations_operations_item_action_artmesh_binding_key_interpolation_three",
    "TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyInterpolationTwo": ".transaction_request_operations_operations_item_action_artmesh_binding_key_interpolation_two",
    "TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyInterpolationZero": ".transaction_request_operations_operations_item_action_artmesh_binding_key_interpolation_zero",
    "TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyOffsetsItem": ".transaction_request_operations_operations_item_action_artmesh_binding_key_offsets_item",
    "TransactionRequestOperationsOperationsItemActionArtmeshBlendShape": ".transaction_request_operations_operations_item_action_artmesh_blend_shape",
    "TransactionRequestOperationsOperationsItemActionArtmeshBlendShapeCurve": ".transaction_request_operations_operations_item_action_artmesh_blend_shape_curve",
    "TransactionRequestOperationsOperationsItemActionArtmeshBlendShapeCurveControlPointsItem": ".transaction_request_operations_operations_item_action_artmesh_blend_shape_curve_control_points_item",
    "TransactionRequestOperationsOperationsItemActionArtmeshBlendShapeInterpolation": ".transaction_request_operations_operations_item_action_artmesh_blend_shape_interpolation",
    "TransactionRequestOperationsOperationsItemActionArtmeshBlendShapeInterpolationFour": ".transaction_request_operations_operations_item_action_artmesh_blend_shape_interpolation_four",
    "TransactionRequestOperationsOperationsItemActionArtmeshBlendShapeInterpolationOne": ".transaction_request_operations_operations_item_action_artmesh_blend_shape_interpolation_one",
    "TransactionRequestOperationsOperationsItemActionArtmeshBlendShapeInterpolationThree": ".transaction_request_operations_operations_item_action_artmesh_blend_shape_interpolation_three",
    "TransactionRequestOperationsOperationsItemActionArtmeshBlendShapeInterpolationTwo": ".transaction_request_operations_operations_item_action_artmesh_blend_shape_interpolation_two",
    "TransactionRequestOperationsOperationsItemActionArtmeshBlendShapeInterpolationZero": ".transaction_request_operations_operations_item_action_artmesh_blend_shape_interpolation_zero",
    "TransactionRequestOperationsOperationsItemActionArtmeshBlendShapeOffsetsItem": ".transaction_request_operations_operations_item_action_artmesh_blend_shape_offsets_item",
    "TransactionRequestOperationsOperationsItemActionArtmeshGenerate": ".transaction_request_operations_operations_item_action_artmesh_generate",
    "TransactionRequestOperationsOperationsItemActionArtmeshGeneratePreset": ".transaction_request_operations_operations_item_action_artmesh_generate_preset",
    "TransactionRequestOperationsOperationsItemActionArtmeshGeneratePresetFive": ".transaction_request_operations_operations_item_action_artmesh_generate_preset_five",
    "TransactionRequestOperationsOperationsItemActionArtmeshGeneratePresetFour": ".transaction_request_operations_operations_item_action_artmesh_generate_preset_four",
    "TransactionRequestOperationsOperationsItemActionArtmeshGeneratePresetOne": ".transaction_request_operations_operations_item_action_artmesh_generate_preset_one",
    "TransactionRequestOperationsOperationsItemActionArtmeshGeneratePresetThree": ".transaction_request_operations_operations_item_action_artmesh_generate_preset_three",
    "TransactionRequestOperationsOperationsItemActionArtmeshGeneratePresetTwo": ".transaction_request_operations_operations_item_action_artmesh_generate_preset_two",
    "TransactionRequestOperationsOperationsItemActionArtmeshGeneratePresetZero": ".transaction_request_operations_operations_item_action_artmesh_generate_preset_zero",
    "TransactionRequestOperationsOperationsItemActionArtmeshGenerateQuality": ".transaction_request_operations_operations_item_action_artmesh_generate_quality",
    "TransactionRequestOperationsOperationsItemActionArtmeshGenerateTopology": ".transaction_request_operations_operations_item_action_artmesh_generate_topology",
    "TransactionRequestOperationsOperationsItemActionArtmeshGenerateTopologyOne": ".transaction_request_operations_operations_item_action_artmesh_generate_topology_one",
    "TransactionRequestOperationsOperationsItemActionArtmeshGenerateTopologyZero": ".transaction_request_operations_operations_item_action_artmesh_generate_topology_zero",
    "TransactionRequestOperationsOperationsItemActionArtmeshMirrorKey": ".transaction_request_operations_operations_item_action_artmesh_mirror_key",
    "TransactionRequestOperationsOperationsItemActionArtmeshMirrorKeyCurve": ".transaction_request_operations_operations_item_action_artmesh_mirror_key_curve",
    "TransactionRequestOperationsOperationsItemActionArtmeshMirrorKeyCurveControlPointsItem": ".transaction_request_operations_operations_item_action_artmesh_mirror_key_curve_control_points_item",
    "TransactionRequestOperationsOperationsItemActionArtmeshMirrorKeyInterpolation": ".transaction_request_operations_operations_item_action_artmesh_mirror_key_interpolation",
    "TransactionRequestOperationsOperationsItemActionArtmeshMirrorKeyInterpolationFour": ".transaction_request_operations_operations_item_action_artmesh_mirror_key_interpolation_four",
    "TransactionRequestOperationsOperationsItemActionArtmeshMirrorKeyInterpolationOne": ".transaction_request_operations_operations_item_action_artmesh_mirror_key_interpolation_one",
    "TransactionRequestOperationsOperationsItemActionArtmeshMirrorKeyInterpolationThree": ".transaction_request_operations_operations_item_action_artmesh_mirror_key_interpolation_three",
    "TransactionRequestOperationsOperationsItemActionArtmeshMirrorKeyInterpolationTwo": ".transaction_request_operations_operations_item_action_artmesh_mirror_key_interpolation_two",
    "TransactionRequestOperationsOperationsItemActionArtmeshMirrorKeyInterpolationZero": ".transaction_request_operations_operations_item_action_artmesh_mirror_key_interpolation_zero",
    "TransactionRequestOperationsOperationsItemActionArtmeshMultiKey": ".transaction_request_operations_operations_item_action_artmesh_multi_key",
    "TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyCurve": ".transaction_request_operations_operations_item_action_artmesh_multi_key_curve",
    "TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyCurveControlPointsItem": ".transaction_request_operations_operations_item_action_artmesh_multi_key_curve_control_points_item",
    "TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyInterpolation": ".transaction_request_operations_operations_item_action_artmesh_multi_key_interpolation",
    "TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyInterpolationFour": ".transaction_request_operations_operations_item_action_artmesh_multi_key_interpolation_four",
    "TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyInterpolationOne": ".transaction_request_operations_operations_item_action_artmesh_multi_key_interpolation_one",
    "TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyInterpolationThree": ".transaction_request_operations_operations_item_action_artmesh_multi_key_interpolation_three",
    "TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyInterpolationTwo": ".transaction_request_operations_operations_item_action_artmesh_multi_key_interpolation_two",
    "TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyInterpolationZero": ".transaction_request_operations_operations_item_action_artmesh_multi_key_interpolation_zero",
    "TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyOffsetsItem": ".transaction_request_operations_operations_item_action_artmesh_multi_key_offsets_item",
    "TransactionRequestOperationsOperationsItemActionArtmeshOffset": ".transaction_request_operations_operations_item_action_artmesh_offset",
    "TransactionRequestOperationsOperationsItemActionArtmeshOffsetUv": ".transaction_request_operations_operations_item_action_artmesh_offset_uv",
    "TransactionRequestOperationsOperationsItemActionArtmeshQuality": ".transaction_request_operations_operations_item_action_artmesh_quality",
    "TransactionRequestOperationsOperationsItemActionArtmeshQualityQuality": ".transaction_request_operations_operations_item_action_artmesh_quality_quality",
    "TransactionRequestOperationsOperationsItemActionArtmeshRebuild": ".transaction_request_operations_operations_item_action_artmesh_rebuild",
    "TransactionRequestOperationsOperationsItemActionArtmeshRebuildPreset": ".transaction_request_operations_operations_item_action_artmesh_rebuild_preset",
    "TransactionRequestOperationsOperationsItemActionArtmeshRebuildPresetFive": ".transaction_request_operations_operations_item_action_artmesh_rebuild_preset_five",
    "TransactionRequestOperationsOperationsItemActionArtmeshRebuildPresetFour": ".transaction_request_operations_operations_item_action_artmesh_rebuild_preset_four",
    "TransactionRequestOperationsOperationsItemActionArtmeshRebuildPresetOne": ".transaction_request_operations_operations_item_action_artmesh_rebuild_preset_one",
    "TransactionRequestOperationsOperationsItemActionArtmeshRebuildPresetThree": ".transaction_request_operations_operations_item_action_artmesh_rebuild_preset_three",
    "TransactionRequestOperationsOperationsItemActionArtmeshRebuildPresetTwo": ".transaction_request_operations_operations_item_action_artmesh_rebuild_preset_two",
    "TransactionRequestOperationsOperationsItemActionArtmeshRebuildPresetZero": ".transaction_request_operations_operations_item_action_artmesh_rebuild_preset_zero",
    "TransactionRequestOperationsOperationsItemActionArtmeshRebuildQuality": ".transaction_request_operations_operations_item_action_artmesh_rebuild_quality",
    "TransactionRequestOperationsOperationsItemActionArtmeshRebuildTopology": ".transaction_request_operations_operations_item_action_artmesh_rebuild_topology",
    "TransactionRequestOperationsOperationsItemActionArtmeshRebuildTopologyOne": ".transaction_request_operations_operations_item_action_artmesh_rebuild_topology_one",
    "TransactionRequestOperationsOperationsItemActionArtmeshRebuildTopologyZero": ".transaction_request_operations_operations_item_action_artmesh_rebuild_topology_zero",
    "TransactionRequestOperationsOperationsItemActionBindingKey": ".transaction_request_operations_operations_item_action_binding_key",
    "TransactionRequestOperationsOperationsItemActionBindingKeyCurve": ".transaction_request_operations_operations_item_action_binding_key_curve",
    "TransactionRequestOperationsOperationsItemActionBindingKeyCurveControlPointsItem": ".transaction_request_operations_operations_item_action_binding_key_curve_control_points_item",
    "TransactionRequestOperationsOperationsItemActionBindingKeyInterpolation": ".transaction_request_operations_operations_item_action_binding_key_interpolation",
    "TransactionRequestOperationsOperationsItemActionBindingKeyInterpolationFour": ".transaction_request_operations_operations_item_action_binding_key_interpolation_four",
    "TransactionRequestOperationsOperationsItemActionBindingKeyInterpolationOne": ".transaction_request_operations_operations_item_action_binding_key_interpolation_one",
    "TransactionRequestOperationsOperationsItemActionBindingKeyInterpolationThree": ".transaction_request_operations_operations_item_action_binding_key_interpolation_three",
    "TransactionRequestOperationsOperationsItemActionBindingKeyInterpolationTwo": ".transaction_request_operations_operations_item_action_binding_key_interpolation_two",
    "TransactionRequestOperationsOperationsItemActionBindingKeyInterpolationZero": ".transaction_request_operations_operations_item_action_binding_key_interpolation_zero",
    "TransactionRequestOperationsOperationsItemActionBindingKeyProperty": ".transaction_request_operations_operations_item_action_binding_key_property",
    "TransactionRequestOperationsOperationsItemActionBindingKeyPropertyFive": ".transaction_request_operations_operations_item_action_binding_key_property_five",
    "TransactionRequestOperationsOperationsItemActionBindingKeyPropertyFour": ".transaction_request_operations_operations_item_action_binding_key_property_four",
    "TransactionRequestOperationsOperationsItemActionBindingKeyPropertyOne": ".transaction_request_operations_operations_item_action_binding_key_property_one",
    "TransactionRequestOperationsOperationsItemActionBindingKeyPropertyThree": ".transaction_request_operations_operations_item_action_binding_key_property_three",
    "TransactionRequestOperationsOperationsItemActionBindingKeyPropertyTwo": ".transaction_request_operations_operations_item_action_binding_key_property_two",
    "TransactionRequestOperationsOperationsItemActionBindingKeyPropertyZero": ".transaction_request_operations_operations_item_action_binding_key_property_zero",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSet": ".transaction_request_operations_operations_item_action_blend_shape_set",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShape": ".transaction_request_operations_operations_item_action_blend_shape_set_shape",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPath": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_art_path",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathCurve": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_art_path_curve",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathCurveControlPointsItem": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_art_path_curve_control_points_item",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathInterpolation": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_art_path_interpolation",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathInterpolationFour": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_art_path_interpolation_four",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathInterpolationOne": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_art_path_interpolation_one",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathInterpolationThree": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_art_path_interpolation_three",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathInterpolationTwo": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_art_path_interpolation_two",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathInterpolationZero": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_art_path_interpolation_zero",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathPointsItem": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_art_path_points_item",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformer": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerCurve": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_curve",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerCurveControlPointsItem": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_curve_control_points_item",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerInterpolation": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_interpolation",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerInterpolationFour": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_interpolation_four",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerInterpolationOne": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_interpolation_one",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerInterpolationThree": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_interpolation_three",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerInterpolationTwo": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_interpolation_two",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerInterpolationZero": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_interpolation_zero",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerPinsItem": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_pins_item",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerSharedPointsItem": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_shared_points_item",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerTransform": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_transform",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerWarp": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_warp",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeGlue": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_glue",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeGlueCurve": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_glue_curve",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeGlueCurveControlPointsItem": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_glue_curve_control_points_item",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeGlueInterpolation": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_glue_interpolation",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeGlueInterpolationFour": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_glue_interpolation_four",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeGlueInterpolationOne": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_glue_interpolation_one",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeGlueInterpolationThree": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_glue_interpolation_three",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeGlueInterpolationTwo": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_glue_interpolation_two",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeGlueInterpolationZero": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_glue_interpolation_zero",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePart": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_part",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartCurve": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_part_curve",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartCurveControlPointsItem": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_part_curve_control_points_item",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartInterpolation": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_part_interpolation",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartInterpolationFour": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_part_interpolation_four",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartInterpolationOne": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_part_interpolation_one",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartInterpolationThree": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_part_interpolation_three",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartInterpolationTwo": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_part_interpolation_two",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartInterpolationZero": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_part_interpolation_zero",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartTransform": ".transaction_request_operations_operations_item_action_blend_shape_set_shape_part_transform",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShape_ArtPath": ".transaction_request_operations_operations_item_action_blend_shape_set_shape",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShape_Deformer": ".transaction_request_operations_operations_item_action_blend_shape_set_shape",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShape_Glue": ".transaction_request_operations_operations_item_action_blend_shape_set_shape",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShape_Part": ".transaction_request_operations_operations_item_action_blend_shape_set_shape",
    "TransactionRequestOperationsOperationsItemActionDeformBrush": ".transaction_request_operations_operations_item_action_deform_brush",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrush": ".transaction_request_operations_operations_item_action_deform_brush_brush",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestination": ".transaction_request_operations_operations_item_action_deform_brush_brush_destination",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBase": ".transaction_request_operations_operations_item_action_deform_brush_brush_destination_base",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShape": ".transaction_request_operations_operations_item_action_deform_brush_brush_destination_blend_shape",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShapeShape": ".transaction_request_operations_operations_item_action_deform_brush_brush_destination_blend_shape_shape",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShapeShapeCurve": ".transaction_request_operations_operations_item_action_deform_brush_brush_destination_blend_shape_shape_curve",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShapeShapeCurveControlPointsItem": ".transaction_request_operations_operations_item_action_deform_brush_brush_destination_blend_shape_shape_curve_control_points_item",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShapeShapeInterpolation": ".transaction_request_operations_operations_item_action_deform_brush_brush_destination_blend_shape_shape_interpolation",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShapeShapeInterpolationFour": ".transaction_request_operations_operations_item_action_deform_brush_brush_destination_blend_shape_shape_interpolation_four",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShapeShapeInterpolationOne": ".transaction_request_operations_operations_item_action_deform_brush_brush_destination_blend_shape_shape_interpolation_one",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShapeShapeInterpolationThree": ".transaction_request_operations_operations_item_action_deform_brush_brush_destination_blend_shape_shape_interpolation_three",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShapeShapeInterpolationTwo": ".transaction_request_operations_operations_item_action_deform_brush_brush_destination_blend_shape_shape_interpolation_two",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShapeShapeInterpolationZero": ".transaction_request_operations_operations_item_action_deform_brush_brush_destination_blend_shape_shape_interpolation_zero",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationKeyform": ".transaction_request_operations_operations_item_action_deform_brush_brush_destination_keyform",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestination_Base": ".transaction_request_operations_operations_item_action_deform_brush_brush_destination",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestination_BlendShape": ".transaction_request_operations_operations_item_action_deform_brush_brush_destination",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestination_Keyform": ".transaction_request_operations_operations_item_action_deform_brush_brush_destination",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffect": ".transaction_request_operations_operations_item_action_deform_brush_brush_effect",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffectBend": ".transaction_request_operations_operations_item_action_deform_brush_brush_effect_bend",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffectContourFollow": ".transaction_request_operations_operations_item_action_deform_brush_brush_effect_contour_follow",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffectInflate": ".transaction_request_operations_operations_item_action_deform_brush_brush_effect_inflate",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffectPinch": ".transaction_request_operations_operations_item_action_deform_brush_brush_effect_pinch",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffectRelax": ".transaction_request_operations_operations_item_action_deform_brush_brush_effect_relax",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffectSmooth": ".transaction_request_operations_operations_item_action_deform_brush_brush_effect_smooth",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffect_Bend": ".transaction_request_operations_operations_item_action_deform_brush_brush_effect",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffect_ContourFollow": ".transaction_request_operations_operations_item_action_deform_brush_brush_effect",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffect_Inflate": ".transaction_request_operations_operations_item_action_deform_brush_brush_effect",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffect_Pinch": ".transaction_request_operations_operations_item_action_deform_brush_brush_effect",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffect_Relax": ".transaction_request_operations_operations_item_action_deform_brush_brush_effect",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffect_Smooth": ".transaction_request_operations_operations_item_action_deform_brush_brush_effect",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushFalloff": ".transaction_request_operations_operations_item_action_deform_brush_brush_falloff",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushFalloffOne": ".transaction_request_operations_operations_item_action_deform_brush_brush_falloff_one",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushFalloffZero": ".transaction_request_operations_operations_item_action_deform_brush_brush_falloff_zero",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurface": ".transaction_request_operations_operations_item_action_deform_brush_brush_surface",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurfaceArtmesh": ".transaction_request_operations_operations_item_action_deform_brush_brush_surface_artmesh",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurfaceArtmeshSpace": ".transaction_request_operations_operations_item_action_deform_brush_brush_surface_artmesh_space",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurfaceSharedWarp": ".transaction_request_operations_operations_item_action_deform_brush_brush_surface_shared_warp",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurfaceSharedWarpSpace": ".transaction_request_operations_operations_item_action_deform_brush_brush_surface_shared_warp_space",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurfaceWarpPins": ".transaction_request_operations_operations_item_action_deform_brush_brush_surface_warp_pins",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurfaceWarpPinsSpace": ".transaction_request_operations_operations_item_action_deform_brush_brush_surface_warp_pins_space",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurface_Artmesh": ".transaction_request_operations_operations_item_action_deform_brush_brush_surface",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurface_SharedWarp": ".transaction_request_operations_operations_item_action_deform_brush_brush_surface",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurface_WarpPins": ".transaction_request_operations_operations_item_action_deform_brush_brush_surface",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKey": ".transaction_request_operations_operations_item_action_deformer_binding_key",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyCurve": ".transaction_request_operations_operations_item_action_deformer_binding_key_curve",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyCurveControlPointsItem": ".transaction_request_operations_operations_item_action_deformer_binding_key_curve_control_points_item",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyInterpolation": ".transaction_request_operations_operations_item_action_deformer_binding_key_interpolation",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyInterpolationFour": ".transaction_request_operations_operations_item_action_deformer_binding_key_interpolation_four",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyInterpolationOne": ".transaction_request_operations_operations_item_action_deformer_binding_key_interpolation_one",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyInterpolationThree": ".transaction_request_operations_operations_item_action_deformer_binding_key_interpolation_three",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyInterpolationTwo": ".transaction_request_operations_operations_item_action_deformer_binding_key_interpolation_two",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyInterpolationZero": ".transaction_request_operations_operations_item_action_deformer_binding_key_interpolation_zero",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyProperty": ".transaction_request_operations_operations_item_action_deformer_binding_key_property",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertyEight": ".transaction_request_operations_operations_item_action_deformer_binding_key_property_eight",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertyFive": ".transaction_request_operations_operations_item_action_deformer_binding_key_property_five",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertyFour": ".transaction_request_operations_operations_item_action_deformer_binding_key_property_four",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertyNine": ".transaction_request_operations_operations_item_action_deformer_binding_key_property_nine",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertyOne": ".transaction_request_operations_operations_item_action_deformer_binding_key_property_one",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertySeven": ".transaction_request_operations_operations_item_action_deformer_binding_key_property_seven",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertySix": ".transaction_request_operations_operations_item_action_deformer_binding_key_property_six",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertyThree": ".transaction_request_operations_operations_item_action_deformer_binding_key_property_three",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertyTwo": ".transaction_request_operations_operations_item_action_deformer_binding_key_property_two",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertyZero": ".transaction_request_operations_operations_item_action_deformer_binding_key_property_zero",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingRemove": ".transaction_request_operations_operations_item_action_deformer_binding_remove",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingRemoveProperty": ".transaction_request_operations_operations_item_action_deformer_binding_remove_property",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingRemovePropertyEight": ".transaction_request_operations_operations_item_action_deformer_binding_remove_property_eight",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingRemovePropertyFive": ".transaction_request_operations_operations_item_action_deformer_binding_remove_property_five",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingRemovePropertyFour": ".transaction_request_operations_operations_item_action_deformer_binding_remove_property_four",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingRemovePropertyNine": ".transaction_request_operations_operations_item_action_deformer_binding_remove_property_nine",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingRemovePropertyOne": ".transaction_request_operations_operations_item_action_deformer_binding_remove_property_one",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingRemovePropertySeven": ".transaction_request_operations_operations_item_action_deformer_binding_remove_property_seven",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingRemovePropertySix": ".transaction_request_operations_operations_item_action_deformer_binding_remove_property_six",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingRemovePropertyThree": ".transaction_request_operations_operations_item_action_deformer_binding_remove_property_three",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingRemovePropertyTwo": ".transaction_request_operations_operations_item_action_deformer_binding_remove_property_two",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingRemovePropertyZero": ".transaction_request_operations_operations_item_action_deformer_binding_remove_property_zero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreate": ".transaction_request_operations_operations_item_action_deformer_create",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformer": ".transaction_request_operations_operations_item_action_deformer_create_deformer",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItem": ".transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemComposition": ".transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_composition",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemCompositionOne": ".transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_composition_one",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemCompositionZero": ".transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_composition_zero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemCurve": ".transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_curve",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemCurveControlPointsItem": ".transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_curve_control_points_item",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemInterpolation": ".transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_interpolation",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemInterpolationFour": ".transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_interpolation_four",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemInterpolationOne": ".transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_interpolation_one",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemInterpolationThree": ".transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_interpolation_three",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemInterpolationTwo": ".transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_interpolation_two",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemInterpolationZero": ".transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_interpolation_zero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemKeysItem": ".transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_keys_item",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemProperty": ".transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_property",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemPropertyEight": ".transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_property_eight",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemPropertyFive": ".transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_property_five",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemPropertyFour": ".transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_property_four",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemPropertyNine": ".transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_property_nine",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemPropertyOne": ".transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_property_one",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemPropertySeven": ".transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_property_seven",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemPropertySix": ".transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_property_six",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemPropertyThree": ".transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_property_three",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemPropertyTwo": ".transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_property_two",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemPropertyZero": ".transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item_property_zero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItem": ".transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemCurve": ".transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item_curve",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemCurveControlPointsItem": ".transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item_curve_control_points_item",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemInterpolation": ".transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item_interpolation",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemInterpolationFour": ".transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item_interpolation_four",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemInterpolationOne": ".transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item_interpolation_one",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemInterpolationThree": ".transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item_interpolation_three",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemInterpolationTwo": ".transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item_interpolation_two",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemInterpolationZero": ".transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item_interpolation_zero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemKind": ".transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item_kind",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemPinsItem": ".transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item_pins_item",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemSharedPointsItem": ".transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item_shared_points_item",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemTransform": ".transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item_transform",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemWarp": ".transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item_warp",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerKind": ".transaction_request_operations_operations_item_action_deformer_create_deformer_kind",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerKindOne": ".transaction_request_operations_operations_item_action_deformer_create_deformer_kind_one",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerKindTwo": ".transaction_request_operations_operations_item_action_deformer_create_deformer_kind_two",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerKindZero": ".transaction_request_operations_operations_item_action_deformer_create_deformer_kind_zero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItem": ".transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemComposition": ".transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_composition",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemCompositionOne": ".transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_composition_one",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemCompositionZero": ".transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_composition_zero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemCurve": ".transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_curve",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemCurveControlPointsItem": ".transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_curve_control_points_item",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemInterpolation": ".transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_interpolation",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemInterpolationFour": ".transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_interpolation_four",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemInterpolationOne": ".transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_interpolation_one",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemInterpolationThree": ".transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_interpolation_three",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemInterpolationTwo": ".transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_interpolation_two",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemInterpolationZero": ".transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_interpolation_zero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemKeyformsItem": ".transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_keyforms_item",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemProperty": ".transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_property",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertyEight": ".transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_property_eight",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertyEleven": ".transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_property_eleven",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertyFive": ".transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_property_five",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertyFour": ".transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_property_four",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertyNine": ".transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_property_nine",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertyOne": ".transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_property_one",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertySeven": ".transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_property_seven",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertySix": ".transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_property_six",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertyTen": ".transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_property_ten",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertyThree": ".transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_property_three",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertyTwo": ".transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_property_two",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertyZero": ".transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item_property_zero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerOrigin": ".transaction_request_operations_operations_item_action_deformer_create_deformer_origin",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadata": ".transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataAngleRange": ".transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata_angle_range",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataAngleUnit": ".transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata_angle_unit",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataParentComposition": ".transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata_parent_composition",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataParentCompositionOne": ".transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata_parent_composition_one",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataParentCompositionZero": ".transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata_parent_composition_zero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataPivot": ".transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata_pivot",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataPivotSpace": ".transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata_pivot_space",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataPivotSpaceOne": ".transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata_pivot_space_one",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataPivotSpaceZero": ".transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata_pivot_space_zero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataShapePreservation": ".transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata_shape_preservation",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataShapePreservationOne": ".transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata_shape_preservation_one",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataShapePreservationTwo": ".transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata_shape_preservation_two",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataShapePreservationZero": ".transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata_shape_preservation_zero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarp": ".transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpBounds": ".transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_bounds",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItem": ".transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_control_points_item",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItem": ".transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemCurve": ".transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_curve",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemCurveControlPointsItem": ".transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_curve_control_points_item",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolation": ".transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_interpolation",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolationFour": ".transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_interpolation_four",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolationOne": ".transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_interpolation_one",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolationThree": ".transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_interpolation_three",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolationTwo": ".transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_interpolation_two",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolationZero": ".transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_interpolation_zero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemKeysItem": ".transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_keys_item",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemProperty": ".transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_property",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemPropertyOne": ".transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_property_one",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemPropertyZero": ".transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_property_zero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpGrid": ".transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp_grid",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerTransform": ".transaction_request_operations_operations_item_action_deformer_create_deformer_transform",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarp": ".transaction_request_operations_operations_item_action_deformer_create_deformer_warp",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpGrid": ".transaction_request_operations_operations_item_action_deformer_create_deformer_warp_grid",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinBlendMode": ".transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pin_blend_mode",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinBlendModeOne": ".transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pin_blend_mode_one",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinBlendModeZero": ".transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pin_blend_mode_zero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItem": ".transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItem": ".transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_bindings_item",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemCurve": ".transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_bindings_item_curve",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemCurveControlPointsItem": ".transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_bindings_item_curve_control_points_item",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolation": ".transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_bindings_item_interpolation",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolationFour": ".transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_bindings_item_interpolation_four",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolationOne": ".transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_bindings_item_interpolation_one",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolationThree": ".transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_bindings_item_interpolation_three",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolationTwo": ".transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_bindings_item_interpolation_two",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolationZero": ".transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_bindings_item_interpolation_zero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemKeysItem": ".transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_bindings_item_keys_item",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemProperty": ".transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_bindings_item_property",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemPropertyOne": ".transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_bindings_item_property_one",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemPropertyZero": ".transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_bindings_item_property_zero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItem": ".transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_multi_bindings_item",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemCurve": ".transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_curve",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemCurveControlPointsItem": ".transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_curve_control_points_item",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolation": ".transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_interpolation",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolationFour": ".transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_interpolation_four",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolationOne": ".transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_interpolation_one",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolationThree": ".transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_interpolation_three",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolationTwo": ".transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_interpolation_two",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolationZero": ".transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_interpolation_zero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemKeyformsItem": ".transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_keyforms_item",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemProperty": ".transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_property",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemPropertyOne": ".transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_property_one",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemPropertyZero": ".transaction_request_operations_operations_item_action_deformer_create_deformer_warp_pins_item_multi_bindings_item_property_zero",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSet": ".transaction_request_operations_operations_item_action_deformer_kind_set",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetKind": ".transaction_request_operations_operations_item_action_deformer_kind_set_kind",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetKindOne": ".transaction_request_operations_operations_item_action_deformer_kind_set_kind_one",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetKindTwo": ".transaction_request_operations_operations_item_action_deformer_kind_set_kind_two",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetKindZero": ".transaction_request_operations_operations_item_action_deformer_kind_set_kind_zero",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarp": ".transaction_request_operations_operations_item_action_deformer_kind_set_warp",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpGrid": ".transaction_request_operations_operations_item_action_deformer_kind_set_warp_grid",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinBlendMode": ".transaction_request_operations_operations_item_action_deformer_kind_set_warp_pin_blend_mode",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinBlendModeOne": ".transaction_request_operations_operations_item_action_deformer_kind_set_warp_pin_blend_mode_one",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinBlendModeZero": ".transaction_request_operations_operations_item_action_deformer_kind_set_warp_pin_blend_mode_zero",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItem": ".transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItem": ".transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_bindings_item",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemCurve": ".transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_bindings_item_curve",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemCurveControlPointsItem": ".transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_bindings_item_curve_control_points_item",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemInterpolation": ".transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_bindings_item_interpolation",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemInterpolationFour": ".transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_bindings_item_interpolation_four",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemInterpolationOne": ".transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_bindings_item_interpolation_one",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemInterpolationThree": ".transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_bindings_item_interpolation_three",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemInterpolationTwo": ".transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_bindings_item_interpolation_two",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemInterpolationZero": ".transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_bindings_item_interpolation_zero",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemKeysItem": ".transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_bindings_item_keys_item",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemProperty": ".transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_bindings_item_property",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemPropertyOne": ".transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_bindings_item_property_one",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemPropertyZero": ".transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_bindings_item_property_zero",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItem": ".transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_multi_bindings_item",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemCurve": ".transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_multi_bindings_item_curve",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemCurveControlPointsItem": ".transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_multi_bindings_item_curve_control_points_item",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolation": ".transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_multi_bindings_item_interpolation",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolationFour": ".transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_multi_bindings_item_interpolation_four",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolationOne": ".transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_multi_bindings_item_interpolation_one",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolationThree": ".transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_multi_bindings_item_interpolation_three",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolationTwo": ".transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_multi_bindings_item_interpolation_two",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolationZero": ".transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_multi_bindings_item_interpolation_zero",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemKeyformsItem": ".transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_multi_bindings_item_keyforms_item",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemProperty": ".transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_multi_bindings_item_property",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemPropertyOne": ".transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_multi_bindings_item_property_one",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemPropertyZero": ".transaction_request_operations_operations_item_action_deformer_kind_set_warp_pins_item_multi_bindings_item_property_zero",
    "TransactionRequestOperationsOperationsItemActionDeformerOrigin": ".transaction_request_operations_operations_item_action_deformer_origin",
    "TransactionRequestOperationsOperationsItemActionDeformerParentSet": ".transaction_request_operations_operations_item_action_deformer_parent_set",
    "TransactionRequestOperationsOperationsItemActionDeformerRotationMetadata": ".transaction_request_operations_operations_item_action_deformer_rotation_metadata",
    "TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadata": ".transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata",
    "TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataAngleRange": ".transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata_angle_range",
    "TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataAngleUnit": ".transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata_angle_unit",
    "TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataParentComposition": ".transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata_parent_composition",
    "TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataParentCompositionOne": ".transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata_parent_composition_one",
    "TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataParentCompositionZero": ".transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata_parent_composition_zero",
    "TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataPivot": ".transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata_pivot",
    "TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataPivotSpace": ".transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata_pivot_space",
    "TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataPivotSpaceOne": ".transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata_pivot_space_one",
    "TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataPivotSpaceZero": ".transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata_pivot_space_zero",
    "TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataShapePreservation": ".transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata_shape_preservation",
    "TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataShapePreservationOne": ".transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata_shape_preservation_one",
    "TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataShapePreservationTwo": ".transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata_shape_preservation_two",
    "TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataShapePreservationZero": ".transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata_shape_preservation_zero",
    "TransactionRequestOperationsOperationsItemActionDeformerSplit": ".transaction_request_operations_operations_item_action_deformer_split",
    "TransactionRequestOperationsOperationsItemActionDeformerTargetsSet": ".transaction_request_operations_operations_item_action_deformer_targets_set",
    "TransactionRequestOperationsOperationsItemActionDeformerTargetsSetMode": ".transaction_request_operations_operations_item_action_deformer_targets_set_mode",
    "TransactionRequestOperationsOperationsItemActionDeformerTargetsSetModeOne": ".transaction_request_operations_operations_item_action_deformer_targets_set_mode_one",
    "TransactionRequestOperationsOperationsItemActionDeformerTargetsSetModeZero": ".transaction_request_operations_operations_item_action_deformer_targets_set_mode_zero",
    "TransactionRequestOperationsOperationsItemActionDeformerTransform": ".transaction_request_operations_operations_item_action_deformer_transform",
    "TransactionRequestOperationsOperationsItemActionDeformerTransformOperator": ".transaction_request_operations_operations_item_action_deformer_transform_operator",
    "TransactionRequestOperationsOperationsItemActionDeformerTransformOperatorOne": ".transaction_request_operations_operations_item_action_deformer_transform_operator_one",
    "TransactionRequestOperationsOperationsItemActionDeformerTransformOperatorTwo": ".transaction_request_operations_operations_item_action_deformer_transform_operator_two",
    "TransactionRequestOperationsOperationsItemActionDeformerTransformOperatorZero": ".transaction_request_operations_operations_item_action_deformer_transform_operator_zero",
    "TransactionRequestOperationsOperationsItemActionDeformerTransformProperty": ".transaction_request_operations_operations_item_action_deformer_transform_property",
    "TransactionRequestOperationsOperationsItemActionDeformerTransformPropertyFive": ".transaction_request_operations_operations_item_action_deformer_transform_property_five",
    "TransactionRequestOperationsOperationsItemActionDeformerTransformPropertyFour": ".transaction_request_operations_operations_item_action_deformer_transform_property_four",
    "TransactionRequestOperationsOperationsItemActionDeformerTransformPropertyOne": ".transaction_request_operations_operations_item_action_deformer_transform_property_one",
    "TransactionRequestOperationsOperationsItemActionDeformerTransformPropertyThree": ".transaction_request_operations_operations_item_action_deformer_transform_property_three",
    "TransactionRequestOperationsOperationsItemActionDeformerTransformPropertyTwo": ".transaction_request_operations_operations_item_action_deformer_transform_property_two",
    "TransactionRequestOperationsOperationsItemActionDeformerTransformPropertyZero": ".transaction_request_operations_operations_item_action_deformer_transform_property_zero",
    "TransactionRequestOperationsOperationsItemActionParameterAdd": ".transaction_request_operations_operations_item_action_parameter_add",
    "TransactionRequestOperationsOperationsItemActionParameterAddParameter": ".transaction_request_operations_operations_item_action_parameter_add_parameter",
    "TransactionRequestOperationsOperationsItemActionPartAlphaReveal": ".transaction_request_operations_operations_item_action_part_alpha_reveal",
    "TransactionRequestOperationsOperationsItemActionPartAlphaRevealReveal": ".transaction_request_operations_operations_item_action_part_alpha_reveal_reveal",
    "TransactionRequestOperationsOperationsItemActionPartBlendMode": ".transaction_request_operations_operations_item_action_part_blend_mode",
    "TransactionRequestOperationsOperationsItemActionPartBlendModeMode": ".transaction_request_operations_operations_item_action_part_blend_mode_mode",
    "TransactionRequestOperationsOperationsItemActionPartBlendModeModeOne": ".transaction_request_operations_operations_item_action_part_blend_mode_mode_one",
    "TransactionRequestOperationsOperationsItemActionPartBlendModeModeThree": ".transaction_request_operations_operations_item_action_part_blend_mode_mode_three",
    "TransactionRequestOperationsOperationsItemActionPartBlendModeModeTwo": ".transaction_request_operations_operations_item_action_part_blend_mode_mode_two",
    "TransactionRequestOperationsOperationsItemActionPartBlendModeModeZero": ".transaction_request_operations_operations_item_action_part_blend_mode_mode_zero",
    "TransactionRequestOperationsOperationsItemActionPartClip": ".transaction_request_operations_operations_item_action_part_clip",
    "TransactionRequestOperationsOperationsItemActionPartClipClip": ".transaction_request_operations_operations_item_action_part_clip_clip",
    "TransactionRequestOperationsOperationsItemActionPartClipClipMaskOpacity": ".transaction_request_operations_operations_item_action_part_clip_clip_mask_opacity",
    "TransactionRequestOperationsOperationsItemActionPartClipClipMaskOpacityOne": ".transaction_request_operations_operations_item_action_part_clip_clip_mask_opacity_one",
    "TransactionRequestOperationsOperationsItemActionPartClipClipMaskOpacityZero": ".transaction_request_operations_operations_item_action_part_clip_clip_mask_opacity_zero",
    "TransactionRequestOperationsOperationsItemActionPartClipClipMode": ".transaction_request_operations_operations_item_action_part_clip_clip_mode",
    "TransactionRequestOperationsOperationsItemActionPartContourShade": ".transaction_request_operations_operations_item_action_part_contour_shade",
    "TransactionRequestOperationsOperationsItemActionPartContourShadeShade": ".transaction_request_operations_operations_item_action_part_contour_shade_shade",
    "TransactionRequestOperationsOperationsItemActionPartContourShadeShadeProfile": ".transaction_request_operations_operations_item_action_part_contour_shade_shade_profile",
    "TransactionRequestOperationsOperationsItemActionPartDrawOrder": ".transaction_request_operations_operations_item_action_part_draw_order",
    "TransactionRequestOperationsOperationsItemActionPartTint": ".transaction_request_operations_operations_item_action_part_tint",
    "TransactionRequestOperationsOperationsItemActionPartTintTint": ".transaction_request_operations_operations_item_action_part_tint_tint",
    "TransactionRequestOperationsOperationsItemActionPartTintTintMode": ".transaction_request_operations_operations_item_action_part_tint_tint_mode",
    "TransactionRequestOperationsOperationsItemActionPartTintTintModeOne": ".transaction_request_operations_operations_item_action_part_tint_tint_mode_one",
    "TransactionRequestOperationsOperationsItemActionPartTintTintModeZero": ".transaction_request_operations_operations_item_action_part_tint_tint_mode_zero",
    "TransactionRequestOperationsOperationsItemActionPartVisibility": ".transaction_request_operations_operations_item_action_part_visibility",
    "TransactionRequestOperationsOperationsItemActionRoleConfirm": ".transaction_request_operations_operations_item_action_role_confirm",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRole": ".transaction_request_operations_operations_item_action_role_confirm_role",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleEight": ".transaction_request_operations_operations_item_action_role_confirm_role_eight",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleEleven": ".transaction_request_operations_operations_item_action_role_confirm_role_eleven",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleFifteen": ".transaction_request_operations_operations_item_action_role_confirm_role_fifteen",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleFive": ".transaction_request_operations_operations_item_action_role_confirm_role_five",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleFour": ".transaction_request_operations_operations_item_action_role_confirm_role_four",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleFourteen": ".transaction_request_operations_operations_item_action_role_confirm_role_fourteen",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleNine": ".transaction_request_operations_operations_item_action_role_confirm_role_nine",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleOne": ".transaction_request_operations_operations_item_action_role_confirm_role_one",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleSeven": ".transaction_request_operations_operations_item_action_role_confirm_role_seven",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleSeventeen": ".transaction_request_operations_operations_item_action_role_confirm_role_seventeen",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleSix": ".transaction_request_operations_operations_item_action_role_confirm_role_six",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleSixteen": ".transaction_request_operations_operations_item_action_role_confirm_role_sixteen",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleTen": ".transaction_request_operations_operations_item_action_role_confirm_role_ten",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleThirteen": ".transaction_request_operations_operations_item_action_role_confirm_role_thirteen",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleThree": ".transaction_request_operations_operations_item_action_role_confirm_role_three",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleTwelve": ".transaction_request_operations_operations_item_action_role_confirm_role_twelve",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleTwo": ".transaction_request_operations_operations_item_action_role_confirm_role_two",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleZero": ".transaction_request_operations_operations_item_action_role_confirm_role_zero",
    "TransactionRequestOperationsOperationsItemActionRoleReclassify": ".transaction_request_operations_operations_item_action_role_reclassify",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRole": ".transaction_request_operations_operations_item_action_role_reclassify_expected_role",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleEight": ".transaction_request_operations_operations_item_action_role_reclassify_expected_role_eight",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleEleven": ".transaction_request_operations_operations_item_action_role_reclassify_expected_role_eleven",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleFifteen": ".transaction_request_operations_operations_item_action_role_reclassify_expected_role_fifteen",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleFive": ".transaction_request_operations_operations_item_action_role_reclassify_expected_role_five",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleFour": ".transaction_request_operations_operations_item_action_role_reclassify_expected_role_four",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleFourteen": ".transaction_request_operations_operations_item_action_role_reclassify_expected_role_fourteen",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleNine": ".transaction_request_operations_operations_item_action_role_reclassify_expected_role_nine",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleOne": ".transaction_request_operations_operations_item_action_role_reclassify_expected_role_one",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleSeven": ".transaction_request_operations_operations_item_action_role_reclassify_expected_role_seven",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleSeventeen": ".transaction_request_operations_operations_item_action_role_reclassify_expected_role_seventeen",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleSix": ".transaction_request_operations_operations_item_action_role_reclassify_expected_role_six",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleSixteen": ".transaction_request_operations_operations_item_action_role_reclassify_expected_role_sixteen",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleTen": ".transaction_request_operations_operations_item_action_role_reclassify_expected_role_ten",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleThirteen": ".transaction_request_operations_operations_item_action_role_reclassify_expected_role_thirteen",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleThree": ".transaction_request_operations_operations_item_action_role_reclassify_expected_role_three",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleTwelve": ".transaction_request_operations_operations_item_action_role_reclassify_expected_role_twelve",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleTwo": ".transaction_request_operations_operations_item_action_role_reclassify_expected_role_two",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleZero": ".transaction_request_operations_operations_item_action_role_reclassify_expected_role_zero",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRole": ".transaction_request_operations_operations_item_action_role_reclassify_role",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleEight": ".transaction_request_operations_operations_item_action_role_reclassify_role_eight",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleEleven": ".transaction_request_operations_operations_item_action_role_reclassify_role_eleven",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleFifteen": ".transaction_request_operations_operations_item_action_role_reclassify_role_fifteen",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleFive": ".transaction_request_operations_operations_item_action_role_reclassify_role_five",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleFour": ".transaction_request_operations_operations_item_action_role_reclassify_role_four",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleFourteen": ".transaction_request_operations_operations_item_action_role_reclassify_role_fourteen",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleNine": ".transaction_request_operations_operations_item_action_role_reclassify_role_nine",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleOne": ".transaction_request_operations_operations_item_action_role_reclassify_role_one",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleSeven": ".transaction_request_operations_operations_item_action_role_reclassify_role_seven",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleSeventeen": ".transaction_request_operations_operations_item_action_role_reclassify_role_seventeen",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleSix": ".transaction_request_operations_operations_item_action_role_reclassify_role_six",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleSixteen": ".transaction_request_operations_operations_item_action_role_reclassify_role_sixteen",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleTen": ".transaction_request_operations_operations_item_action_role_reclassify_role_ten",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleThirteen": ".transaction_request_operations_operations_item_action_role_reclassify_role_thirteen",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleThree": ".transaction_request_operations_operations_item_action_role_reclassify_role_three",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleTwelve": ".transaction_request_operations_operations_item_action_role_reclassify_role_twelve",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleTwo": ".transaction_request_operations_operations_item_action_role_reclassify_role_two",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleZero": ".transaction_request_operations_operations_item_action_role_reclassify_role_zero",
    "TransactionRequestOperationsOperationsItemActionSymmetryArtmeshBindings": ".transaction_request_operations_operations_item_action_symmetry_artmesh_bindings",
    "TransactionRequestOperationsOperationsItemActionSymmetryArtmeshBindingsLinksItem": ".transaction_request_operations_operations_item_action_symmetry_artmesh_bindings_links_item",
    "TransactionRequestOperationsOperationsItemActionSymmetryArtmeshBindingsLinksItemAxis": ".transaction_request_operations_operations_item_action_symmetry_artmesh_bindings_links_item_axis",
    "TransactionRequestOperationsOperationsItemActionSymmetryArtmeshBindingsLinksItemKind": ".transaction_request_operations_operations_item_action_symmetry_artmesh_bindings_links_item_kind",
    "TransactionRequestOperationsOperationsItemActionSymmetryArtmeshBindingsLinksItemKindOne": ".transaction_request_operations_operations_item_action_symmetry_artmesh_bindings_links_item_kind_one",
    "TransactionRequestOperationsOperationsItemActionSymmetryArtmeshBindingsLinksItemKindThree": ".transaction_request_operations_operations_item_action_symmetry_artmesh_bindings_links_item_kind_three",
    "TransactionRequestOperationsOperationsItemActionSymmetryArtmeshBindingsLinksItemKindTwo": ".transaction_request_operations_operations_item_action_symmetry_artmesh_bindings_links_item_kind_two",
    "TransactionRequestOperationsOperationsItemActionSymmetryArtmeshBindingsLinksItemKindZero": ".transaction_request_operations_operations_item_action_symmetry_artmesh_bindings_links_item_kind_zero",
    "TransactionRequestOperationsOperationsItemActionSymmetryContract": ".transaction_request_operations_operations_item_action_symmetry_contract",
    "TransactionRequestOperationsOperationsItemActionSymmetryContractContract": ".transaction_request_operations_operations_item_action_symmetry_contract_contract",
    "TransactionRequestOperationsOperationsItemActionSymmetryContractContractAxis": ".transaction_request_operations_operations_item_action_symmetry_contract_contract_axis",
    "TransactionRequestOperationsOperationsItemActionSymmetryContractContractLinksItem": ".transaction_request_operations_operations_item_action_symmetry_contract_contract_links_item",
    "TransactionRequestOperationsOperationsItemActionSymmetryContractContractLinksItemAxis": ".transaction_request_operations_operations_item_action_symmetry_contract_contract_links_item_axis",
    "TransactionRequestOperationsOperationsItemActionSymmetryContractContractLinksItemKind": ".transaction_request_operations_operations_item_action_symmetry_contract_contract_links_item_kind",
    "TransactionRequestOperationsOperationsItemActionSymmetryContractContractLinksItemKindOne": ".transaction_request_operations_operations_item_action_symmetry_contract_contract_links_item_kind_one",
    "TransactionRequestOperationsOperationsItemActionSymmetryContractContractLinksItemKindThree": ".transaction_request_operations_operations_item_action_symmetry_contract_contract_links_item_kind_three",
    "TransactionRequestOperationsOperationsItemActionSymmetryContractContractLinksItemKindTwo": ".transaction_request_operations_operations_item_action_symmetry_contract_contract_links_item_kind_two",
    "TransactionRequestOperationsOperationsItemActionSymmetryContractContractLinksItemKindZero": ".transaction_request_operations_operations_item_action_symmetry_contract_contract_links_item_kind_zero",
    "TransactionRequestOperationsOperationsItemActionTransform": ".transaction_request_operations_operations_item_action_transform",
    "TransactionRequestOperationsOperationsItemActionTransformOperator": ".transaction_request_operations_operations_item_action_transform_operator",
    "TransactionRequestOperationsOperationsItemActionTransformOperatorOne": ".transaction_request_operations_operations_item_action_transform_operator_one",
    "TransactionRequestOperationsOperationsItemActionTransformOperatorTwo": ".transaction_request_operations_operations_item_action_transform_operator_two",
    "TransactionRequestOperationsOperationsItemActionTransformOperatorZero": ".transaction_request_operations_operations_item_action_transform_operator_zero",
    "TransactionRequestOperationsOperationsItemActionTransformProperty": ".transaction_request_operations_operations_item_action_transform_property",
    "TransactionRequestOperationsOperationsItemActionTransformPropertyFive": ".transaction_request_operations_operations_item_action_transform_property_five",
    "TransactionRequestOperationsOperationsItemActionTransformPropertyFour": ".transaction_request_operations_operations_item_action_transform_property_four",
    "TransactionRequestOperationsOperationsItemActionTransformPropertyOne": ".transaction_request_operations_operations_item_action_transform_property_one",
    "TransactionRequestOperationsOperationsItemActionTransformPropertyThree": ".transaction_request_operations_operations_item_action_transform_property_three",
    "TransactionRequestOperationsOperationsItemActionTransformPropertyTwo": ".transaction_request_operations_operations_item_action_transform_property_two",
    "TransactionRequestOperationsOperationsItemActionTransformPropertyZero": ".transaction_request_operations_operations_item_action_transform_property_zero",
    "TransactionRequestOperationsOperationsItemActionWarpPinBindingKey": ".transaction_request_operations_operations_item_action_warp_pin_binding_key",
    "TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyCurve": ".transaction_request_operations_operations_item_action_warp_pin_binding_key_curve",
    "TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyCurveControlPointsItem": ".transaction_request_operations_operations_item_action_warp_pin_binding_key_curve_control_points_item",
    "TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyInterpolation": ".transaction_request_operations_operations_item_action_warp_pin_binding_key_interpolation",
    "TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyInterpolationFour": ".transaction_request_operations_operations_item_action_warp_pin_binding_key_interpolation_four",
    "TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyInterpolationOne": ".transaction_request_operations_operations_item_action_warp_pin_binding_key_interpolation_one",
    "TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyInterpolationThree": ".transaction_request_operations_operations_item_action_warp_pin_binding_key_interpolation_three",
    "TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyInterpolationTwo": ".transaction_request_operations_operations_item_action_warp_pin_binding_key_interpolation_two",
    "TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyInterpolationZero": ".transaction_request_operations_operations_item_action_warp_pin_binding_key_interpolation_zero",
    "TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyProperty": ".transaction_request_operations_operations_item_action_warp_pin_binding_key_property",
    "TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyPropertyOne": ".transaction_request_operations_operations_item_action_warp_pin_binding_key_property_one",
    "TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyPropertyZero": ".transaction_request_operations_operations_item_action_warp_pin_binding_key_property_zero",
    "TransactionRequestOperationsOperationsItemAction_ArtmeshBindingKey": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemAction_ArtmeshBlendShape": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemAction_ArtmeshGenerate": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemAction_ArtmeshMirrorKey": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemAction_ArtmeshMultiKey": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemAction_ArtmeshOffset": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemAction_ArtmeshQuality": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemAction_ArtmeshRebuild": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemAction_BindingKey": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemAction_BlendShapeSet": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemAction_DeformBrush": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemAction_DeformerBindingKey": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemAction_DeformerBindingRemove": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemAction_DeformerCreate": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemAction_DeformerKindSet": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemAction_DeformerOrigin": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemAction_DeformerParentSet": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemAction_DeformerRotationMetadata": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemAction_DeformerSplit": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemAction_DeformerTargetsSet": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemAction_DeformerTransform": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemAction_ParameterAdd": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemAction_PartAlphaReveal": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemAction_PartBlendMode": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemAction_PartClip": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemAction_PartContourShade": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemAction_PartDrawOrder": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemAction_PartTint": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemAction_PartVisibility": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemAction_RoleConfirm": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemAction_RoleReclassify": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemAction_SymmetryArtmeshBindings": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemAction_SymmetryContract": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemAction_Transform": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemAction_WarpPinBindingKey": ".transaction_request_operations_operations_item_action",
    "TransactionRequestOperationsOperationsItemTarget": ".transaction_request_operations_operations_item_target",
    "TransactionRequestOperationsOperationsItemTargetRolesItem": ".transaction_request_operations_operations_item_target_roles_item",
    "TransactionRequestOperationsOperationsItemTargetRolesItemEight": ".transaction_request_operations_operations_item_target_roles_item_eight",
    "TransactionRequestOperationsOperationsItemTargetRolesItemEleven": ".transaction_request_operations_operations_item_target_roles_item_eleven",
    "TransactionRequestOperationsOperationsItemTargetRolesItemFifteen": ".transaction_request_operations_operations_item_target_roles_item_fifteen",
    "TransactionRequestOperationsOperationsItemTargetRolesItemFive": ".transaction_request_operations_operations_item_target_roles_item_five",
    "TransactionRequestOperationsOperationsItemTargetRolesItemFour": ".transaction_request_operations_operations_item_target_roles_item_four",
    "TransactionRequestOperationsOperationsItemTargetRolesItemFourteen": ".transaction_request_operations_operations_item_target_roles_item_fourteen",
    "TransactionRequestOperationsOperationsItemTargetRolesItemNine": ".transaction_request_operations_operations_item_target_roles_item_nine",
    "TransactionRequestOperationsOperationsItemTargetRolesItemOne": ".transaction_request_operations_operations_item_target_roles_item_one",
    "TransactionRequestOperationsOperationsItemTargetRolesItemSeven": ".transaction_request_operations_operations_item_target_roles_item_seven",
    "TransactionRequestOperationsOperationsItemTargetRolesItemSeventeen": ".transaction_request_operations_operations_item_target_roles_item_seventeen",
    "TransactionRequestOperationsOperationsItemTargetRolesItemSix": ".transaction_request_operations_operations_item_target_roles_item_six",
    "TransactionRequestOperationsOperationsItemTargetRolesItemSixteen": ".transaction_request_operations_operations_item_target_roles_item_sixteen",
    "TransactionRequestOperationsOperationsItemTargetRolesItemTen": ".transaction_request_operations_operations_item_target_roles_item_ten",
    "TransactionRequestOperationsOperationsItemTargetRolesItemThirteen": ".transaction_request_operations_operations_item_target_roles_item_thirteen",
    "TransactionRequestOperationsOperationsItemTargetRolesItemThree": ".transaction_request_operations_operations_item_target_roles_item_three",
    "TransactionRequestOperationsOperationsItemTargetRolesItemTwelve": ".transaction_request_operations_operations_item_target_roles_item_twelve",
    "TransactionRequestOperationsOperationsItemTargetRolesItemTwo": ".transaction_request_operations_operations_item_target_roles_item_two",
    "TransactionRequestOperationsOperationsItemTargetRolesItemZero": ".transaction_request_operations_operations_item_target_roles_item_zero",
    "TransactionRequestOperationsQa": ".transaction_request_operations_qa",
    "TransactionRequestOperationsQaMotionSweep": ".transaction_request_operations_qa_motion_sweep",
    "TransactionRequestOperationsQaMotionSweepCheckMonotonic": ".transaction_request_operations_qa_motion_sweep_check_monotonic",
    "TransactionRequestOperationsQaPoseSamplesItem": ".transaction_request_operations_qa_pose_samples_item",
    "TransactionRequestRig": ".transaction_request_rig",
    "TransactionRequestRigKind": ".transaction_request_rig_kind",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "GetApiPlaybackMotionResponse",
    "GetApiPlaybackMotionResponsePlayback",
    "GetApiPlaybackMotionResponsePlaybackDemo",
    "GetApiPlaybackMotionResponsePlaybackDemoMode",
    "GetApiPlaybackMotionResponsePlaybackMotion",
    "GetApiPlaybackResponse",
    "GetApiPlaybackResponsePlayback",
    "GetApiPlaybackResponsePlaybackDemo",
    "GetApiPlaybackResponsePlaybackDemoMode",
    "GetApiPlaybackResponsePlaybackMotion",
    "ModelingOperation",
    "ModelingOperationAction",
    "ModelingOperationActionArtmeshBindingKey",
    "ModelingOperationActionArtmeshBindingKeyCurve",
    "ModelingOperationActionArtmeshBindingKeyCurveControlPointsItem",
    "ModelingOperationActionArtmeshBindingKeyInterpolation",
    "ModelingOperationActionArtmeshBindingKeyInterpolationFour",
    "ModelingOperationActionArtmeshBindingKeyInterpolationOne",
    "ModelingOperationActionArtmeshBindingKeyInterpolationThree",
    "ModelingOperationActionArtmeshBindingKeyInterpolationTwo",
    "ModelingOperationActionArtmeshBindingKeyInterpolationZero",
    "ModelingOperationActionArtmeshBindingKeyOffsetsItem",
    "ModelingOperationActionArtmeshBlendShape",
    "ModelingOperationActionArtmeshBlendShapeCurve",
    "ModelingOperationActionArtmeshBlendShapeCurveControlPointsItem",
    "ModelingOperationActionArtmeshBlendShapeInterpolation",
    "ModelingOperationActionArtmeshBlendShapeInterpolationFour",
    "ModelingOperationActionArtmeshBlendShapeInterpolationOne",
    "ModelingOperationActionArtmeshBlendShapeInterpolationThree",
    "ModelingOperationActionArtmeshBlendShapeInterpolationTwo",
    "ModelingOperationActionArtmeshBlendShapeInterpolationZero",
    "ModelingOperationActionArtmeshBlendShapeOffsetsItem",
    "ModelingOperationActionArtmeshGenerate",
    "ModelingOperationActionArtmeshGeneratePreset",
    "ModelingOperationActionArtmeshGeneratePresetFive",
    "ModelingOperationActionArtmeshGeneratePresetFour",
    "ModelingOperationActionArtmeshGeneratePresetOne",
    "ModelingOperationActionArtmeshGeneratePresetThree",
    "ModelingOperationActionArtmeshGeneratePresetTwo",
    "ModelingOperationActionArtmeshGeneratePresetZero",
    "ModelingOperationActionArtmeshGenerateQuality",
    "ModelingOperationActionArtmeshGenerateTopology",
    "ModelingOperationActionArtmeshGenerateTopologyOne",
    "ModelingOperationActionArtmeshGenerateTopologyZero",
    "ModelingOperationActionArtmeshMirrorKey",
    "ModelingOperationActionArtmeshMirrorKeyCurve",
    "ModelingOperationActionArtmeshMirrorKeyCurveControlPointsItem",
    "ModelingOperationActionArtmeshMirrorKeyInterpolation",
    "ModelingOperationActionArtmeshMirrorKeyInterpolationFour",
    "ModelingOperationActionArtmeshMirrorKeyInterpolationOne",
    "ModelingOperationActionArtmeshMirrorKeyInterpolationThree",
    "ModelingOperationActionArtmeshMirrorKeyInterpolationTwo",
    "ModelingOperationActionArtmeshMirrorKeyInterpolationZero",
    "ModelingOperationActionArtmeshMultiKey",
    "ModelingOperationActionArtmeshMultiKeyCurve",
    "ModelingOperationActionArtmeshMultiKeyCurveControlPointsItem",
    "ModelingOperationActionArtmeshMultiKeyInterpolation",
    "ModelingOperationActionArtmeshMultiKeyInterpolationFour",
    "ModelingOperationActionArtmeshMultiKeyInterpolationOne",
    "ModelingOperationActionArtmeshMultiKeyInterpolationThree",
    "ModelingOperationActionArtmeshMultiKeyInterpolationTwo",
    "ModelingOperationActionArtmeshMultiKeyInterpolationZero",
    "ModelingOperationActionArtmeshMultiKeyOffsetsItem",
    "ModelingOperationActionArtmeshOffset",
    "ModelingOperationActionArtmeshOffsetUv",
    "ModelingOperationActionArtmeshQuality",
    "ModelingOperationActionArtmeshQualityQuality",
    "ModelingOperationActionArtmeshRebuild",
    "ModelingOperationActionArtmeshRebuildPreset",
    "ModelingOperationActionArtmeshRebuildPresetFive",
    "ModelingOperationActionArtmeshRebuildPresetFour",
    "ModelingOperationActionArtmeshRebuildPresetOne",
    "ModelingOperationActionArtmeshRebuildPresetThree",
    "ModelingOperationActionArtmeshRebuildPresetTwo",
    "ModelingOperationActionArtmeshRebuildPresetZero",
    "ModelingOperationActionArtmeshRebuildQuality",
    "ModelingOperationActionArtmeshRebuildTopology",
    "ModelingOperationActionArtmeshRebuildTopologyOne",
    "ModelingOperationActionArtmeshRebuildTopologyZero",
    "ModelingOperationActionBindingKey",
    "ModelingOperationActionBindingKeyCurve",
    "ModelingOperationActionBindingKeyCurveControlPointsItem",
    "ModelingOperationActionBindingKeyInterpolation",
    "ModelingOperationActionBindingKeyInterpolationFour",
    "ModelingOperationActionBindingKeyInterpolationOne",
    "ModelingOperationActionBindingKeyInterpolationThree",
    "ModelingOperationActionBindingKeyInterpolationTwo",
    "ModelingOperationActionBindingKeyInterpolationZero",
    "ModelingOperationActionBindingKeyProperty",
    "ModelingOperationActionBindingKeyPropertyFive",
    "ModelingOperationActionBindingKeyPropertyFour",
    "ModelingOperationActionBindingKeyPropertyOne",
    "ModelingOperationActionBindingKeyPropertyThree",
    "ModelingOperationActionBindingKeyPropertyTwo",
    "ModelingOperationActionBindingKeyPropertyZero",
    "ModelingOperationActionBlendShapeSet",
    "ModelingOperationActionBlendShapeSetShape",
    "ModelingOperationActionBlendShapeSetShapeArtPath",
    "ModelingOperationActionBlendShapeSetShapeArtPathCurve",
    "ModelingOperationActionBlendShapeSetShapeArtPathCurveControlPointsItem",
    "ModelingOperationActionBlendShapeSetShapeArtPathInterpolation",
    "ModelingOperationActionBlendShapeSetShapeArtPathInterpolationFour",
    "ModelingOperationActionBlendShapeSetShapeArtPathInterpolationOne",
    "ModelingOperationActionBlendShapeSetShapeArtPathInterpolationThree",
    "ModelingOperationActionBlendShapeSetShapeArtPathInterpolationTwo",
    "ModelingOperationActionBlendShapeSetShapeArtPathInterpolationZero",
    "ModelingOperationActionBlendShapeSetShapeArtPathPointsItem",
    "ModelingOperationActionBlendShapeSetShapeDeformer",
    "ModelingOperationActionBlendShapeSetShapeDeformerCurve",
    "ModelingOperationActionBlendShapeSetShapeDeformerCurveControlPointsItem",
    "ModelingOperationActionBlendShapeSetShapeDeformerInterpolation",
    "ModelingOperationActionBlendShapeSetShapeDeformerInterpolationFour",
    "ModelingOperationActionBlendShapeSetShapeDeformerInterpolationOne",
    "ModelingOperationActionBlendShapeSetShapeDeformerInterpolationThree",
    "ModelingOperationActionBlendShapeSetShapeDeformerInterpolationTwo",
    "ModelingOperationActionBlendShapeSetShapeDeformerInterpolationZero",
    "ModelingOperationActionBlendShapeSetShapeDeformerPinsItem",
    "ModelingOperationActionBlendShapeSetShapeDeformerSharedPointsItem",
    "ModelingOperationActionBlendShapeSetShapeDeformerTransform",
    "ModelingOperationActionBlendShapeSetShapeDeformerWarp",
    "ModelingOperationActionBlendShapeSetShapeGlue",
    "ModelingOperationActionBlendShapeSetShapeGlueCurve",
    "ModelingOperationActionBlendShapeSetShapeGlueCurveControlPointsItem",
    "ModelingOperationActionBlendShapeSetShapeGlueInterpolation",
    "ModelingOperationActionBlendShapeSetShapeGlueInterpolationFour",
    "ModelingOperationActionBlendShapeSetShapeGlueInterpolationOne",
    "ModelingOperationActionBlendShapeSetShapeGlueInterpolationThree",
    "ModelingOperationActionBlendShapeSetShapeGlueInterpolationTwo",
    "ModelingOperationActionBlendShapeSetShapeGlueInterpolationZero",
    "ModelingOperationActionBlendShapeSetShapePart",
    "ModelingOperationActionBlendShapeSetShapePartCurve",
    "ModelingOperationActionBlendShapeSetShapePartCurveControlPointsItem",
    "ModelingOperationActionBlendShapeSetShapePartInterpolation",
    "ModelingOperationActionBlendShapeSetShapePartInterpolationFour",
    "ModelingOperationActionBlendShapeSetShapePartInterpolationOne",
    "ModelingOperationActionBlendShapeSetShapePartInterpolationThree",
    "ModelingOperationActionBlendShapeSetShapePartInterpolationTwo",
    "ModelingOperationActionBlendShapeSetShapePartInterpolationZero",
    "ModelingOperationActionBlendShapeSetShapePartTransform",
    "ModelingOperationActionBlendShapeSetShape_ArtPath",
    "ModelingOperationActionBlendShapeSetShape_Deformer",
    "ModelingOperationActionBlendShapeSetShape_Glue",
    "ModelingOperationActionBlendShapeSetShape_Part",
    "ModelingOperationActionDeformBrush",
    "ModelingOperationActionDeformBrushBrush",
    "ModelingOperationActionDeformBrushBrushDestination",
    "ModelingOperationActionDeformBrushBrushDestinationBase",
    "ModelingOperationActionDeformBrushBrushDestinationBlendShape",
    "ModelingOperationActionDeformBrushBrushDestinationBlendShapeShape",
    "ModelingOperationActionDeformBrushBrushDestinationBlendShapeShapeCurve",
    "ModelingOperationActionDeformBrushBrushDestinationBlendShapeShapeCurveControlPointsItem",
    "ModelingOperationActionDeformBrushBrushDestinationBlendShapeShapeInterpolation",
    "ModelingOperationActionDeformBrushBrushDestinationBlendShapeShapeInterpolationFour",
    "ModelingOperationActionDeformBrushBrushDestinationBlendShapeShapeInterpolationOne",
    "ModelingOperationActionDeformBrushBrushDestinationBlendShapeShapeInterpolationThree",
    "ModelingOperationActionDeformBrushBrushDestinationBlendShapeShapeInterpolationTwo",
    "ModelingOperationActionDeformBrushBrushDestinationBlendShapeShapeInterpolationZero",
    "ModelingOperationActionDeformBrushBrushDestinationKeyform",
    "ModelingOperationActionDeformBrushBrushDestination_Base",
    "ModelingOperationActionDeformBrushBrushDestination_BlendShape",
    "ModelingOperationActionDeformBrushBrushDestination_Keyform",
    "ModelingOperationActionDeformBrushBrushEffect",
    "ModelingOperationActionDeformBrushBrushEffectBend",
    "ModelingOperationActionDeformBrushBrushEffectContourFollow",
    "ModelingOperationActionDeformBrushBrushEffectInflate",
    "ModelingOperationActionDeformBrushBrushEffectPinch",
    "ModelingOperationActionDeformBrushBrushEffectRelax",
    "ModelingOperationActionDeformBrushBrushEffectSmooth",
    "ModelingOperationActionDeformBrushBrushEffect_Bend",
    "ModelingOperationActionDeformBrushBrushEffect_ContourFollow",
    "ModelingOperationActionDeformBrushBrushEffect_Inflate",
    "ModelingOperationActionDeformBrushBrushEffect_Pinch",
    "ModelingOperationActionDeformBrushBrushEffect_Relax",
    "ModelingOperationActionDeformBrushBrushEffect_Smooth",
    "ModelingOperationActionDeformBrushBrushFalloff",
    "ModelingOperationActionDeformBrushBrushFalloffOne",
    "ModelingOperationActionDeformBrushBrushFalloffZero",
    "ModelingOperationActionDeformBrushBrushSurface",
    "ModelingOperationActionDeformBrushBrushSurfaceArtmesh",
    "ModelingOperationActionDeformBrushBrushSurfaceArtmeshSpace",
    "ModelingOperationActionDeformBrushBrushSurfaceSharedWarp",
    "ModelingOperationActionDeformBrushBrushSurfaceSharedWarpSpace",
    "ModelingOperationActionDeformBrushBrushSurfaceWarpPins",
    "ModelingOperationActionDeformBrushBrushSurfaceWarpPinsSpace",
    "ModelingOperationActionDeformBrushBrushSurface_Artmesh",
    "ModelingOperationActionDeformBrushBrushSurface_SharedWarp",
    "ModelingOperationActionDeformBrushBrushSurface_WarpPins",
    "ModelingOperationActionDeformerBindingKey",
    "ModelingOperationActionDeformerBindingKeyCurve",
    "ModelingOperationActionDeformerBindingKeyCurveControlPointsItem",
    "ModelingOperationActionDeformerBindingKeyInterpolation",
    "ModelingOperationActionDeformerBindingKeyInterpolationFour",
    "ModelingOperationActionDeformerBindingKeyInterpolationOne",
    "ModelingOperationActionDeformerBindingKeyInterpolationThree",
    "ModelingOperationActionDeformerBindingKeyInterpolationTwo",
    "ModelingOperationActionDeformerBindingKeyInterpolationZero",
    "ModelingOperationActionDeformerBindingKeyProperty",
    "ModelingOperationActionDeformerBindingKeyPropertyEight",
    "ModelingOperationActionDeformerBindingKeyPropertyFive",
    "ModelingOperationActionDeformerBindingKeyPropertyFour",
    "ModelingOperationActionDeformerBindingKeyPropertyNine",
    "ModelingOperationActionDeformerBindingKeyPropertyOne",
    "ModelingOperationActionDeformerBindingKeyPropertySeven",
    "ModelingOperationActionDeformerBindingKeyPropertySix",
    "ModelingOperationActionDeformerBindingKeyPropertyThree",
    "ModelingOperationActionDeformerBindingKeyPropertyTwo",
    "ModelingOperationActionDeformerBindingKeyPropertyZero",
    "ModelingOperationActionDeformerBindingRemove",
    "ModelingOperationActionDeformerBindingRemoveProperty",
    "ModelingOperationActionDeformerBindingRemovePropertyEight",
    "ModelingOperationActionDeformerBindingRemovePropertyFive",
    "ModelingOperationActionDeformerBindingRemovePropertyFour",
    "ModelingOperationActionDeformerBindingRemovePropertyNine",
    "ModelingOperationActionDeformerBindingRemovePropertyOne",
    "ModelingOperationActionDeformerBindingRemovePropertySeven",
    "ModelingOperationActionDeformerBindingRemovePropertySix",
    "ModelingOperationActionDeformerBindingRemovePropertyThree",
    "ModelingOperationActionDeformerBindingRemovePropertyTwo",
    "ModelingOperationActionDeformerBindingRemovePropertyZero",
    "ModelingOperationActionDeformerCreate",
    "ModelingOperationActionDeformerCreateDeformer",
    "ModelingOperationActionDeformerCreateDeformerBindingsItem",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemComposition",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemCompositionOne",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemCompositionZero",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemCurve",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemCurveControlPointsItem",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemInterpolation",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemInterpolationFour",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemInterpolationOne",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemInterpolationThree",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemInterpolationTwo",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemInterpolationZero",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemKeysItem",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemProperty",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemPropertyEight",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemPropertyFive",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemPropertyFour",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemPropertyNine",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemPropertyOne",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemPropertySeven",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemPropertySix",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemPropertyThree",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemPropertyTwo",
    "ModelingOperationActionDeformerCreateDeformerBindingsItemPropertyZero",
    "ModelingOperationActionDeformerCreateDeformerBlendShapesItem",
    "ModelingOperationActionDeformerCreateDeformerBlendShapesItemCurve",
    "ModelingOperationActionDeformerCreateDeformerBlendShapesItemCurveControlPointsItem",
    "ModelingOperationActionDeformerCreateDeformerBlendShapesItemInterpolation",
    "ModelingOperationActionDeformerCreateDeformerBlendShapesItemInterpolationFour",
    "ModelingOperationActionDeformerCreateDeformerBlendShapesItemInterpolationOne",
    "ModelingOperationActionDeformerCreateDeformerBlendShapesItemInterpolationThree",
    "ModelingOperationActionDeformerCreateDeformerBlendShapesItemInterpolationTwo",
    "ModelingOperationActionDeformerCreateDeformerBlendShapesItemInterpolationZero",
    "ModelingOperationActionDeformerCreateDeformerBlendShapesItemKind",
    "ModelingOperationActionDeformerCreateDeformerBlendShapesItemPinsItem",
    "ModelingOperationActionDeformerCreateDeformerBlendShapesItemSharedPointsItem",
    "ModelingOperationActionDeformerCreateDeformerBlendShapesItemTransform",
    "ModelingOperationActionDeformerCreateDeformerBlendShapesItemWarp",
    "ModelingOperationActionDeformerCreateDeformerKind",
    "ModelingOperationActionDeformerCreateDeformerKindOne",
    "ModelingOperationActionDeformerCreateDeformerKindTwo",
    "ModelingOperationActionDeformerCreateDeformerKindZero",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItem",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemComposition",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemCompositionOne",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemCompositionZero",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemCurve",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemCurveControlPointsItem",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemInterpolation",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemInterpolationFour",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemInterpolationOne",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemInterpolationThree",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemInterpolationTwo",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemInterpolationZero",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemKeyformsItem",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemProperty",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertyEight",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertyEleven",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertyFive",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertyFour",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertyNine",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertyOne",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertySeven",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertySix",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertyTen",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertyThree",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertyTwo",
    "ModelingOperationActionDeformerCreateDeformerMultiBindingsItemPropertyZero",
    "ModelingOperationActionDeformerCreateDeformerOrigin",
    "ModelingOperationActionDeformerCreateDeformerRotationMetadata",
    "ModelingOperationActionDeformerCreateDeformerRotationMetadataAngleRange",
    "ModelingOperationActionDeformerCreateDeformerRotationMetadataAngleUnit",
    "ModelingOperationActionDeformerCreateDeformerRotationMetadataParentComposition",
    "ModelingOperationActionDeformerCreateDeformerRotationMetadataParentCompositionOne",
    "ModelingOperationActionDeformerCreateDeformerRotationMetadataParentCompositionZero",
    "ModelingOperationActionDeformerCreateDeformerRotationMetadataPivot",
    "ModelingOperationActionDeformerCreateDeformerRotationMetadataPivotSpace",
    "ModelingOperationActionDeformerCreateDeformerRotationMetadataPivotSpaceOne",
    "ModelingOperationActionDeformerCreateDeformerRotationMetadataPivotSpaceZero",
    "ModelingOperationActionDeformerCreateDeformerRotationMetadataShapePreservation",
    "ModelingOperationActionDeformerCreateDeformerRotationMetadataShapePreservationOne",
    "ModelingOperationActionDeformerCreateDeformerRotationMetadataShapePreservationTwo",
    "ModelingOperationActionDeformerCreateDeformerRotationMetadataShapePreservationZero",
    "ModelingOperationActionDeformerCreateDeformerSharedWarp",
    "ModelingOperationActionDeformerCreateDeformerSharedWarpBounds",
    "ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItem",
    "ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItem",
    "ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemCurve",
    "ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemCurveControlPointsItem",
    "ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolation",
    "ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolationFour",
    "ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolationOne",
    "ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolationThree",
    "ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolationTwo",
    "ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolationZero",
    "ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemKeysItem",
    "ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemProperty",
    "ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemPropertyOne",
    "ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemPropertyZero",
    "ModelingOperationActionDeformerCreateDeformerSharedWarpGrid",
    "ModelingOperationActionDeformerCreateDeformerTransform",
    "ModelingOperationActionDeformerCreateDeformerWarp",
    "ModelingOperationActionDeformerCreateDeformerWarpGrid",
    "ModelingOperationActionDeformerCreateDeformerWarpPinBlendMode",
    "ModelingOperationActionDeformerCreateDeformerWarpPinBlendModeOne",
    "ModelingOperationActionDeformerCreateDeformerWarpPinBlendModeZero",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItem",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItem",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemCurve",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemCurveControlPointsItem",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolation",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolationFour",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolationOne",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolationThree",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolationTwo",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolationZero",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemKeysItem",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemProperty",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemPropertyOne",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemBindingsItemPropertyZero",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItem",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemCurve",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemCurveControlPointsItem",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolation",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolationFour",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolationOne",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolationThree",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolationTwo",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolationZero",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemKeyformsItem",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemProperty",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemPropertyOne",
    "ModelingOperationActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemPropertyZero",
    "ModelingOperationActionDeformerKindSet",
    "ModelingOperationActionDeformerKindSetKind",
    "ModelingOperationActionDeformerKindSetKindOne",
    "ModelingOperationActionDeformerKindSetKindTwo",
    "ModelingOperationActionDeformerKindSetKindZero",
    "ModelingOperationActionDeformerKindSetWarp",
    "ModelingOperationActionDeformerKindSetWarpGrid",
    "ModelingOperationActionDeformerKindSetWarpPinBlendMode",
    "ModelingOperationActionDeformerKindSetWarpPinBlendModeOne",
    "ModelingOperationActionDeformerKindSetWarpPinBlendModeZero",
    "ModelingOperationActionDeformerKindSetWarpPinsItem",
    "ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItem",
    "ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemCurve",
    "ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemCurveControlPointsItem",
    "ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemInterpolation",
    "ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemInterpolationFour",
    "ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemInterpolationOne",
    "ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemInterpolationThree",
    "ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemInterpolationTwo",
    "ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemInterpolationZero",
    "ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemKeysItem",
    "ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemProperty",
    "ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemPropertyOne",
    "ModelingOperationActionDeformerKindSetWarpPinsItemBindingsItemPropertyZero",
    "ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItem",
    "ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemCurve",
    "ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemCurveControlPointsItem",
    "ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolation",
    "ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolationFour",
    "ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolationOne",
    "ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolationThree",
    "ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolationTwo",
    "ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolationZero",
    "ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemKeyformsItem",
    "ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemProperty",
    "ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemPropertyOne",
    "ModelingOperationActionDeformerKindSetWarpPinsItemMultiBindingsItemPropertyZero",
    "ModelingOperationActionDeformerOrigin",
    "ModelingOperationActionDeformerParentSet",
    "ModelingOperationActionDeformerRotationMetadata",
    "ModelingOperationActionDeformerRotationMetadataMetadata",
    "ModelingOperationActionDeformerRotationMetadataMetadataAngleRange",
    "ModelingOperationActionDeformerRotationMetadataMetadataAngleUnit",
    "ModelingOperationActionDeformerRotationMetadataMetadataParentComposition",
    "ModelingOperationActionDeformerRotationMetadataMetadataParentCompositionOne",
    "ModelingOperationActionDeformerRotationMetadataMetadataParentCompositionZero",
    "ModelingOperationActionDeformerRotationMetadataMetadataPivot",
    "ModelingOperationActionDeformerRotationMetadataMetadataPivotSpace",
    "ModelingOperationActionDeformerRotationMetadataMetadataPivotSpaceOne",
    "ModelingOperationActionDeformerRotationMetadataMetadataPivotSpaceZero",
    "ModelingOperationActionDeformerRotationMetadataMetadataShapePreservation",
    "ModelingOperationActionDeformerRotationMetadataMetadataShapePreservationOne",
    "ModelingOperationActionDeformerRotationMetadataMetadataShapePreservationTwo",
    "ModelingOperationActionDeformerRotationMetadataMetadataShapePreservationZero",
    "ModelingOperationActionDeformerSplit",
    "ModelingOperationActionDeformerTargetsSet",
    "ModelingOperationActionDeformerTargetsSetMode",
    "ModelingOperationActionDeformerTargetsSetModeOne",
    "ModelingOperationActionDeformerTargetsSetModeZero",
    "ModelingOperationActionDeformerTransform",
    "ModelingOperationActionDeformerTransformOperator",
    "ModelingOperationActionDeformerTransformOperatorOne",
    "ModelingOperationActionDeformerTransformOperatorTwo",
    "ModelingOperationActionDeformerTransformOperatorZero",
    "ModelingOperationActionDeformerTransformProperty",
    "ModelingOperationActionDeformerTransformPropertyFive",
    "ModelingOperationActionDeformerTransformPropertyFour",
    "ModelingOperationActionDeformerTransformPropertyOne",
    "ModelingOperationActionDeformerTransformPropertyThree",
    "ModelingOperationActionDeformerTransformPropertyTwo",
    "ModelingOperationActionDeformerTransformPropertyZero",
    "ModelingOperationActionParameterAdd",
    "ModelingOperationActionParameterAddParameter",
    "ModelingOperationActionPartAlphaReveal",
    "ModelingOperationActionPartAlphaRevealReveal",
    "ModelingOperationActionPartBlendMode",
    "ModelingOperationActionPartBlendModeMode",
    "ModelingOperationActionPartBlendModeModeOne",
    "ModelingOperationActionPartBlendModeModeThree",
    "ModelingOperationActionPartBlendModeModeTwo",
    "ModelingOperationActionPartBlendModeModeZero",
    "ModelingOperationActionPartClip",
    "ModelingOperationActionPartClipClip",
    "ModelingOperationActionPartClipClipMaskOpacity",
    "ModelingOperationActionPartClipClipMaskOpacityOne",
    "ModelingOperationActionPartClipClipMaskOpacityZero",
    "ModelingOperationActionPartClipClipMode",
    "ModelingOperationActionPartContourShade",
    "ModelingOperationActionPartContourShadeShade",
    "ModelingOperationActionPartContourShadeShadeProfile",
    "ModelingOperationActionPartDrawOrder",
    "ModelingOperationActionPartTint",
    "ModelingOperationActionPartTintTint",
    "ModelingOperationActionPartTintTintMode",
    "ModelingOperationActionPartTintTintModeOne",
    "ModelingOperationActionPartTintTintModeZero",
    "ModelingOperationActionPartVisibility",
    "ModelingOperationActionRoleConfirm",
    "ModelingOperationActionRoleConfirmRole",
    "ModelingOperationActionRoleConfirmRoleEight",
    "ModelingOperationActionRoleConfirmRoleEleven",
    "ModelingOperationActionRoleConfirmRoleFifteen",
    "ModelingOperationActionRoleConfirmRoleFive",
    "ModelingOperationActionRoleConfirmRoleFour",
    "ModelingOperationActionRoleConfirmRoleFourteen",
    "ModelingOperationActionRoleConfirmRoleNine",
    "ModelingOperationActionRoleConfirmRoleOne",
    "ModelingOperationActionRoleConfirmRoleSeven",
    "ModelingOperationActionRoleConfirmRoleSeventeen",
    "ModelingOperationActionRoleConfirmRoleSix",
    "ModelingOperationActionRoleConfirmRoleSixteen",
    "ModelingOperationActionRoleConfirmRoleTen",
    "ModelingOperationActionRoleConfirmRoleThirteen",
    "ModelingOperationActionRoleConfirmRoleThree",
    "ModelingOperationActionRoleConfirmRoleTwelve",
    "ModelingOperationActionRoleConfirmRoleTwo",
    "ModelingOperationActionRoleConfirmRoleZero",
    "ModelingOperationActionRoleReclassify",
    "ModelingOperationActionRoleReclassifyExpectedRole",
    "ModelingOperationActionRoleReclassifyExpectedRoleEight",
    "ModelingOperationActionRoleReclassifyExpectedRoleEleven",
    "ModelingOperationActionRoleReclassifyExpectedRoleFifteen",
    "ModelingOperationActionRoleReclassifyExpectedRoleFive",
    "ModelingOperationActionRoleReclassifyExpectedRoleFour",
    "ModelingOperationActionRoleReclassifyExpectedRoleFourteen",
    "ModelingOperationActionRoleReclassifyExpectedRoleNine",
    "ModelingOperationActionRoleReclassifyExpectedRoleOne",
    "ModelingOperationActionRoleReclassifyExpectedRoleSeven",
    "ModelingOperationActionRoleReclassifyExpectedRoleSeventeen",
    "ModelingOperationActionRoleReclassifyExpectedRoleSix",
    "ModelingOperationActionRoleReclassifyExpectedRoleSixteen",
    "ModelingOperationActionRoleReclassifyExpectedRoleTen",
    "ModelingOperationActionRoleReclassifyExpectedRoleThirteen",
    "ModelingOperationActionRoleReclassifyExpectedRoleThree",
    "ModelingOperationActionRoleReclassifyExpectedRoleTwelve",
    "ModelingOperationActionRoleReclassifyExpectedRoleTwo",
    "ModelingOperationActionRoleReclassifyExpectedRoleZero",
    "ModelingOperationActionRoleReclassifyRole",
    "ModelingOperationActionRoleReclassifyRoleEight",
    "ModelingOperationActionRoleReclassifyRoleEleven",
    "ModelingOperationActionRoleReclassifyRoleFifteen",
    "ModelingOperationActionRoleReclassifyRoleFive",
    "ModelingOperationActionRoleReclassifyRoleFour",
    "ModelingOperationActionRoleReclassifyRoleFourteen",
    "ModelingOperationActionRoleReclassifyRoleNine",
    "ModelingOperationActionRoleReclassifyRoleOne",
    "ModelingOperationActionRoleReclassifyRoleSeven",
    "ModelingOperationActionRoleReclassifyRoleSeventeen",
    "ModelingOperationActionRoleReclassifyRoleSix",
    "ModelingOperationActionRoleReclassifyRoleSixteen",
    "ModelingOperationActionRoleReclassifyRoleTen",
    "ModelingOperationActionRoleReclassifyRoleThirteen",
    "ModelingOperationActionRoleReclassifyRoleThree",
    "ModelingOperationActionRoleReclassifyRoleTwelve",
    "ModelingOperationActionRoleReclassifyRoleTwo",
    "ModelingOperationActionRoleReclassifyRoleZero",
    "ModelingOperationActionSymmetryArtmeshBindings",
    "ModelingOperationActionSymmetryArtmeshBindingsLinksItem",
    "ModelingOperationActionSymmetryArtmeshBindingsLinksItemAxis",
    "ModelingOperationActionSymmetryArtmeshBindingsLinksItemKind",
    "ModelingOperationActionSymmetryArtmeshBindingsLinksItemKindOne",
    "ModelingOperationActionSymmetryArtmeshBindingsLinksItemKindThree",
    "ModelingOperationActionSymmetryArtmeshBindingsLinksItemKindTwo",
    "ModelingOperationActionSymmetryArtmeshBindingsLinksItemKindZero",
    "ModelingOperationActionSymmetryContract",
    "ModelingOperationActionSymmetryContractContract",
    "ModelingOperationActionSymmetryContractContractAxis",
    "ModelingOperationActionSymmetryContractContractLinksItem",
    "ModelingOperationActionSymmetryContractContractLinksItemAxis",
    "ModelingOperationActionSymmetryContractContractLinksItemKind",
    "ModelingOperationActionSymmetryContractContractLinksItemKindOne",
    "ModelingOperationActionSymmetryContractContractLinksItemKindThree",
    "ModelingOperationActionSymmetryContractContractLinksItemKindTwo",
    "ModelingOperationActionSymmetryContractContractLinksItemKindZero",
    "ModelingOperationActionTransform",
    "ModelingOperationActionTransformOperator",
    "ModelingOperationActionTransformOperatorOne",
    "ModelingOperationActionTransformOperatorTwo",
    "ModelingOperationActionTransformOperatorZero",
    "ModelingOperationActionTransformProperty",
    "ModelingOperationActionTransformPropertyFive",
    "ModelingOperationActionTransformPropertyFour",
    "ModelingOperationActionTransformPropertyOne",
    "ModelingOperationActionTransformPropertyThree",
    "ModelingOperationActionTransformPropertyTwo",
    "ModelingOperationActionTransformPropertyZero",
    "ModelingOperationActionWarpPinBindingKey",
    "ModelingOperationActionWarpPinBindingKeyCurve",
    "ModelingOperationActionWarpPinBindingKeyCurveControlPointsItem",
    "ModelingOperationActionWarpPinBindingKeyInterpolation",
    "ModelingOperationActionWarpPinBindingKeyInterpolationFour",
    "ModelingOperationActionWarpPinBindingKeyInterpolationOne",
    "ModelingOperationActionWarpPinBindingKeyInterpolationThree",
    "ModelingOperationActionWarpPinBindingKeyInterpolationTwo",
    "ModelingOperationActionWarpPinBindingKeyInterpolationZero",
    "ModelingOperationActionWarpPinBindingKeyProperty",
    "ModelingOperationActionWarpPinBindingKeyPropertyOne",
    "ModelingOperationActionWarpPinBindingKeyPropertyZero",
    "ModelingOperationAction_ArtmeshBindingKey",
    "ModelingOperationAction_ArtmeshBlendShape",
    "ModelingOperationAction_ArtmeshGenerate",
    "ModelingOperationAction_ArtmeshMirrorKey",
    "ModelingOperationAction_ArtmeshMultiKey",
    "ModelingOperationAction_ArtmeshOffset",
    "ModelingOperationAction_ArtmeshQuality",
    "ModelingOperationAction_ArtmeshRebuild",
    "ModelingOperationAction_BindingKey",
    "ModelingOperationAction_BlendShapeSet",
    "ModelingOperationAction_DeformBrush",
    "ModelingOperationAction_DeformerBindingKey",
    "ModelingOperationAction_DeformerBindingRemove",
    "ModelingOperationAction_DeformerCreate",
    "ModelingOperationAction_DeformerKindSet",
    "ModelingOperationAction_DeformerOrigin",
    "ModelingOperationAction_DeformerParentSet",
    "ModelingOperationAction_DeformerRotationMetadata",
    "ModelingOperationAction_DeformerSplit",
    "ModelingOperationAction_DeformerTargetsSet",
    "ModelingOperationAction_DeformerTransform",
    "ModelingOperationAction_ParameterAdd",
    "ModelingOperationAction_PartAlphaReveal",
    "ModelingOperationAction_PartBlendMode",
    "ModelingOperationAction_PartClip",
    "ModelingOperationAction_PartContourShade",
    "ModelingOperationAction_PartDrawOrder",
    "ModelingOperationAction_PartTint",
    "ModelingOperationAction_PartVisibility",
    "ModelingOperationAction_RoleConfirm",
    "ModelingOperationAction_RoleReclassify",
    "ModelingOperationAction_SymmetryArtmeshBindings",
    "ModelingOperationAction_SymmetryContract",
    "ModelingOperationAction_Transform",
    "ModelingOperationAction_WarpPinBindingKey",
    "ModelingOperationTarget",
    "ModelingOperationTargetRolesItem",
    "ModelingOperationTargetRolesItemEight",
    "ModelingOperationTargetRolesItemEleven",
    "ModelingOperationTargetRolesItemFifteen",
    "ModelingOperationTargetRolesItemFive",
    "ModelingOperationTargetRolesItemFour",
    "ModelingOperationTargetRolesItemFourteen",
    "ModelingOperationTargetRolesItemNine",
    "ModelingOperationTargetRolesItemOne",
    "ModelingOperationTargetRolesItemSeven",
    "ModelingOperationTargetRolesItemSeventeen",
    "ModelingOperationTargetRolesItemSix",
    "ModelingOperationTargetRolesItemSixteen",
    "ModelingOperationTargetRolesItemTen",
    "ModelingOperationTargetRolesItemThirteen",
    "ModelingOperationTargetRolesItemThree",
    "ModelingOperationTargetRolesItemTwelve",
    "ModelingOperationTargetRolesItemTwo",
    "ModelingOperationTargetRolesItemZero",
    "MotionClip",
    "MotionClipFormat",
    "MotionClipTracksItem",
    "MotionClipTracksItemKeysItem",
    "MotionClipTracksItemKeysItemSegment",
    "MotionClipTracksItemKeysItemSegmentControl1",
    "MotionClipTracksItemKeysItemSegmentControl1Control1",
    "MotionClipTracksItemKeysItemSegmentControl1Control2",
    "MotionClipTracksItemKeysItemSegmentControl1Kind",
    "MotionClipTracksItemKeysItemSegmentZero",
    "MotionClipTracksItemKeysItemSegmentZeroKind",
    "MotionClipTracksItemKeysItemSegmentZeroKindOne",
    "MotionClipTracksItemKeysItemSegmentZeroKindTwo",
    "MotionClipTracksItemKeysItemSegmentZeroKindZero",
    "MotionRequest",
    "MotionRequestClip",
    "MotionRequestClipAction",
    "MotionRequestClipClip",
    "MotionRequestClipClipFormat",
    "MotionRequestClipClipTracksItem",
    "MotionRequestClipClipTracksItemKeysItem",
    "MotionRequestClipClipTracksItemKeysItemSegment",
    "MotionRequestClipClipTracksItemKeysItemSegmentControl1",
    "MotionRequestClipClipTracksItemKeysItemSegmentControl1Control1",
    "MotionRequestClipClipTracksItemKeysItemSegmentControl1Control2",
    "MotionRequestClipClipTracksItemKeysItemSegmentControl1Kind",
    "MotionRequestClipClipTracksItemKeysItemSegmentZero",
    "MotionRequestClipClipTracksItemKeysItemSegmentZeroKind",
    "MotionRequestClipClipTracksItemKeysItemSegmentZeroKindOne",
    "MotionRequestClipClipTracksItemKeysItemSegmentZeroKindTwo",
    "MotionRequestClipClipTracksItemKeysItemSegmentZeroKindZero",
    "MotionRequestLoop",
    "MotionRequestLoopAction",
    "MotionRequestOne",
    "MotionRequestOneAction",
    "MotionRequestOneActionOne",
    "MotionRequestOneActionThree",
    "MotionRequestOneActionTwo",
    "MotionRequestOneActionZero",
    "MotionRequestTime",
    "MotionRequestTimeAction",
    "PostApiBridgePoseRequest",
    "PostApiBridgePoseRequestClearParameterValues",
    "PostApiBridgePoseRequestClearParameterValuesData",
    "PostApiBridgePoseRequestSetParameterValues",
    "PostApiBridgePoseRequestSetParameterValuesData",
    "PostApiBridgePoseRequestSetParameterValuesDataParametersItem",
    "PostApiBridgePoseRequest_ClearParameterValues",
    "PostApiBridgePoseRequest_SetParameterValues",
    "PostApiBridgeReadRequest",
    "PostApiBridgeReadRequestGetCurrentDocumentUid",
    "PostApiBridgeReadRequestGetCurrentDocumentUidData",
    "PostApiBridgeReadRequestGetCurrentEditMode",
    "PostApiBridgeReadRequestGetCurrentEditModeData",
    "PostApiBridgeReadRequestGetCurrentModelUid",
    "PostApiBridgeReadRequestGetCurrentModelUidData",
    "PostApiBridgeReadRequestGetDeformerStructure",
    "PostApiBridgeReadRequestGetDeformerStructureData",
    "PostApiBridgeReadRequestGetDocument",
    "PostApiBridgeReadRequestGetDocumentData",
    "PostApiBridgeReadRequestGetDocuments",
    "PostApiBridgeReadRequestGetDocumentsData",
    "PostApiBridgeReadRequestGetObject",
    "PostApiBridgeReadRequestGetObjectData",
    "PostApiBridgeReadRequestGetParameterGroups",
    "PostApiBridgeReadRequestGetParameterGroupsData",
    "PostApiBridgeReadRequestGetParameterValues",
    "PostApiBridgeReadRequestGetParameterValuesData",
    "PostApiBridgeReadRequestGetParameters",
    "PostApiBridgeReadRequestGetParametersData",
    "PostApiBridgeReadRequestGetPartStructure",
    "PostApiBridgeReadRequestGetPartStructureData",
    "PostApiBridgeReadRequestGetPhysicsInfo",
    "PostApiBridgeReadRequestGetPhysicsInfoData",
    "PostApiBridgeReadRequest_GetCurrentDocumentUid",
    "PostApiBridgeReadRequest_GetCurrentEditMode",
    "PostApiBridgeReadRequest_GetCurrentModelUid",
    "PostApiBridgeReadRequest_GetDeformerStructure",
    "PostApiBridgeReadRequest_GetDocument",
    "PostApiBridgeReadRequest_GetDocuments",
    "PostApiBridgeReadRequest_GetObject",
    "PostApiBridgeReadRequest_GetParameterGroups",
    "PostApiBridgeReadRequest_GetParameterValues",
    "PostApiBridgeReadRequest_GetParameters",
    "PostApiBridgeReadRequest_GetPartStructure",
    "PostApiBridgeReadRequest_GetPhysicsInfo",
    "PostApiPlaybackControlRequestCommand",
    "PostApiPlaybackControlRequestMode",
    "PostApiPlaybackControlResponse",
    "PostApiPlaybackControlResponsePlayback",
    "PostApiPlaybackControlResponsePlaybackDemo",
    "PostApiPlaybackControlResponsePlaybackDemoMode",
    "PostApiPlaybackControlResponsePlaybackMotion",
    "PostApiPlaybackMotionRequest",
    "PostApiPlaybackMotionRequestClip",
    "PostApiPlaybackMotionRequestClipAction",
    "PostApiPlaybackMotionRequestClipClip",
    "PostApiPlaybackMotionRequestClipClipFormat",
    "PostApiPlaybackMotionRequestClipClipTracksItem",
    "PostApiPlaybackMotionRequestClipClipTracksItemKeysItem",
    "PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegment",
    "PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentControl1",
    "PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentControl1Control1",
    "PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentControl1Control2",
    "PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentControl1Kind",
    "PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentZero",
    "PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentZeroKind",
    "PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentZeroKindOne",
    "PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentZeroKindTwo",
    "PostApiPlaybackMotionRequestClipClipTracksItemKeysItemSegmentZeroKindZero",
    "PostApiPlaybackMotionRequestLoop",
    "PostApiPlaybackMotionRequestLoopAction",
    "PostApiPlaybackMotionRequestOne",
    "PostApiPlaybackMotionRequestOneAction",
    "PostApiPlaybackMotionRequestOneActionOne",
    "PostApiPlaybackMotionRequestOneActionThree",
    "PostApiPlaybackMotionRequestOneActionTwo",
    "PostApiPlaybackMotionRequestOneActionZero",
    "PostApiPlaybackMotionRequestTime",
    "PostApiPlaybackMotionRequestTimeAction",
    "PostApiPlaybackMotionResponse",
    "PostApiPlaybackMotionResponsePlayback",
    "PostApiPlaybackMotionResponsePlaybackDemo",
    "PostApiPlaybackMotionResponsePlaybackDemoMode",
    "PostApiPlaybackMotionResponsePlaybackMotion",
    "PostApiPlaybackParametersResponse",
    "PostApiPlaybackParametersResponsePlayback",
    "PostApiPlaybackParametersResponsePlaybackDemo",
    "PostApiPlaybackParametersResponsePlaybackDemoMode",
    "PostApiPlaybackParametersResponsePlaybackMotion",
    "PostApiPlaybackReloadResponse",
    "PostApiPlaybackReloadResponsePlayback",
    "PostApiPlaybackReloadResponsePlaybackDemo",
    "PostApiPlaybackReloadResponsePlaybackDemoMode",
    "PostApiPlaybackReloadResponsePlaybackMotion",
    "QaCheckRequest",
    "QaCheckRequestMotionSweep",
    "QaCheckRequestMotionSweepCheckMonotonic",
    "QaCheckRequestPoseSamplesItem",
    "TransactionRequest",
    "TransactionRequestCheckpointId",
    "TransactionRequestCheckpointIdKind",
    "TransactionRequestOperations",
    "TransactionRequestOperationsOperationsItem",
    "TransactionRequestOperationsOperationsItemAction",
    "TransactionRequestOperationsOperationsItemActionArtmeshBindingKey",
    "TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyCurve",
    "TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyCurveControlPointsItem",
    "TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyInterpolation",
    "TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyInterpolationFour",
    "TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyInterpolationOne",
    "TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyInterpolationThree",
    "TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyInterpolationTwo",
    "TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyInterpolationZero",
    "TransactionRequestOperationsOperationsItemActionArtmeshBindingKeyOffsetsItem",
    "TransactionRequestOperationsOperationsItemActionArtmeshBlendShape",
    "TransactionRequestOperationsOperationsItemActionArtmeshBlendShapeCurve",
    "TransactionRequestOperationsOperationsItemActionArtmeshBlendShapeCurveControlPointsItem",
    "TransactionRequestOperationsOperationsItemActionArtmeshBlendShapeInterpolation",
    "TransactionRequestOperationsOperationsItemActionArtmeshBlendShapeInterpolationFour",
    "TransactionRequestOperationsOperationsItemActionArtmeshBlendShapeInterpolationOne",
    "TransactionRequestOperationsOperationsItemActionArtmeshBlendShapeInterpolationThree",
    "TransactionRequestOperationsOperationsItemActionArtmeshBlendShapeInterpolationTwo",
    "TransactionRequestOperationsOperationsItemActionArtmeshBlendShapeInterpolationZero",
    "TransactionRequestOperationsOperationsItemActionArtmeshBlendShapeOffsetsItem",
    "TransactionRequestOperationsOperationsItemActionArtmeshGenerate",
    "TransactionRequestOperationsOperationsItemActionArtmeshGeneratePreset",
    "TransactionRequestOperationsOperationsItemActionArtmeshGeneratePresetFive",
    "TransactionRequestOperationsOperationsItemActionArtmeshGeneratePresetFour",
    "TransactionRequestOperationsOperationsItemActionArtmeshGeneratePresetOne",
    "TransactionRequestOperationsOperationsItemActionArtmeshGeneratePresetThree",
    "TransactionRequestOperationsOperationsItemActionArtmeshGeneratePresetTwo",
    "TransactionRequestOperationsOperationsItemActionArtmeshGeneratePresetZero",
    "TransactionRequestOperationsOperationsItemActionArtmeshGenerateQuality",
    "TransactionRequestOperationsOperationsItemActionArtmeshGenerateTopology",
    "TransactionRequestOperationsOperationsItemActionArtmeshGenerateTopologyOne",
    "TransactionRequestOperationsOperationsItemActionArtmeshGenerateTopologyZero",
    "TransactionRequestOperationsOperationsItemActionArtmeshMirrorKey",
    "TransactionRequestOperationsOperationsItemActionArtmeshMirrorKeyCurve",
    "TransactionRequestOperationsOperationsItemActionArtmeshMirrorKeyCurveControlPointsItem",
    "TransactionRequestOperationsOperationsItemActionArtmeshMirrorKeyInterpolation",
    "TransactionRequestOperationsOperationsItemActionArtmeshMirrorKeyInterpolationFour",
    "TransactionRequestOperationsOperationsItemActionArtmeshMirrorKeyInterpolationOne",
    "TransactionRequestOperationsOperationsItemActionArtmeshMirrorKeyInterpolationThree",
    "TransactionRequestOperationsOperationsItemActionArtmeshMirrorKeyInterpolationTwo",
    "TransactionRequestOperationsOperationsItemActionArtmeshMirrorKeyInterpolationZero",
    "TransactionRequestOperationsOperationsItemActionArtmeshMultiKey",
    "TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyCurve",
    "TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyCurveControlPointsItem",
    "TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyInterpolation",
    "TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyInterpolationFour",
    "TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyInterpolationOne",
    "TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyInterpolationThree",
    "TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyInterpolationTwo",
    "TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyInterpolationZero",
    "TransactionRequestOperationsOperationsItemActionArtmeshMultiKeyOffsetsItem",
    "TransactionRequestOperationsOperationsItemActionArtmeshOffset",
    "TransactionRequestOperationsOperationsItemActionArtmeshOffsetUv",
    "TransactionRequestOperationsOperationsItemActionArtmeshQuality",
    "TransactionRequestOperationsOperationsItemActionArtmeshQualityQuality",
    "TransactionRequestOperationsOperationsItemActionArtmeshRebuild",
    "TransactionRequestOperationsOperationsItemActionArtmeshRebuildPreset",
    "TransactionRequestOperationsOperationsItemActionArtmeshRebuildPresetFive",
    "TransactionRequestOperationsOperationsItemActionArtmeshRebuildPresetFour",
    "TransactionRequestOperationsOperationsItemActionArtmeshRebuildPresetOne",
    "TransactionRequestOperationsOperationsItemActionArtmeshRebuildPresetThree",
    "TransactionRequestOperationsOperationsItemActionArtmeshRebuildPresetTwo",
    "TransactionRequestOperationsOperationsItemActionArtmeshRebuildPresetZero",
    "TransactionRequestOperationsOperationsItemActionArtmeshRebuildQuality",
    "TransactionRequestOperationsOperationsItemActionArtmeshRebuildTopology",
    "TransactionRequestOperationsOperationsItemActionArtmeshRebuildTopologyOne",
    "TransactionRequestOperationsOperationsItemActionArtmeshRebuildTopologyZero",
    "TransactionRequestOperationsOperationsItemActionBindingKey",
    "TransactionRequestOperationsOperationsItemActionBindingKeyCurve",
    "TransactionRequestOperationsOperationsItemActionBindingKeyCurveControlPointsItem",
    "TransactionRequestOperationsOperationsItemActionBindingKeyInterpolation",
    "TransactionRequestOperationsOperationsItemActionBindingKeyInterpolationFour",
    "TransactionRequestOperationsOperationsItemActionBindingKeyInterpolationOne",
    "TransactionRequestOperationsOperationsItemActionBindingKeyInterpolationThree",
    "TransactionRequestOperationsOperationsItemActionBindingKeyInterpolationTwo",
    "TransactionRequestOperationsOperationsItemActionBindingKeyInterpolationZero",
    "TransactionRequestOperationsOperationsItemActionBindingKeyProperty",
    "TransactionRequestOperationsOperationsItemActionBindingKeyPropertyFive",
    "TransactionRequestOperationsOperationsItemActionBindingKeyPropertyFour",
    "TransactionRequestOperationsOperationsItemActionBindingKeyPropertyOne",
    "TransactionRequestOperationsOperationsItemActionBindingKeyPropertyThree",
    "TransactionRequestOperationsOperationsItemActionBindingKeyPropertyTwo",
    "TransactionRequestOperationsOperationsItemActionBindingKeyPropertyZero",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSet",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShape",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPath",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathCurve",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathCurveControlPointsItem",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathInterpolation",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathInterpolationFour",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathInterpolationOne",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathInterpolationThree",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathInterpolationTwo",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathInterpolationZero",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeArtPathPointsItem",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformer",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerCurve",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerCurveControlPointsItem",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerInterpolation",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerInterpolationFour",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerInterpolationOne",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerInterpolationThree",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerInterpolationTwo",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerInterpolationZero",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerPinsItem",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerSharedPointsItem",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerTransform",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerWarp",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeGlue",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeGlueCurve",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeGlueCurveControlPointsItem",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeGlueInterpolation",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeGlueInterpolationFour",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeGlueInterpolationOne",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeGlueInterpolationThree",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeGlueInterpolationTwo",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeGlueInterpolationZero",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePart",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartCurve",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartCurveControlPointsItem",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartInterpolation",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartInterpolationFour",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartInterpolationOne",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartInterpolationThree",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartInterpolationTwo",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartInterpolationZero",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShapePartTransform",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShape_ArtPath",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShape_Deformer",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShape_Glue",
    "TransactionRequestOperationsOperationsItemActionBlendShapeSetShape_Part",
    "TransactionRequestOperationsOperationsItemActionDeformBrush",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrush",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestination",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBase",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShape",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShapeShape",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShapeShapeCurve",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShapeShapeCurveControlPointsItem",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShapeShapeInterpolation",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShapeShapeInterpolationFour",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShapeShapeInterpolationOne",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShapeShapeInterpolationThree",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShapeShapeInterpolationTwo",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShapeShapeInterpolationZero",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationKeyform",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestination_Base",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestination_BlendShape",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestination_Keyform",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffect",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffectBend",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffectContourFollow",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffectInflate",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffectPinch",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffectRelax",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffectSmooth",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffect_Bend",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffect_ContourFollow",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffect_Inflate",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffect_Pinch",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffect_Relax",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffect_Smooth",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushFalloff",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushFalloffOne",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushFalloffZero",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurface",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurfaceArtmesh",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurfaceArtmeshSpace",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurfaceSharedWarp",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurfaceSharedWarpSpace",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurfaceWarpPins",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurfaceWarpPinsSpace",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurface_Artmesh",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurface_SharedWarp",
    "TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurface_WarpPins",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKey",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyCurve",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyCurveControlPointsItem",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyInterpolation",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyInterpolationFour",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyInterpolationOne",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyInterpolationThree",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyInterpolationTwo",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyInterpolationZero",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyProperty",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertyEight",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertyFive",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertyFour",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertyNine",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertyOne",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertySeven",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertySix",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertyThree",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertyTwo",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingKeyPropertyZero",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingRemove",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingRemoveProperty",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingRemovePropertyEight",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingRemovePropertyFive",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingRemovePropertyFour",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingRemovePropertyNine",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingRemovePropertyOne",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingRemovePropertySeven",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingRemovePropertySix",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingRemovePropertyThree",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingRemovePropertyTwo",
    "TransactionRequestOperationsOperationsItemActionDeformerBindingRemovePropertyZero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreate",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformer",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItem",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemComposition",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemCompositionOne",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemCompositionZero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemCurve",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemCurveControlPointsItem",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemInterpolation",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemInterpolationFour",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemInterpolationOne",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemInterpolationThree",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemInterpolationTwo",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemInterpolationZero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemKeysItem",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemProperty",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemPropertyEight",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemPropertyFive",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemPropertyFour",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemPropertyNine",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemPropertyOne",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemPropertySeven",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemPropertySix",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemPropertyThree",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemPropertyTwo",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItemPropertyZero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItem",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemCurve",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemCurveControlPointsItem",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemInterpolation",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemInterpolationFour",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemInterpolationOne",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemInterpolationThree",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemInterpolationTwo",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemInterpolationZero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemKind",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemPinsItem",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemSharedPointsItem",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemTransform",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemWarp",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerKind",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerKindOne",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerKindTwo",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerKindZero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItem",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemComposition",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemCompositionOne",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemCompositionZero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemCurve",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemCurveControlPointsItem",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemInterpolation",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemInterpolationFour",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemInterpolationOne",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemInterpolationThree",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemInterpolationTwo",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemInterpolationZero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemKeyformsItem",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemProperty",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertyEight",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertyEleven",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertyFive",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertyFour",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertyNine",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertyOne",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertySeven",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertySix",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertyTen",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertyThree",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertyTwo",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItemPropertyZero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerOrigin",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadata",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataAngleRange",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataAngleUnit",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataParentComposition",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataParentCompositionOne",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataParentCompositionZero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataPivot",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataPivotSpace",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataPivotSpaceOne",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataPivotSpaceZero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataShapePreservation",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataShapePreservationOne",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataShapePreservationTwo",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataShapePreservationZero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarp",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpBounds",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItem",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItem",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemCurve",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemCurveControlPointsItem",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolation",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolationFour",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolationOne",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolationThree",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolationTwo",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemInterpolationZero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemKeysItem",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemProperty",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemPropertyOne",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemPropertyZero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarpGrid",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerTransform",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarp",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpGrid",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinBlendMode",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinBlendModeOne",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinBlendModeZero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItem",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItem",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemCurve",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemCurveControlPointsItem",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolation",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolationFour",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolationOne",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolationThree",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolationTwo",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemInterpolationZero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemKeysItem",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemProperty",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemPropertyOne",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemBindingsItemPropertyZero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItem",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemCurve",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemCurveControlPointsItem",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolation",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolationFour",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolationOne",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolationThree",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolationTwo",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemInterpolationZero",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemKeyformsItem",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemProperty",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemPropertyOne",
    "TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarpPinsItemMultiBindingsItemPropertyZero",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSet",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetKind",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetKindOne",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetKindTwo",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetKindZero",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarp",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpGrid",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinBlendMode",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinBlendModeOne",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinBlendModeZero",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItem",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItem",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemCurve",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemCurveControlPointsItem",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemInterpolation",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemInterpolationFour",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemInterpolationOne",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemInterpolationThree",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemInterpolationTwo",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemInterpolationZero",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemKeysItem",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemProperty",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemPropertyOne",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemBindingsItemPropertyZero",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItem",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemCurve",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemCurveControlPointsItem",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolation",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolationFour",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolationOne",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolationThree",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolationTwo",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemInterpolationZero",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemKeyformsItem",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemProperty",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemPropertyOne",
    "TransactionRequestOperationsOperationsItemActionDeformerKindSetWarpPinsItemMultiBindingsItemPropertyZero",
    "TransactionRequestOperationsOperationsItemActionDeformerOrigin",
    "TransactionRequestOperationsOperationsItemActionDeformerParentSet",
    "TransactionRequestOperationsOperationsItemActionDeformerRotationMetadata",
    "TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadata",
    "TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataAngleRange",
    "TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataAngleUnit",
    "TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataParentComposition",
    "TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataParentCompositionOne",
    "TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataParentCompositionZero",
    "TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataPivot",
    "TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataPivotSpace",
    "TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataPivotSpaceOne",
    "TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataPivotSpaceZero",
    "TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataShapePreservation",
    "TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataShapePreservationOne",
    "TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataShapePreservationTwo",
    "TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataShapePreservationZero",
    "TransactionRequestOperationsOperationsItemActionDeformerSplit",
    "TransactionRequestOperationsOperationsItemActionDeformerTargetsSet",
    "TransactionRequestOperationsOperationsItemActionDeformerTargetsSetMode",
    "TransactionRequestOperationsOperationsItemActionDeformerTargetsSetModeOne",
    "TransactionRequestOperationsOperationsItemActionDeformerTargetsSetModeZero",
    "TransactionRequestOperationsOperationsItemActionDeformerTransform",
    "TransactionRequestOperationsOperationsItemActionDeformerTransformOperator",
    "TransactionRequestOperationsOperationsItemActionDeformerTransformOperatorOne",
    "TransactionRequestOperationsOperationsItemActionDeformerTransformOperatorTwo",
    "TransactionRequestOperationsOperationsItemActionDeformerTransformOperatorZero",
    "TransactionRequestOperationsOperationsItemActionDeformerTransformProperty",
    "TransactionRequestOperationsOperationsItemActionDeformerTransformPropertyFive",
    "TransactionRequestOperationsOperationsItemActionDeformerTransformPropertyFour",
    "TransactionRequestOperationsOperationsItemActionDeformerTransformPropertyOne",
    "TransactionRequestOperationsOperationsItemActionDeformerTransformPropertyThree",
    "TransactionRequestOperationsOperationsItemActionDeformerTransformPropertyTwo",
    "TransactionRequestOperationsOperationsItemActionDeformerTransformPropertyZero",
    "TransactionRequestOperationsOperationsItemActionParameterAdd",
    "TransactionRequestOperationsOperationsItemActionParameterAddParameter",
    "TransactionRequestOperationsOperationsItemActionPartAlphaReveal",
    "TransactionRequestOperationsOperationsItemActionPartAlphaRevealReveal",
    "TransactionRequestOperationsOperationsItemActionPartBlendMode",
    "TransactionRequestOperationsOperationsItemActionPartBlendModeMode",
    "TransactionRequestOperationsOperationsItemActionPartBlendModeModeOne",
    "TransactionRequestOperationsOperationsItemActionPartBlendModeModeThree",
    "TransactionRequestOperationsOperationsItemActionPartBlendModeModeTwo",
    "TransactionRequestOperationsOperationsItemActionPartBlendModeModeZero",
    "TransactionRequestOperationsOperationsItemActionPartClip",
    "TransactionRequestOperationsOperationsItemActionPartClipClip",
    "TransactionRequestOperationsOperationsItemActionPartClipClipMaskOpacity",
    "TransactionRequestOperationsOperationsItemActionPartClipClipMaskOpacityOne",
    "TransactionRequestOperationsOperationsItemActionPartClipClipMaskOpacityZero",
    "TransactionRequestOperationsOperationsItemActionPartClipClipMode",
    "TransactionRequestOperationsOperationsItemActionPartContourShade",
    "TransactionRequestOperationsOperationsItemActionPartContourShadeShade",
    "TransactionRequestOperationsOperationsItemActionPartContourShadeShadeProfile",
    "TransactionRequestOperationsOperationsItemActionPartDrawOrder",
    "TransactionRequestOperationsOperationsItemActionPartTint",
    "TransactionRequestOperationsOperationsItemActionPartTintTint",
    "TransactionRequestOperationsOperationsItemActionPartTintTintMode",
    "TransactionRequestOperationsOperationsItemActionPartTintTintModeOne",
    "TransactionRequestOperationsOperationsItemActionPartTintTintModeZero",
    "TransactionRequestOperationsOperationsItemActionPartVisibility",
    "TransactionRequestOperationsOperationsItemActionRoleConfirm",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRole",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleEight",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleEleven",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleFifteen",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleFive",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleFour",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleFourteen",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleNine",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleOne",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleSeven",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleSeventeen",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleSix",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleSixteen",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleTen",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleThirteen",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleThree",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleTwelve",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleTwo",
    "TransactionRequestOperationsOperationsItemActionRoleConfirmRoleZero",
    "TransactionRequestOperationsOperationsItemActionRoleReclassify",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRole",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleEight",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleEleven",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleFifteen",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleFive",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleFour",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleFourteen",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleNine",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleOne",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleSeven",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleSeventeen",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleSix",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleSixteen",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleTen",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleThirteen",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleThree",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleTwelve",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleTwo",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyExpectedRoleZero",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRole",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleEight",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleEleven",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleFifteen",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleFive",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleFour",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleFourteen",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleNine",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleOne",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleSeven",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleSeventeen",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleSix",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleSixteen",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleTen",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleThirteen",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleThree",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleTwelve",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleTwo",
    "TransactionRequestOperationsOperationsItemActionRoleReclassifyRoleZero",
    "TransactionRequestOperationsOperationsItemActionSymmetryArtmeshBindings",
    "TransactionRequestOperationsOperationsItemActionSymmetryArtmeshBindingsLinksItem",
    "TransactionRequestOperationsOperationsItemActionSymmetryArtmeshBindingsLinksItemAxis",
    "TransactionRequestOperationsOperationsItemActionSymmetryArtmeshBindingsLinksItemKind",
    "TransactionRequestOperationsOperationsItemActionSymmetryArtmeshBindingsLinksItemKindOne",
    "TransactionRequestOperationsOperationsItemActionSymmetryArtmeshBindingsLinksItemKindThree",
    "TransactionRequestOperationsOperationsItemActionSymmetryArtmeshBindingsLinksItemKindTwo",
    "TransactionRequestOperationsOperationsItemActionSymmetryArtmeshBindingsLinksItemKindZero",
    "TransactionRequestOperationsOperationsItemActionSymmetryContract",
    "TransactionRequestOperationsOperationsItemActionSymmetryContractContract",
    "TransactionRequestOperationsOperationsItemActionSymmetryContractContractAxis",
    "TransactionRequestOperationsOperationsItemActionSymmetryContractContractLinksItem",
    "TransactionRequestOperationsOperationsItemActionSymmetryContractContractLinksItemAxis",
    "TransactionRequestOperationsOperationsItemActionSymmetryContractContractLinksItemKind",
    "TransactionRequestOperationsOperationsItemActionSymmetryContractContractLinksItemKindOne",
    "TransactionRequestOperationsOperationsItemActionSymmetryContractContractLinksItemKindThree",
    "TransactionRequestOperationsOperationsItemActionSymmetryContractContractLinksItemKindTwo",
    "TransactionRequestOperationsOperationsItemActionSymmetryContractContractLinksItemKindZero",
    "TransactionRequestOperationsOperationsItemActionTransform",
    "TransactionRequestOperationsOperationsItemActionTransformOperator",
    "TransactionRequestOperationsOperationsItemActionTransformOperatorOne",
    "TransactionRequestOperationsOperationsItemActionTransformOperatorTwo",
    "TransactionRequestOperationsOperationsItemActionTransformOperatorZero",
    "TransactionRequestOperationsOperationsItemActionTransformProperty",
    "TransactionRequestOperationsOperationsItemActionTransformPropertyFive",
    "TransactionRequestOperationsOperationsItemActionTransformPropertyFour",
    "TransactionRequestOperationsOperationsItemActionTransformPropertyOne",
    "TransactionRequestOperationsOperationsItemActionTransformPropertyThree",
    "TransactionRequestOperationsOperationsItemActionTransformPropertyTwo",
    "TransactionRequestOperationsOperationsItemActionTransformPropertyZero",
    "TransactionRequestOperationsOperationsItemActionWarpPinBindingKey",
    "TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyCurve",
    "TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyCurveControlPointsItem",
    "TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyInterpolation",
    "TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyInterpolationFour",
    "TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyInterpolationOne",
    "TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyInterpolationThree",
    "TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyInterpolationTwo",
    "TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyInterpolationZero",
    "TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyProperty",
    "TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyPropertyOne",
    "TransactionRequestOperationsOperationsItemActionWarpPinBindingKeyPropertyZero",
    "TransactionRequestOperationsOperationsItemAction_ArtmeshBindingKey",
    "TransactionRequestOperationsOperationsItemAction_ArtmeshBlendShape",
    "TransactionRequestOperationsOperationsItemAction_ArtmeshGenerate",
    "TransactionRequestOperationsOperationsItemAction_ArtmeshMirrorKey",
    "TransactionRequestOperationsOperationsItemAction_ArtmeshMultiKey",
    "TransactionRequestOperationsOperationsItemAction_ArtmeshOffset",
    "TransactionRequestOperationsOperationsItemAction_ArtmeshQuality",
    "TransactionRequestOperationsOperationsItemAction_ArtmeshRebuild",
    "TransactionRequestOperationsOperationsItemAction_BindingKey",
    "TransactionRequestOperationsOperationsItemAction_BlendShapeSet",
    "TransactionRequestOperationsOperationsItemAction_DeformBrush",
    "TransactionRequestOperationsOperationsItemAction_DeformerBindingKey",
    "TransactionRequestOperationsOperationsItemAction_DeformerBindingRemove",
    "TransactionRequestOperationsOperationsItemAction_DeformerCreate",
    "TransactionRequestOperationsOperationsItemAction_DeformerKindSet",
    "TransactionRequestOperationsOperationsItemAction_DeformerOrigin",
    "TransactionRequestOperationsOperationsItemAction_DeformerParentSet",
    "TransactionRequestOperationsOperationsItemAction_DeformerRotationMetadata",
    "TransactionRequestOperationsOperationsItemAction_DeformerSplit",
    "TransactionRequestOperationsOperationsItemAction_DeformerTargetsSet",
    "TransactionRequestOperationsOperationsItemAction_DeformerTransform",
    "TransactionRequestOperationsOperationsItemAction_ParameterAdd",
    "TransactionRequestOperationsOperationsItemAction_PartAlphaReveal",
    "TransactionRequestOperationsOperationsItemAction_PartBlendMode",
    "TransactionRequestOperationsOperationsItemAction_PartClip",
    "TransactionRequestOperationsOperationsItemAction_PartContourShade",
    "TransactionRequestOperationsOperationsItemAction_PartDrawOrder",
    "TransactionRequestOperationsOperationsItemAction_PartTint",
    "TransactionRequestOperationsOperationsItemAction_PartVisibility",
    "TransactionRequestOperationsOperationsItemAction_RoleConfirm",
    "TransactionRequestOperationsOperationsItemAction_RoleReclassify",
    "TransactionRequestOperationsOperationsItemAction_SymmetryArtmeshBindings",
    "TransactionRequestOperationsOperationsItemAction_SymmetryContract",
    "TransactionRequestOperationsOperationsItemAction_Transform",
    "TransactionRequestOperationsOperationsItemAction_WarpPinBindingKey",
    "TransactionRequestOperationsOperationsItemTarget",
    "TransactionRequestOperationsOperationsItemTargetRolesItem",
    "TransactionRequestOperationsOperationsItemTargetRolesItemEight",
    "TransactionRequestOperationsOperationsItemTargetRolesItemEleven",
    "TransactionRequestOperationsOperationsItemTargetRolesItemFifteen",
    "TransactionRequestOperationsOperationsItemTargetRolesItemFive",
    "TransactionRequestOperationsOperationsItemTargetRolesItemFour",
    "TransactionRequestOperationsOperationsItemTargetRolesItemFourteen",
    "TransactionRequestOperationsOperationsItemTargetRolesItemNine",
    "TransactionRequestOperationsOperationsItemTargetRolesItemOne",
    "TransactionRequestOperationsOperationsItemTargetRolesItemSeven",
    "TransactionRequestOperationsOperationsItemTargetRolesItemSeventeen",
    "TransactionRequestOperationsOperationsItemTargetRolesItemSix",
    "TransactionRequestOperationsOperationsItemTargetRolesItemSixteen",
    "TransactionRequestOperationsOperationsItemTargetRolesItemTen",
    "TransactionRequestOperationsOperationsItemTargetRolesItemThirteen",
    "TransactionRequestOperationsOperationsItemTargetRolesItemThree",
    "TransactionRequestOperationsOperationsItemTargetRolesItemTwelve",
    "TransactionRequestOperationsOperationsItemTargetRolesItemTwo",
    "TransactionRequestOperationsOperationsItemTargetRolesItemZero",
    "TransactionRequestOperationsQa",
    "TransactionRequestOperationsQaMotionSweep",
    "TransactionRequestOperationsQaMotionSweepCheckMonotonic",
    "TransactionRequestOperationsQaPoseSamplesItem",
    "TransactionRequestRig",
    "TransactionRequestRigKind",
]
