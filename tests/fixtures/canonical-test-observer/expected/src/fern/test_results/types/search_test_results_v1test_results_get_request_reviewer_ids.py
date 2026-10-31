

import typing

from .search_test_results_v1test_results_get_request_reviewer_ids_one_item import (
    SearchTestResultsV1TestResultsGetRequestReviewerIdsOneItem,
)
from .search_test_results_v1test_results_get_request_reviewer_ids_two_item import (
    SearchTestResultsV1TestResultsGetRequestReviewerIdsTwoItem,
)

SearchTestResultsV1TestResultsGetRequestReviewerIds = typing.Union[
    typing.List[int],
    typing.List[SearchTestResultsV1TestResultsGetRequestReviewerIdsOneItem],
    typing.List[SearchTestResultsV1TestResultsGetRequestReviewerIdsTwoItem],
]
