



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        DeactivatedWorkflowResponseObject,
        ErrorResponse,
        FindObject,
        QueryNextAfter,
        TaskDirectiveObject,
        TaskforceObject,
        TaskforceObjectPhase,
        TaskforceObjectPhaseChangeLogItem,
        TaskforceObjectPilotConfig,
        TaskforceObjectPilotConfigEnvironmentValue,
        TaskforceObjectPilotConfigImageSource,
        TaskforceObjectSubmitDictValue,
        TaskforceObjectWorkerConfig,
        TaskforceObjectWorkerConfigWorkerDisk,
        TaskforceObjectWorkerConfigWorkerMemory,
        WorkflowObject,
        WorkflowObjectDeactivated,
    )
    from .errors import BadRequestError, NotFoundError, UnprocessableEntityError
    from . import openapi, task_directives, taskforces, tms_internal, workflows
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .task_directives import PostV1QueryTaskDirectivesResponse
    from .taskforces import PostV1QueryTaskforcesResponse
    from .tms_internal import (
        GetV1TmsPendingStarterTaskforcesResponse,
        GetV1TmsPendingStarterTaskforcesResponseMqprofiles,
        GetV1TmsPendingStopperTaskforcesResponse,
        PostV1TmsCondorCompleteTaskforcesTaskforceUuidResponse,
        PostV1TmsCondorRmTaskforcesTaskforceUuidFailedResponse,
        PostV1TmsCondorRmTaskforcesTaskforceUuidResponse,
        PostV1TmsCondorSubmitTaskforcesTaskforceUuidFailedResponse,
        PostV1TmsCondorSubmitTaskforcesTaskforceUuidResponse,
        PostV1TmsStatusesTaskforcesResponse,
        PostV1TmsStatusesTaskforcesResponseResultsItem,
    )
    from .version import __version__
    from .workflows import (
        PostV1QueryWorkflowsResponse,
        PostV1WorkflowsRequestTasksItem,
        PostV1WorkflowsRequestTasksItemPilotConfig,
        PostV1WorkflowsRequestTasksItemPilotConfigEnvironmentValue,
        PostV1WorkflowsRequestTasksItemPilotConfigImageSource,
        PostV1WorkflowsRequestTasksItemWorkerConfig,
        PostV1WorkflowsRequestTasksItemWorkerConfigWorkerDisk,
        PostV1WorkflowsRequestTasksItemWorkerConfigWorkerMemory,
        PostV1WorkflowsResponse,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "DeactivatedWorkflowResponseObject": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "ErrorResponse": ".types",
    "FernApi": ".client",
    "FindObject": ".types",
    "GetV1TmsPendingStarterTaskforcesResponse": ".tms_internal",
    "GetV1TmsPendingStarterTaskforcesResponseMqprofiles": ".tms_internal",
    "GetV1TmsPendingStopperTaskforcesResponse": ".tms_internal",
    "NotFoundError": ".errors",
    "PostV1QueryTaskDirectivesResponse": ".task_directives",
    "PostV1QueryTaskforcesResponse": ".taskforces",
    "PostV1QueryWorkflowsResponse": ".workflows",
    "PostV1TmsCondorCompleteTaskforcesTaskforceUuidResponse": ".tms_internal",
    "PostV1TmsCondorRmTaskforcesTaskforceUuidFailedResponse": ".tms_internal",
    "PostV1TmsCondorRmTaskforcesTaskforceUuidResponse": ".tms_internal",
    "PostV1TmsCondorSubmitTaskforcesTaskforceUuidFailedResponse": ".tms_internal",
    "PostV1TmsCondorSubmitTaskforcesTaskforceUuidResponse": ".tms_internal",
    "PostV1TmsStatusesTaskforcesResponse": ".tms_internal",
    "PostV1TmsStatusesTaskforcesResponseResultsItem": ".tms_internal",
    "PostV1WorkflowsRequestTasksItem": ".workflows",
    "PostV1WorkflowsRequestTasksItemPilotConfig": ".workflows",
    "PostV1WorkflowsRequestTasksItemPilotConfigEnvironmentValue": ".workflows",
    "PostV1WorkflowsRequestTasksItemPilotConfigImageSource": ".workflows",
    "PostV1WorkflowsRequestTasksItemWorkerConfig": ".workflows",
    "PostV1WorkflowsRequestTasksItemWorkerConfigWorkerDisk": ".workflows",
    "PostV1WorkflowsRequestTasksItemWorkerConfigWorkerMemory": ".workflows",
    "PostV1WorkflowsResponse": ".workflows",
    "QueryNextAfter": ".types",
    "TaskDirectiveObject": ".types",
    "TaskforceObject": ".types",
    "TaskforceObjectPhase": ".types",
    "TaskforceObjectPhaseChangeLogItem": ".types",
    "TaskforceObjectPilotConfig": ".types",
    "TaskforceObjectPilotConfigEnvironmentValue": ".types",
    "TaskforceObjectPilotConfigImageSource": ".types",
    "TaskforceObjectSubmitDictValue": ".types",
    "TaskforceObjectWorkerConfig": ".types",
    "TaskforceObjectWorkerConfigWorkerDisk": ".types",
    "TaskforceObjectWorkerConfigWorkerMemory": ".types",
    "UnprocessableEntityError": ".errors",
    "WorkflowObject": ".types",
    "WorkflowObjectDeactivated": ".types",
    "__version__": ".version",
    "openapi": ".openapi",
    "task_directives": ".task_directives",
    "taskforces": ".taskforces",
    "tms_internal": ".tms_internal",
    "workflows": ".workflows",
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
    "AsyncFernApi",
    "BadRequestError",
    "DeactivatedWorkflowResponseObject",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "ErrorResponse",
    "FernApi",
    "FindObject",
    "GetV1TmsPendingStarterTaskforcesResponse",
    "GetV1TmsPendingStarterTaskforcesResponseMqprofiles",
    "GetV1TmsPendingStopperTaskforcesResponse",
    "NotFoundError",
    "PostV1QueryTaskDirectivesResponse",
    "PostV1QueryTaskforcesResponse",
    "PostV1QueryWorkflowsResponse",
    "PostV1TmsCondorCompleteTaskforcesTaskforceUuidResponse",
    "PostV1TmsCondorRmTaskforcesTaskforceUuidFailedResponse",
    "PostV1TmsCondorRmTaskforcesTaskforceUuidResponse",
    "PostV1TmsCondorSubmitTaskforcesTaskforceUuidFailedResponse",
    "PostV1TmsCondorSubmitTaskforcesTaskforceUuidResponse",
    "PostV1TmsStatusesTaskforcesResponse",
    "PostV1TmsStatusesTaskforcesResponseResultsItem",
    "PostV1WorkflowsRequestTasksItem",
    "PostV1WorkflowsRequestTasksItemPilotConfig",
    "PostV1WorkflowsRequestTasksItemPilotConfigEnvironmentValue",
    "PostV1WorkflowsRequestTasksItemPilotConfigImageSource",
    "PostV1WorkflowsRequestTasksItemWorkerConfig",
    "PostV1WorkflowsRequestTasksItemWorkerConfigWorkerDisk",
    "PostV1WorkflowsRequestTasksItemWorkerConfigWorkerMemory",
    "PostV1WorkflowsResponse",
    "QueryNextAfter",
    "TaskDirectiveObject",
    "TaskforceObject",
    "TaskforceObjectPhase",
    "TaskforceObjectPhaseChangeLogItem",
    "TaskforceObjectPilotConfig",
    "TaskforceObjectPilotConfigEnvironmentValue",
    "TaskforceObjectPilotConfigImageSource",
    "TaskforceObjectSubmitDictValue",
    "TaskforceObjectWorkerConfig",
    "TaskforceObjectWorkerConfigWorkerDisk",
    "TaskforceObjectWorkerConfigWorkerMemory",
    "UnprocessableEntityError",
    "WorkflowObject",
    "WorkflowObjectDeactivated",
    "__version__",
    "openapi",
    "task_directives",
    "taskforces",
    "tms_internal",
    "workflows",
]
