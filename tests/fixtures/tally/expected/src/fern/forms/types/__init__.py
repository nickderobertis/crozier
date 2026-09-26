



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_form_submission_response import GetFormSubmissionResponse
    from .get_form_submission_response_submission import GetFormSubmissionResponseSubmission
    from .get_form_submission_response_submission_responses_item import GetFormSubmissionResponseSubmissionResponsesItem
    from .get_form_submission_response_submission_responses_item_answer import (
        GetFormSubmissionResponseSubmissionResponsesItemAnswer,
    )
    from .list_form_blocks_response import ListFormBlocksResponse
    from .list_form_questions_response import ListFormQuestionsResponse
    from .list_form_submissions_request_filter import ListFormSubmissionsRequestFilter
    from .list_form_submissions_response import ListFormSubmissionsResponse
    from .list_form_submissions_response_submissions_item import ListFormSubmissionsResponseSubmissionsItem
    from .list_form_submissions_response_submissions_item_responses_item import (
        ListFormSubmissionsResponseSubmissionsItemResponsesItem,
    )
    from .list_form_submissions_response_submissions_item_responses_item_answer import (
        ListFormSubmissionsResponseSubmissionsItemResponsesItemAnswer,
    )
    from .list_form_submissions_response_total_number_of_submissions_per_filter import (
        ListFormSubmissionsResponseTotalNumberOfSubmissionsPerFilter,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "GetFormSubmissionResponse": ".get_form_submission_response",
    "GetFormSubmissionResponseSubmission": ".get_form_submission_response_submission",
    "GetFormSubmissionResponseSubmissionResponsesItem": ".get_form_submission_response_submission_responses_item",
    "GetFormSubmissionResponseSubmissionResponsesItemAnswer": ".get_form_submission_response_submission_responses_item_answer",
    "ListFormBlocksResponse": ".list_form_blocks_response",
    "ListFormQuestionsResponse": ".list_form_questions_response",
    "ListFormSubmissionsRequestFilter": ".list_form_submissions_request_filter",
    "ListFormSubmissionsResponse": ".list_form_submissions_response",
    "ListFormSubmissionsResponseSubmissionsItem": ".list_form_submissions_response_submissions_item",
    "ListFormSubmissionsResponseSubmissionsItemResponsesItem": ".list_form_submissions_response_submissions_item_responses_item",
    "ListFormSubmissionsResponseSubmissionsItemResponsesItemAnswer": ".list_form_submissions_response_submissions_item_responses_item_answer",
    "ListFormSubmissionsResponseTotalNumberOfSubmissionsPerFilter": ".list_form_submissions_response_total_number_of_submissions_per_filter",
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
    "GetFormSubmissionResponse",
    "GetFormSubmissionResponseSubmission",
    "GetFormSubmissionResponseSubmissionResponsesItem",
    "GetFormSubmissionResponseSubmissionResponsesItemAnswer",
    "ListFormBlocksResponse",
    "ListFormQuestionsResponse",
    "ListFormSubmissionsRequestFilter",
    "ListFormSubmissionsResponse",
    "ListFormSubmissionsResponseSubmissionsItem",
    "ListFormSubmissionsResponseSubmissionsItemResponsesItem",
    "ListFormSubmissionsResponseSubmissionsItemResponsesItemAnswer",
    "ListFormSubmissionsResponseTotalNumberOfSubmissionsPerFilter",
]
