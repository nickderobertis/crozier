

import typing

from .search_test_executions_v1test_executions_get_request_event_names_one_item import (
    SearchTestExecutionsV1TestExecutionsGetRequestEventNamesOneItem,
)
from .search_test_executions_v1test_executions_get_request_event_names_two_item import (
    SearchTestExecutionsV1TestExecutionsGetRequestEventNamesTwoItem,
)

SearchTestExecutionsV1TestExecutionsGetRequestEventNames = typing.Union[
    typing.List[str],
    typing.List[SearchTestExecutionsV1TestExecutionsGetRequestEventNamesOneItem],
    typing.List[SearchTestExecutionsV1TestExecutionsGetRequestEventNamesTwoItem],
]
