



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        SearchTestResultsV1TestResultsGetRequestAssigneeIds,
        SearchTestResultsV1TestResultsGetRequestAssigneeIdsOneItem,
        SearchTestResultsV1TestResultsGetRequestAssigneeIdsTwoItem,
        SearchTestResultsV1TestResultsGetRequestIssues,
        SearchTestResultsV1TestResultsGetRequestIssuesOneItem,
        SearchTestResultsV1TestResultsGetRequestIssuesTwoItem,
        SearchTestResultsV1TestResultsGetRequestReviewerIds,
        SearchTestResultsV1TestResultsGetRequestReviewerIdsOneItem,
        SearchTestResultsV1TestResultsGetRequestReviewerIdsTwoItem,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "SearchTestResultsV1TestResultsGetRequestAssigneeIds": ".types",
    "SearchTestResultsV1TestResultsGetRequestAssigneeIdsOneItem": ".types",
    "SearchTestResultsV1TestResultsGetRequestAssigneeIdsTwoItem": ".types",
    "SearchTestResultsV1TestResultsGetRequestIssues": ".types",
    "SearchTestResultsV1TestResultsGetRequestIssuesOneItem": ".types",
    "SearchTestResultsV1TestResultsGetRequestIssuesTwoItem": ".types",
    "SearchTestResultsV1TestResultsGetRequestReviewerIds": ".types",
    "SearchTestResultsV1TestResultsGetRequestReviewerIdsOneItem": ".types",
    "SearchTestResultsV1TestResultsGetRequestReviewerIdsTwoItem": ".types",
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
    "SearchTestResultsV1TestResultsGetRequestAssigneeIds",
    "SearchTestResultsV1TestResultsGetRequestAssigneeIdsOneItem",
    "SearchTestResultsV1TestResultsGetRequestAssigneeIdsTwoItem",
    "SearchTestResultsV1TestResultsGetRequestIssues",
    "SearchTestResultsV1TestResultsGetRequestIssuesOneItem",
    "SearchTestResultsV1TestResultsGetRequestIssuesTwoItem",
    "SearchTestResultsV1TestResultsGetRequestReviewerIds",
    "SearchTestResultsV1TestResultsGetRequestReviewerIdsOneItem",
    "SearchTestResultsV1TestResultsGetRequestReviewerIdsTwoItem",
]
