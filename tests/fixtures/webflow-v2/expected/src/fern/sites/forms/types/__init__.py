



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_submission_forms_response import GetSubmissionFormsResponse
    from .list_submissions_by_site_forms_response import ListSubmissionsBySiteFormsResponse
    from .list_submissions_by_site_forms_response_form_submissions_item import (
        ListSubmissionsBySiteFormsResponseFormSubmissionsItem,
    )
    from .list_submissions_by_site_forms_response_pagination import ListSubmissionsBySiteFormsResponsePagination
    from .list_submissions_forms_response import ListSubmissionsFormsResponse
    from .list_submissions_forms_response_form_submissions_item import ListSubmissionsFormsResponseFormSubmissionsItem
    from .list_submissions_forms_response_pagination import ListSubmissionsFormsResponsePagination
    from .update_submission_forms_response import UpdateSubmissionFormsResponse
_dynamic_imports: typing.Dict[str, str] = {
    "GetSubmissionFormsResponse": ".get_submission_forms_response",
    "ListSubmissionsBySiteFormsResponse": ".list_submissions_by_site_forms_response",
    "ListSubmissionsBySiteFormsResponseFormSubmissionsItem": ".list_submissions_by_site_forms_response_form_submissions_item",
    "ListSubmissionsBySiteFormsResponsePagination": ".list_submissions_by_site_forms_response_pagination",
    "ListSubmissionsFormsResponse": ".list_submissions_forms_response",
    "ListSubmissionsFormsResponseFormSubmissionsItem": ".list_submissions_forms_response_form_submissions_item",
    "ListSubmissionsFormsResponsePagination": ".list_submissions_forms_response_pagination",
    "UpdateSubmissionFormsResponse": ".update_submission_forms_response",
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
    "GetSubmissionFormsResponse",
    "ListSubmissionsBySiteFormsResponse",
    "ListSubmissionsBySiteFormsResponseFormSubmissionsItem",
    "ListSubmissionsBySiteFormsResponsePagination",
    "ListSubmissionsFormsResponse",
    "ListSubmissionsFormsResponseFormSubmissionsItem",
    "ListSubmissionsFormsResponsePagination",
    "UpdateSubmissionFormsResponse",
]
