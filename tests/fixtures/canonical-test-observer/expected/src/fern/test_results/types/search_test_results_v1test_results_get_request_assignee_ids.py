

import typing

from .search_test_results_v1test_results_get_request_assignee_ids_one_item import (
    SearchTestResultsV1TestResultsGetRequestAssigneeIdsOneItem,
)
from .search_test_results_v1test_results_get_request_assignee_ids_two_item import (
    SearchTestResultsV1TestResultsGetRequestAssigneeIdsTwoItem,
)

SearchTestResultsV1TestResultsGetRequestAssigneeIds = typing.Union[
    typing.List[int],
    typing.List[SearchTestResultsV1TestResultsGetRequestAssigneeIdsOneItem],
    typing.List[SearchTestResultsV1TestResultsGetRequestAssigneeIdsTwoItem],
]
