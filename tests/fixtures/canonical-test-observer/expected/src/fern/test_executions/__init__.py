



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        SearchTestExecutionsV1TestExecutionsGetRequestAssigneeIds,
        SearchTestExecutionsV1TestExecutionsGetRequestAssigneeIdsOneItem,
        SearchTestExecutionsV1TestExecutionsGetRequestAssigneeIdsTwoItem,
        SearchTestExecutionsV1TestExecutionsGetRequestEventNames,
        SearchTestExecutionsV1TestExecutionsGetRequestEventNamesOneItem,
        SearchTestExecutionsV1TestExecutionsGetRequestEventNamesTwoItem,
        SearchTestExecutionsV1TestExecutionsGetRequestReviewerIds,
        SearchTestExecutionsV1TestExecutionsGetRequestReviewerIdsOneItem,
        SearchTestExecutionsV1TestExecutionsGetRequestReviewerIdsTwoItem,
        SearchTestExecutionsV1TestExecutionsGetRequestTestResult,
        SearchTestExecutionsV1TestExecutionsGetRequestTestResultOneItem,
        SearchTestExecutionsV1TestExecutionsGetRequestTestResultTwoItem,
        StartTestExecutionV1TestExecutionsStartTestPutRequest,
        StartTestExecutionV1TestExecutionsStartTestPutRequest_Charm,
        StartTestExecutionV1TestExecutionsStartTestPutRequest_Deb,
        StartTestExecutionV1TestExecutionsStartTestPutRequest_Image,
        StartTestExecutionV1TestExecutionsStartTestPutRequest_Snap,
        StartTestExecutionV1TestExecutionsStartTestPutRequest_Solution,
        TestExecutionsPatchRequestStatus,
        TestExecutionsPatchRequestStatusOne,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "SearchTestExecutionsV1TestExecutionsGetRequestAssigneeIds": ".types",
    "SearchTestExecutionsV1TestExecutionsGetRequestAssigneeIdsOneItem": ".types",
    "SearchTestExecutionsV1TestExecutionsGetRequestAssigneeIdsTwoItem": ".types",
    "SearchTestExecutionsV1TestExecutionsGetRequestEventNames": ".types",
    "SearchTestExecutionsV1TestExecutionsGetRequestEventNamesOneItem": ".types",
    "SearchTestExecutionsV1TestExecutionsGetRequestEventNamesTwoItem": ".types",
    "SearchTestExecutionsV1TestExecutionsGetRequestReviewerIds": ".types",
    "SearchTestExecutionsV1TestExecutionsGetRequestReviewerIdsOneItem": ".types",
    "SearchTestExecutionsV1TestExecutionsGetRequestReviewerIdsTwoItem": ".types",
    "SearchTestExecutionsV1TestExecutionsGetRequestTestResult": ".types",
    "SearchTestExecutionsV1TestExecutionsGetRequestTestResultOneItem": ".types",
    "SearchTestExecutionsV1TestExecutionsGetRequestTestResultTwoItem": ".types",
    "StartTestExecutionV1TestExecutionsStartTestPutRequest": ".types",
    "StartTestExecutionV1TestExecutionsStartTestPutRequest_Charm": ".types",
    "StartTestExecutionV1TestExecutionsStartTestPutRequest_Deb": ".types",
    "StartTestExecutionV1TestExecutionsStartTestPutRequest_Image": ".types",
    "StartTestExecutionV1TestExecutionsStartTestPutRequest_Snap": ".types",
    "StartTestExecutionV1TestExecutionsStartTestPutRequest_Solution": ".types",
    "TestExecutionsPatchRequestStatus": ".types",
    "TestExecutionsPatchRequestStatusOne": ".types",
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
