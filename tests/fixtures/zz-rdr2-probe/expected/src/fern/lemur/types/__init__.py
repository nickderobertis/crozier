



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .lemur_action_items_params import LemurActionItemsParams
    from .lemur_action_items_response import LemurActionItemsResponse
    from .lemur_base_params import LemurBaseParams
    from .lemur_base_params_context import LemurBaseParamsContext
    from .lemur_base_params_final_model import LemurBaseParamsFinalModel
    from .lemur_base_response import LemurBaseResponse
    from .lemur_model import LemurModel
    from .lemur_question import LemurQuestion
    from .lemur_question_answer import LemurQuestionAnswer
    from .lemur_question_answer_params import LemurQuestionAnswerParams
    from .lemur_question_answer_response import LemurQuestionAnswerResponse
    from .lemur_question_context import LemurQuestionContext
    from .lemur_response import LemurResponse
    from .lemur_string_response import LemurStringResponse
    from .lemur_summary_params import LemurSummaryParams
    from .lemur_summary_response import LemurSummaryResponse
    from .lemur_task_response import LemurTaskResponse
    from .lemur_usage import LemurUsage
    from .purge_lemur_request_data_response import PurgeLemurRequestDataResponse
_dynamic_imports: typing.Dict[str, str] = {
    "LemurActionItemsParams": ".lemur_action_items_params",
    "LemurActionItemsResponse": ".lemur_action_items_response",
    "LemurBaseParams": ".lemur_base_params",
    "LemurBaseParamsContext": ".lemur_base_params_context",
    "LemurBaseParamsFinalModel": ".lemur_base_params_final_model",
    "LemurBaseResponse": ".lemur_base_response",
    "LemurModel": ".lemur_model",
    "LemurQuestion": ".lemur_question",
    "LemurQuestionAnswer": ".lemur_question_answer",
    "LemurQuestionAnswerParams": ".lemur_question_answer_params",
    "LemurQuestionAnswerResponse": ".lemur_question_answer_response",
    "LemurQuestionContext": ".lemur_question_context",
    "LemurResponse": ".lemur_response",
    "LemurStringResponse": ".lemur_string_response",
    "LemurSummaryParams": ".lemur_summary_params",
    "LemurSummaryResponse": ".lemur_summary_response",
    "LemurTaskResponse": ".lemur_task_response",
    "LemurUsage": ".lemur_usage",
    "PurgeLemurRequestDataResponse": ".purge_lemur_request_data_response",
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
    "LemurActionItemsParams",
    "LemurActionItemsResponse",
    "LemurBaseParams",
    "LemurBaseParamsContext",
    "LemurBaseParamsFinalModel",
    "LemurBaseResponse",
    "LemurModel",
    "LemurQuestion",
    "LemurQuestionAnswer",
    "LemurQuestionAnswerParams",
    "LemurQuestionAnswerResponse",
    "LemurQuestionContext",
    "LemurResponse",
    "LemurStringResponse",
    "LemurSummaryParams",
    "LemurSummaryResponse",
    "LemurTaskResponse",
    "LemurUsage",
    "PurgeLemurRequestDataResponse",
]
