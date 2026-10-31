



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .search_test_results_v1test_results_get_request_assignee_ids import (
        SearchTestResultsV1TestResultsGetRequestAssigneeIds,
    )
    from .search_test_results_v1test_results_get_request_assignee_ids_one_item import (
        SearchTestResultsV1TestResultsGetRequestAssigneeIdsOneItem,
    )
    from .search_test_results_v1test_results_get_request_assignee_ids_two_item import (
        SearchTestResultsV1TestResultsGetRequestAssigneeIdsTwoItem,
    )
    from .search_test_results_v1test_results_get_request_issues import SearchTestResultsV1TestResultsGetRequestIssues
    from .search_test_results_v1test_results_get_request_issues_one_item import (
        SearchTestResultsV1TestResultsGetRequestIssuesOneItem,
    )
    from .search_test_results_v1test_results_get_request_issues_two_item import (
        SearchTestResultsV1TestResultsGetRequestIssuesTwoItem,
    )
    from .search_test_results_v1test_results_get_request_reviewer_ids import (
        SearchTestResultsV1TestResultsGetRequestReviewerIds,
    )
    from .search_test_results_v1test_results_get_request_reviewer_ids_one_item import (
        SearchTestResultsV1TestResultsGetRequestReviewerIdsOneItem,
    )
    from .search_test_results_v1test_results_get_request_reviewer_ids_two_item import (
        SearchTestResultsV1TestResultsGetRequestReviewerIdsTwoItem,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "SearchTestResultsV1TestResultsGetRequestAssigneeIds": ".search_test_results_v1test_results_get_request_assignee_ids",
    "SearchTestResultsV1TestResultsGetRequestAssigneeIdsOneItem": ".search_test_results_v1test_results_get_request_assignee_ids_one_item",
    "SearchTestResultsV1TestResultsGetRequestAssigneeIdsTwoItem": ".search_test_results_v1test_results_get_request_assignee_ids_two_item",
    "SearchTestResultsV1TestResultsGetRequestIssues": ".search_test_results_v1test_results_get_request_issues",
    "SearchTestResultsV1TestResultsGetRequestIssuesOneItem": ".search_test_results_v1test_results_get_request_issues_one_item",
    "SearchTestResultsV1TestResultsGetRequestIssuesTwoItem": ".search_test_results_v1test_results_get_request_issues_two_item",
    "SearchTestResultsV1TestResultsGetRequestReviewerIds": ".search_test_results_v1test_results_get_request_reviewer_ids",
    "SearchTestResultsV1TestResultsGetRequestReviewerIdsOneItem": ".search_test_results_v1test_results_get_request_reviewer_ids_one_item",
    "SearchTestResultsV1TestResultsGetRequestReviewerIdsTwoItem": ".search_test_results_v1test_results_get_request_reviewer_ids_two_item",
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
