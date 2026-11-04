



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .a import A
    from .all_null import AllNull
    from .b import B
    from .base import Base
    from .composed_default_container import ComposedDefaultContainer
    from .conditional_annotation_isolation import ConditionalAnnotationIsolation
    from .deduplicated_ref_container import DeduplicatedRefContainer
    from .deduplicated_ref_container_inner import DeduplicatedRefContainerInner
    from .default_custom_voice import DefaultCustomVoice
    from .default_voice import DefaultVoice
    from .default_voice_ids import DefaultVoiceIds
    from .default_voice_ids_one import DefaultVoiceIdsOne
    from .default_voice_ids_zero import DefaultVoiceIdsZero
    from .dependent_annotation_isolation import DependentAnnotationIsolation
    from .duplicate_null import DuplicateNull
    from .fallback import Fallback, Fallback_A, Fallback_B
    from .mixed import Mixed, Mixed_A, Mixed_B
    from .mixed_primitive_enum import MixedPrimitiveEnum
    from .model_branch_null_default import ModelBranchNullDefault
    from .nested_union_one import NestedUnionOne
    from .non_ascii_pattern import NonAsciiPattern
    from .null_drift_event import NullDriftEvent, NullDriftEvent_Other, NullDriftEvent_ResponseCompleted
    from .null_drift_event_other import NullDriftEventOther
    from .null_drift_event_response_completed import NullDriftEventResponseCompleted
    from .null_drift_response import NullDriftResponse
    from .nullable_enum_box import NullableEnumBox
    from .nullable_enum_box_optional_enum import NullableEnumBoxOptionalEnum
    from .nullable_enum_box_required_enum import NullableEnumBoxRequiredEnum
    from .outer_union import OuterUnion
    from .ref_annotation_isolation import RefAnnotationIsolation
    from .ref_annotation_target import RefAnnotationTarget
    from .ref_sibling_composition import RefSiblingComposition
    from .ref_sibling_target import RefSiblingTarget
    from .representation_checks import RepresentationChecks
    from .scalar_defaults import ScalarDefaults
    from .scalar_defaults_mode import ScalarDefaultsMode
    from .simple import Simple
    from .stream_chunk import StreamChunk
    from .stream_chunk_inline_nullable import StreamChunkInlineNullable
    from .tagged_union_container import TaggedUnionContainer
    from .toggle import Toggle
    from .unevaluated_all_of import UnevaluatedAllOf
    from .unevaluated_items_only import UnevaluatedItemsOnly
    from .validation_vocabulary_inert_unique import ValidationVocabularyInertUnique
    from .zeta import Zeta
_dynamic_imports: typing.Dict[str, str] = {
    "A": ".a",
    "AllNull": ".all_null",
    "B": ".b",
    "Base": ".base",
    "ComposedDefaultContainer": ".composed_default_container",
    "ConditionalAnnotationIsolation": ".conditional_annotation_isolation",
    "DeduplicatedRefContainer": ".deduplicated_ref_container",
    "DeduplicatedRefContainerInner": ".deduplicated_ref_container_inner",
    "DefaultCustomVoice": ".default_custom_voice",
    "DefaultVoice": ".default_voice",
    "DefaultVoiceIds": ".default_voice_ids",
    "DefaultVoiceIdsOne": ".default_voice_ids_one",
    "DefaultVoiceIdsZero": ".default_voice_ids_zero",
    "DependentAnnotationIsolation": ".dependent_annotation_isolation",
    "DuplicateNull": ".duplicate_null",
    "Fallback": ".fallback",
    "Fallback_A": ".fallback",
    "Fallback_B": ".fallback",
    "Mixed": ".mixed",
    "MixedPrimitiveEnum": ".mixed_primitive_enum",
    "Mixed_A": ".mixed",
    "Mixed_B": ".mixed",
    "ModelBranchNullDefault": ".model_branch_null_default",
    "NestedUnionOne": ".nested_union_one",
    "NonAsciiPattern": ".non_ascii_pattern",
    "NullDriftEvent": ".null_drift_event",
    "NullDriftEventOther": ".null_drift_event_other",
    "NullDriftEventResponseCompleted": ".null_drift_event_response_completed",
    "NullDriftEvent_Other": ".null_drift_event",
    "NullDriftEvent_ResponseCompleted": ".null_drift_event",
    "NullDriftResponse": ".null_drift_response",
    "NullableEnumBox": ".nullable_enum_box",
    "NullableEnumBoxOptionalEnum": ".nullable_enum_box_optional_enum",
    "NullableEnumBoxRequiredEnum": ".nullable_enum_box_required_enum",
    "OuterUnion": ".outer_union",
    "RefAnnotationIsolation": ".ref_annotation_isolation",
    "RefAnnotationTarget": ".ref_annotation_target",
    "RefSiblingComposition": ".ref_sibling_composition",
    "RefSiblingTarget": ".ref_sibling_target",
    "RepresentationChecks": ".representation_checks",
    "ScalarDefaults": ".scalar_defaults",
    "ScalarDefaultsMode": ".scalar_defaults_mode",
    "Simple": ".simple",
    "StreamChunk": ".stream_chunk",
    "StreamChunkInlineNullable": ".stream_chunk_inline_nullable",
    "TaggedUnionContainer": ".tagged_union_container",
    "Toggle": ".toggle",
    "UnevaluatedAllOf": ".unevaluated_all_of",
    "UnevaluatedItemsOnly": ".unevaluated_items_only",
    "ValidationVocabularyInertUnique": ".validation_vocabulary_inert_unique",
    "Zeta": ".zeta",
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
    "A",
    "AllNull",
    "B",
    "Base",
    "ComposedDefaultContainer",
    "ConditionalAnnotationIsolation",
    "DeduplicatedRefContainer",
    "DeduplicatedRefContainerInner",
    "DefaultCustomVoice",
    "DefaultVoice",
    "DefaultVoiceIds",
    "DefaultVoiceIdsOne",
    "DefaultVoiceIdsZero",
    "DependentAnnotationIsolation",
    "DuplicateNull",
    "Fallback",
    "Fallback_A",
    "Fallback_B",
    "Mixed",
    "MixedPrimitiveEnum",
    "Mixed_A",
    "Mixed_B",
    "ModelBranchNullDefault",
    "NestedUnionOne",
    "NonAsciiPattern",
    "NullDriftEvent",
    "NullDriftEventOther",
    "NullDriftEventResponseCompleted",
    "NullDriftEvent_Other",
    "NullDriftEvent_ResponseCompleted",
    "NullDriftResponse",
    "NullableEnumBox",
    "NullableEnumBoxOptionalEnum",
    "NullableEnumBoxRequiredEnum",
    "OuterUnion",
    "RefAnnotationIsolation",
    "RefAnnotationTarget",
    "RefSiblingComposition",
    "RefSiblingTarget",
    "RepresentationChecks",
    "ScalarDefaults",
    "ScalarDefaultsMode",
    "Simple",
    "StreamChunk",
    "StreamChunkInlineNullable",
    "TaggedUnionContainer",
    "Toggle",
    "UnevaluatedAllOf",
    "UnevaluatedItemsOnly",
    "ValidationVocabularyInertUnique",
    "Zeta",
]
