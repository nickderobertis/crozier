



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        A,
        AllNull,
        B,
        Base,
        ComposedDefaultContainer,
        ConditionalAnnotationIsolation,
        DeduplicatedRefContainer,
        DeduplicatedRefContainerInner,
        DefaultCustomVoice,
        DefaultVoice,
        DefaultVoiceIds,
        DefaultVoiceIdsOne,
        DefaultVoiceIdsZero,
        DependentAnnotationIsolation,
        DuplicateNull,
        Fallback,
        Fallback_A,
        Fallback_B,
        Mixed,
        MixedPrimitiveEnum,
        Mixed_A,
        Mixed_B,
        ModelBranchNullDefault,
        NestedUnionOne,
        NonAsciiPattern,
        NullDriftEvent,
        NullDriftEventOther,
        NullDriftEventResponseCompleted,
        NullDriftEvent_Other,
        NullDriftEvent_ResponseCompleted,
        NullDriftResponse,
        NullableEnumBox,
        NullableEnumBoxOptionalEnum,
        NullableEnumBoxRequiredEnum,
        OuterUnion,
        RefAnnotationIsolation,
        RefAnnotationTarget,
        RefSiblingComposition,
        RefSiblingTarget,
        RepresentationChecks,
        ScalarDefaults,
        ScalarDefaultsMode,
        Simple,
        StreamChunk,
        StreamChunkInlineNullable,
        TaggedUnionContainer,
        Toggle,
        UnevaluatedAllOf,
        UnevaluatedItemsOnly,
        ValidationVocabularyInertUnique,
        Zeta,
    )
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "A": ".types",
    "AllNull": ".types",
    "AsyncFernApi": ".client",
    "B": ".types",
    "Base": ".types",
    "ComposedDefaultContainer": ".types",
    "ConditionalAnnotationIsolation": ".types",
    "DeduplicatedRefContainer": ".types",
    "DeduplicatedRefContainerInner": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "DefaultCustomVoice": ".types",
    "DefaultVoice": ".types",
    "DefaultVoiceIds": ".types",
    "DefaultVoiceIdsOne": ".types",
    "DefaultVoiceIdsZero": ".types",
    "DependentAnnotationIsolation": ".types",
    "DuplicateNull": ".types",
    "Fallback": ".types",
    "Fallback_A": ".types",
    "Fallback_B": ".types",
    "FernApi": ".client",
    "Mixed": ".types",
    "MixedPrimitiveEnum": ".types",
    "Mixed_A": ".types",
    "Mixed_B": ".types",
    "ModelBranchNullDefault": ".types",
    "NestedUnionOne": ".types",
    "NonAsciiPattern": ".types",
    "NullDriftEvent": ".types",
    "NullDriftEventOther": ".types",
    "NullDriftEventResponseCompleted": ".types",
    "NullDriftEvent_Other": ".types",
    "NullDriftEvent_ResponseCompleted": ".types",
    "NullDriftResponse": ".types",
    "NullableEnumBox": ".types",
    "NullableEnumBoxOptionalEnum": ".types",
    "NullableEnumBoxRequiredEnum": ".types",
    "OuterUnion": ".types",
    "RefAnnotationIsolation": ".types",
    "RefAnnotationTarget": ".types",
    "RefSiblingComposition": ".types",
    "RefSiblingTarget": ".types",
    "RepresentationChecks": ".types",
    "ScalarDefaults": ".types",
    "ScalarDefaultsMode": ".types",
    "Simple": ".types",
    "StreamChunk": ".types",
    "StreamChunkInlineNullable": ".types",
    "TaggedUnionContainer": ".types",
    "Toggle": ".types",
    "UnevaluatedAllOf": ".types",
    "UnevaluatedItemsOnly": ".types",
    "ValidationVocabularyInertUnique": ".types",
    "Zeta": ".types",
    "__version__": ".version",
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
    "AsyncFernApi",
    "B",
    "Base",
    "ComposedDefaultContainer",
    "ConditionalAnnotationIsolation",
    "DeduplicatedRefContainer",
    "DeduplicatedRefContainerInner",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
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
    "FernApi",
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
    "__version__",
]
