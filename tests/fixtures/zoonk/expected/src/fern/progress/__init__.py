



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        LessonCompletionRequestAnswersValue,
        LessonCompletionRequestAnswersValueFillBlank,
        LessonCompletionRequestAnswersValueListening,
        LessonCompletionRequestAnswersValueMatchColumns,
        LessonCompletionRequestAnswersValueMatchColumnsUserPairsItem,
        LessonCompletionRequestAnswersValueMultipleChoice,
        LessonCompletionRequestAnswersValueReading,
        LessonCompletionRequestAnswersValueSelectImage,
        LessonCompletionRequestAnswersValueSortOrder,
        LessonCompletionRequestAnswersValueTranslation,
        LessonCompletionRequestAnswersValue_FillBlank,
        LessonCompletionRequestAnswersValue_Listening,
        LessonCompletionRequestAnswersValue_MatchColumns,
        LessonCompletionRequestAnswersValue_MultipleChoice,
        LessonCompletionRequestAnswersValue_Reading,
        LessonCompletionRequestAnswersValue_SelectImage,
        LessonCompletionRequestAnswersValue_SortOrder,
        LessonCompletionRequestAnswersValue_Translation,
        LessonCompletionRequestStepTimingsValue,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "LessonCompletionRequestAnswersValue": ".types",
    "LessonCompletionRequestAnswersValueFillBlank": ".types",
    "LessonCompletionRequestAnswersValueListening": ".types",
    "LessonCompletionRequestAnswersValueMatchColumns": ".types",
    "LessonCompletionRequestAnswersValueMatchColumnsUserPairsItem": ".types",
    "LessonCompletionRequestAnswersValueMultipleChoice": ".types",
    "LessonCompletionRequestAnswersValueReading": ".types",
    "LessonCompletionRequestAnswersValueSelectImage": ".types",
    "LessonCompletionRequestAnswersValueSortOrder": ".types",
    "LessonCompletionRequestAnswersValueTranslation": ".types",
    "LessonCompletionRequestAnswersValue_FillBlank": ".types",
    "LessonCompletionRequestAnswersValue_Listening": ".types",
    "LessonCompletionRequestAnswersValue_MatchColumns": ".types",
    "LessonCompletionRequestAnswersValue_MultipleChoice": ".types",
    "LessonCompletionRequestAnswersValue_Reading": ".types",
    "LessonCompletionRequestAnswersValue_SelectImage": ".types",
    "LessonCompletionRequestAnswersValue_SortOrder": ".types",
    "LessonCompletionRequestAnswersValue_Translation": ".types",
    "LessonCompletionRequestStepTimingsValue": ".types",
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
    "LessonCompletionRequestAnswersValue",
    "LessonCompletionRequestAnswersValueFillBlank",
    "LessonCompletionRequestAnswersValueListening",
    "LessonCompletionRequestAnswersValueMatchColumns",
    "LessonCompletionRequestAnswersValueMatchColumnsUserPairsItem",
    "LessonCompletionRequestAnswersValueMultipleChoice",
    "LessonCompletionRequestAnswersValueReading",
    "LessonCompletionRequestAnswersValueSelectImage",
    "LessonCompletionRequestAnswersValueSortOrder",
    "LessonCompletionRequestAnswersValueTranslation",
    "LessonCompletionRequestAnswersValue_FillBlank",
    "LessonCompletionRequestAnswersValue_Listening",
    "LessonCompletionRequestAnswersValue_MatchColumns",
    "LessonCompletionRequestAnswersValue_MultipleChoice",
    "LessonCompletionRequestAnswersValue_Reading",
    "LessonCompletionRequestAnswersValue_SelectImage",
    "LessonCompletionRequestAnswersValue_SortOrder",
    "LessonCompletionRequestAnswersValue_Translation",
    "LessonCompletionRequestStepTimingsValue",
]
