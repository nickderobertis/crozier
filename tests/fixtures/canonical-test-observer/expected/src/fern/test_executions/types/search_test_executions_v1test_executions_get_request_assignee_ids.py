

import typing

from .search_test_executions_v1test_executions_get_request_assignee_ids_one_item import (
    SearchTestExecutionsV1TestExecutionsGetRequestAssigneeIdsOneItem,
)
from .search_test_executions_v1test_executions_get_request_assignee_ids_two_item import (
    SearchTestExecutionsV1TestExecutionsGetRequestAssigneeIdsTwoItem,
)

SearchTestExecutionsV1TestExecutionsGetRequestAssigneeIds = typing.Union[
    typing.List[int],
    typing.List[SearchTestExecutionsV1TestExecutionsGetRequestAssigneeIdsOneItem],
    typing.List[SearchTestExecutionsV1TestExecutionsGetRequestAssigneeIdsTwoItem],
]
