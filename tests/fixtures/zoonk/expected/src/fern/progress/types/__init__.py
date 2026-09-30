



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .lesson_completion_request_answers_value import (
        LessonCompletionRequestAnswersValue,
        LessonCompletionRequestAnswersValue_FillBlank,
        LessonCompletionRequestAnswersValue_Listening,
        LessonCompletionRequestAnswersValue_MatchColumns,
        LessonCompletionRequestAnswersValue_MultipleChoice,
        LessonCompletionRequestAnswersValue_Reading,
        LessonCompletionRequestAnswersValue_SelectImage,
        LessonCompletionRequestAnswersValue_SortOrder,
        LessonCompletionRequestAnswersValue_Translation,
    )
    from .lesson_completion_request_answers_value_fill_blank import LessonCompletionRequestAnswersValueFillBlank
    from .lesson_completion_request_answers_value_listening import LessonCompletionRequestAnswersValueListening
    from .lesson_completion_request_answers_value_match_columns import LessonCompletionRequestAnswersValueMatchColumns
    from .lesson_completion_request_answers_value_match_columns_user_pairs_item import (
        LessonCompletionRequestAnswersValueMatchColumnsUserPairsItem,
    )
    from .lesson_completion_request_answers_value_multiple_choice import (
        LessonCompletionRequestAnswersValueMultipleChoice,
    )
    from .lesson_completion_request_answers_value_reading import LessonCompletionRequestAnswersValueReading
    from .lesson_completion_request_answers_value_select_image import LessonCompletionRequestAnswersValueSelectImage
    from .lesson_completion_request_answers_value_sort_order import LessonCompletionRequestAnswersValueSortOrder
    from .lesson_completion_request_answers_value_translation import LessonCompletionRequestAnswersValueTranslation
    from .lesson_completion_request_step_timings_value import LessonCompletionRequestStepTimingsValue
_dynamic_imports: typing.Dict[str, str] = {
    "LessonCompletionRequestAnswersValue": ".lesson_completion_request_answers_value",
    "LessonCompletionRequestAnswersValueFillBlank": ".lesson_completion_request_answers_value_fill_blank",
    "LessonCompletionRequestAnswersValueListening": ".lesson_completion_request_answers_value_listening",
    "LessonCompletionRequestAnswersValueMatchColumns": ".lesson_completion_request_answers_value_match_columns",
    "LessonCompletionRequestAnswersValueMatchColumnsUserPairsItem": ".lesson_completion_request_answers_value_match_columns_user_pairs_item",
    "LessonCompletionRequestAnswersValueMultipleChoice": ".lesson_completion_request_answers_value_multiple_choice",
    "LessonCompletionRequestAnswersValueReading": ".lesson_completion_request_answers_value_reading",
    "LessonCompletionRequestAnswersValueSelectImage": ".lesson_completion_request_answers_value_select_image",
    "LessonCompletionRequestAnswersValueSortOrder": ".lesson_completion_request_answers_value_sort_order",
    "LessonCompletionRequestAnswersValueTranslation": ".lesson_completion_request_answers_value_translation",
    "LessonCompletionRequestAnswersValue_FillBlank": ".lesson_completion_request_answers_value",
    "LessonCompletionRequestAnswersValue_Listening": ".lesson_completion_request_answers_value",
    "LessonCompletionRequestAnswersValue_MatchColumns": ".lesson_completion_request_answers_value",
    "LessonCompletionRequestAnswersValue_MultipleChoice": ".lesson_completion_request_answers_value",
    "LessonCompletionRequestAnswersValue_Reading": ".lesson_completion_request_answers_value",
    "LessonCompletionRequestAnswersValue_SelectImage": ".lesson_completion_request_answers_value",
    "LessonCompletionRequestAnswersValue_SortOrder": ".lesson_completion_request_answers_value",
    "LessonCompletionRequestAnswersValue_Translation": ".lesson_completion_request_answers_value",
    "LessonCompletionRequestStepTimingsValue": ".lesson_completion_request_step_timings_value",
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
