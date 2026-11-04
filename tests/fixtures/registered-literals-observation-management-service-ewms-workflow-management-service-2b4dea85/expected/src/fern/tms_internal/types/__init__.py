



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_v1tms_pending_starter_taskforces_response import GetV1TmsPendingStarterTaskforcesResponse
    from .get_v1tms_pending_starter_taskforces_response_mqprofiles import (
        GetV1TmsPendingStarterTaskforcesResponseMqprofiles,
    )
    from .get_v1tms_pending_stopper_taskforces_response import GetV1TmsPendingStopperTaskforcesResponse
    from .post_v1tms_condor_complete_taskforces_taskforce_uuid_response import (
        PostV1TmsCondorCompleteTaskforcesTaskforceUuidResponse,
    )
    from .post_v1tms_condor_rm_taskforces_taskforce_uuid_failed_response import (
        PostV1TmsCondorRmTaskforcesTaskforceUuidFailedResponse,
    )
    from .post_v1tms_condor_rm_taskforces_taskforce_uuid_response import (
        PostV1TmsCondorRmTaskforcesTaskforceUuidResponse,
    )
    from .post_v1tms_condor_submit_taskforces_taskforce_uuid_failed_response import (
        PostV1TmsCondorSubmitTaskforcesTaskforceUuidFailedResponse,
    )
    from .post_v1tms_condor_submit_taskforces_taskforce_uuid_response import (
        PostV1TmsCondorSubmitTaskforcesTaskforceUuidResponse,
    )
    from .post_v1tms_statuses_taskforces_response import PostV1TmsStatusesTaskforcesResponse
    from .post_v1tms_statuses_taskforces_response_results_item import PostV1TmsStatusesTaskforcesResponseResultsItem
_dynamic_imports: typing.Dict[str, str] = {
    "GetV1TmsPendingStarterTaskforcesResponse": ".get_v1tms_pending_starter_taskforces_response",
    "GetV1TmsPendingStarterTaskforcesResponseMqprofiles": ".get_v1tms_pending_starter_taskforces_response_mqprofiles",
    "GetV1TmsPendingStopperTaskforcesResponse": ".get_v1tms_pending_stopper_taskforces_response",
    "PostV1TmsCondorCompleteTaskforcesTaskforceUuidResponse": ".post_v1tms_condor_complete_taskforces_taskforce_uuid_response",
    "PostV1TmsCondorRmTaskforcesTaskforceUuidFailedResponse": ".post_v1tms_condor_rm_taskforces_taskforce_uuid_failed_response",
    "PostV1TmsCondorRmTaskforcesTaskforceUuidResponse": ".post_v1tms_condor_rm_taskforces_taskforce_uuid_response",
    "PostV1TmsCondorSubmitTaskforcesTaskforceUuidFailedResponse": ".post_v1tms_condor_submit_taskforces_taskforce_uuid_failed_response",
    "PostV1TmsCondorSubmitTaskforcesTaskforceUuidResponse": ".post_v1tms_condor_submit_taskforces_taskforce_uuid_response",
    "PostV1TmsStatusesTaskforcesResponse": ".post_v1tms_statuses_taskforces_response",
    "PostV1TmsStatusesTaskforcesResponseResultsItem": ".post_v1tms_statuses_taskforces_response_results_item",
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
    "GetV1TmsPendingStarterTaskforcesResponse",
    "GetV1TmsPendingStarterTaskforcesResponseMqprofiles",
    "GetV1TmsPendingStopperTaskforcesResponse",
    "PostV1TmsCondorCompleteTaskforcesTaskforceUuidResponse",
    "PostV1TmsCondorRmTaskforcesTaskforceUuidFailedResponse",
    "PostV1TmsCondorRmTaskforcesTaskforceUuidResponse",
    "PostV1TmsCondorSubmitTaskforcesTaskforceUuidFailedResponse",
    "PostV1TmsCondorSubmitTaskforcesTaskforceUuidResponse",
    "PostV1TmsStatusesTaskforcesResponse",
    "PostV1TmsStatusesTaskforcesResponseResultsItem",
]
