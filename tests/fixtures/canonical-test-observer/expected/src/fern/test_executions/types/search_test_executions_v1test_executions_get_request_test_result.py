

import typing

from .search_test_executions_v1test_executions_get_request_test_result_one_item import (
    SearchTestExecutionsV1TestExecutionsGetRequestTestResultOneItem,
)
from .search_test_executions_v1test_executions_get_request_test_result_two_item import (
    SearchTestExecutionsV1TestExecutionsGetRequestTestResultTwoItem,
)

SearchTestExecutionsV1TestExecutionsGetRequestTestResult = typing.Union[
    typing.List[int],
    typing.List[SearchTestExecutionsV1TestExecutionsGetRequestTestResultOneItem],
    typing.List[SearchTestExecutionsV1TestExecutionsGetRequestTestResultTwoItem],
]
