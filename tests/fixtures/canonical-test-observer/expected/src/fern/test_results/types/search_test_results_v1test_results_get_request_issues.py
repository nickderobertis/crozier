

import typing

from .search_test_results_v1test_results_get_request_issues_one_item import (
    SearchTestResultsV1TestResultsGetRequestIssuesOneItem,
)
from .search_test_results_v1test_results_get_request_issues_two_item import (
    SearchTestResultsV1TestResultsGetRequestIssuesTwoItem,
)

SearchTestResultsV1TestResultsGetRequestIssues = typing.Union[
    typing.List[int],
    typing.List[SearchTestResultsV1TestResultsGetRequestIssuesOneItem],
    typing.List[SearchTestResultsV1TestResultsGetRequestIssuesTwoItem],
]
