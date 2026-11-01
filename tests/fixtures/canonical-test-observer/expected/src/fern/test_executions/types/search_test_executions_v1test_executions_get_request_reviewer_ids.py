

import typing

from .search_test_executions_v1test_executions_get_request_reviewer_ids_one_item import (
    SearchTestExecutionsV1TestExecutionsGetRequestReviewerIdsOneItem,
)
from .search_test_executions_v1test_executions_get_request_reviewer_ids_two_item import (
    SearchTestExecutionsV1TestExecutionsGetRequestReviewerIdsTwoItem,
)

SearchTestExecutionsV1TestExecutionsGetRequestReviewerIds = typing.Union[
    typing.List[int],
    typing.List[SearchTestExecutionsV1TestExecutionsGetRequestReviewerIdsOneItem],
    typing.List[SearchTestExecutionsV1TestExecutionsGetRequestReviewerIdsTwoItem],
]
