



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .search_test_executions_v1test_executions_get_request_assignee_ids import (
        SearchTestExecutionsV1TestExecutionsGetRequestAssigneeIds,
    )
    from .search_test_executions_v1test_executions_get_request_assignee_ids_one_item import (
        SearchTestExecutionsV1TestExecutionsGetRequestAssigneeIdsOneItem,
    )
    from .search_test_executions_v1test_executions_get_request_assignee_ids_two_item import (
        SearchTestExecutionsV1TestExecutionsGetRequestAssigneeIdsTwoItem,
    )
    from .search_test_executions_v1test_executions_get_request_event_names import (
        SearchTestExecutionsV1TestExecutionsGetRequestEventNames,
    )
    from .search_test_executions_v1test_executions_get_request_event_names_one_item import (
        SearchTestExecutionsV1TestExecutionsGetRequestEventNamesOneItem,
    )
    from .search_test_executions_v1test_executions_get_request_event_names_two_item import (
        SearchTestExecutionsV1TestExecutionsGetRequestEventNamesTwoItem,
    )
    from .search_test_executions_v1test_executions_get_request_reviewer_ids import (
        SearchTestExecutionsV1TestExecutionsGetRequestReviewerIds,
    )
    from .search_test_executions_v1test_executions_get_request_reviewer_ids_one_item import (
        SearchTestExecutionsV1TestExecutionsGetRequestReviewerIdsOneItem,
    )
    from .search_test_executions_v1test_executions_get_request_reviewer_ids_two_item import (
        SearchTestExecutionsV1TestExecutionsGetRequestReviewerIdsTwoItem,
    )
    from .search_test_executions_v1test_executions_get_request_test_result import (
        SearchTestExecutionsV1TestExecutionsGetRequestTestResult,
    )
    from .search_test_executions_v1test_executions_get_request_test_result_one_item import (
        SearchTestExecutionsV1TestExecutionsGetRequestTestResultOneItem,
    )
    from .search_test_executions_v1test_executions_get_request_test_result_two_item import (
        SearchTestExecutionsV1TestExecutionsGetRequestTestResultTwoItem,
    )
    from .start_test_execution_v1test_executions_start_test_put_request import (
        StartTestExecutionV1TestExecutionsStartTestPutRequest,
        StartTestExecutionV1TestExecutionsStartTestPutRequest_Charm,
        StartTestExecutionV1TestExecutionsStartTestPutRequest_Deb,
        StartTestExecutionV1TestExecutionsStartTestPutRequest_Image,
        StartTestExecutionV1TestExecutionsStartTestPutRequest_Snap,
        StartTestExecutionV1TestExecutionsStartTestPutRequest_Solution,
    )
    from .test_executions_patch_request_status import TestExecutionsPatchRequestStatus
    from .test_executions_patch_request_status_one import TestExecutionsPatchRequestStatusOne
_dynamic_imports: typing.Dict[str, str] = {
    "SearchTestExecutionsV1TestExecutionsGetRequestAssigneeIds": ".search_test_executions_v1test_executions_get_request_assignee_ids",
    "SearchTestExecutionsV1TestExecutionsGetRequestAssigneeIdsOneItem": ".search_test_executions_v1test_executions_get_request_assignee_ids_one_item",
    "SearchTestExecutionsV1TestExecutionsGetRequestAssigneeIdsTwoItem": ".search_test_executions_v1test_executions_get_request_assignee_ids_two_item",
    "SearchTestExecutionsV1TestExecutionsGetRequestEventNames": ".search_test_executions_v1test_executions_get_request_event_names",
    "SearchTestExecutionsV1TestExecutionsGetRequestEventNamesOneItem": ".search_test_executions_v1test_executions_get_request_event_names_one_item",
    "SearchTestExecutionsV1TestExecutionsGetRequestEventNamesTwoItem": ".search_test_executions_v1test_executions_get_request_event_names_two_item",
    "SearchTestExecutionsV1TestExecutionsGetRequestReviewerIds": ".search_test_executions_v1test_executions_get_request_reviewer_ids",
    "SearchTestExecutionsV1TestExecutionsGetRequestReviewerIdsOneItem": ".search_test_executions_v1test_executions_get_request_reviewer_ids_one_item",
    "SearchTestExecutionsV1TestExecutionsGetRequestReviewerIdsTwoItem": ".search_test_executions_v1test_executions_get_request_reviewer_ids_two_item",
    "SearchTestExecutionsV1TestExecutionsGetRequestTestResult": ".search_test_executions_v1test_executions_get_request_test_result",
    "SearchTestExecutionsV1TestExecutionsGetRequestTestResultOneItem": ".search_test_executions_v1test_executions_get_request_test_result_one_item",
    "SearchTestExecutionsV1TestExecutionsGetRequestTestResultTwoItem": ".search_test_executions_v1test_executions_get_request_test_result_two_item",
    "StartTestExecutionV1TestExecutionsStartTestPutRequest": ".start_test_execution_v1test_executions_start_test_put_request",
    "StartTestExecutionV1TestExecutionsStartTestPutRequest_Charm": ".start_test_execution_v1test_executions_start_test_put_request",
    "StartTestExecutionV1TestExecutionsStartTestPutRequest_Deb": ".start_test_execution_v1test_executions_start_test_put_request",
    "StartTestExecutionV1TestExecutionsStartTestPutRequest_Image": ".start_test_execution_v1test_executions_start_test_put_request",
    "StartTestExecutionV1TestExecutionsStartTestPutRequest_Snap": ".start_test_execution_v1test_executions_start_test_put_request",
    "StartTestExecutionV1TestExecutionsStartTestPutRequest_Solution": ".start_test_execution_v1test_executions_start_test_put_request",
    "TestExecutionsPatchRequestStatus": ".test_executions_patch_request_status",
    "TestExecutionsPatchRequestStatusOne": ".test_executions_patch_request_status_one",
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
    "SearchTestExecutionsV1TestExecutionsGetRequestAssigneeIds",
    "SearchTestExecutionsV1TestExecutionsGetRequestAssigneeIdsOneItem",
    "SearchTestExecutionsV1TestExecutionsGetRequestAssigneeIdsTwoItem",
    "SearchTestExecutionsV1TestExecutionsGetRequestEventNames",
    "SearchTestExecutionsV1TestExecutionsGetRequestEventNamesOneItem",
    "SearchTestExecutionsV1TestExecutionsGetRequestEventNamesTwoItem",
    "SearchTestExecutionsV1TestExecutionsGetRequestReviewerIds",
    "SearchTestExecutionsV1TestExecutionsGetRequestReviewerIdsOneItem",
    "SearchTestExecutionsV1TestExecutionsGetRequestReviewerIdsTwoItem",
    "SearchTestExecutionsV1TestExecutionsGetRequestTestResult",
    "SearchTestExecutionsV1TestExecutionsGetRequestTestResultOneItem",
    "SearchTestExecutionsV1TestExecutionsGetRequestTestResultTwoItem",
    "StartTestExecutionV1TestExecutionsStartTestPutRequest",
    "StartTestExecutionV1TestExecutionsStartTestPutRequest_Charm",
    "StartTestExecutionV1TestExecutionsStartTestPutRequest_Deb",
    "StartTestExecutionV1TestExecutionsStartTestPutRequest_Image",
    "StartTestExecutionV1TestExecutionsStartTestPutRequest_Snap",
    "StartTestExecutionV1TestExecutionsStartTestPutRequest_Solution",
    "TestExecutionsPatchRequestStatus",
    "TestExecutionsPatchRequestStatusOne",
]
