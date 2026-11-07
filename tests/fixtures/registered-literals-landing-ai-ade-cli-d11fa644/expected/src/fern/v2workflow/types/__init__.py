



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .v2workflow_create_job_request_service_tier import V2WorkflowCreateJobRequestServiceTier
    from .v2workflow_create_job_response import V2WorkflowCreateJobResponse
    from .v2workflow_create_job_response_status import V2WorkflowCreateJobResponseStatus
    from .v2workflow_get_job_response import V2WorkflowGetJobResponse
    from .v2workflow_get_job_response_error import V2WorkflowGetJobResponseError
    from .v2workflow_get_job_response_result import V2WorkflowGetJobResponseResult
    from .v2workflow_get_job_response_status import V2WorkflowGetJobResponseStatus
    from .v2workflow_list_jobs_response import V2WorkflowListJobsResponse
    from .v2workflow_list_jobs_response_jobs_item import V2WorkflowListJobsResponseJobsItem
    from .v2workflow_list_jobs_response_jobs_item_status import V2WorkflowListJobsResponseJobsItemStatus
    from .v2workflow_run_sync_response import V2WorkflowRunSyncResponse
_dynamic_imports: typing.Dict[str, str] = {
    "V2WorkflowCreateJobRequestServiceTier": ".v2workflow_create_job_request_service_tier",
    "V2WorkflowCreateJobResponse": ".v2workflow_create_job_response",
    "V2WorkflowCreateJobResponseStatus": ".v2workflow_create_job_response_status",
    "V2WorkflowGetJobResponse": ".v2workflow_get_job_response",
    "V2WorkflowGetJobResponseError": ".v2workflow_get_job_response_error",
    "V2WorkflowGetJobResponseResult": ".v2workflow_get_job_response_result",
    "V2WorkflowGetJobResponseStatus": ".v2workflow_get_job_response_status",
    "V2WorkflowListJobsResponse": ".v2workflow_list_jobs_response",
    "V2WorkflowListJobsResponseJobsItem": ".v2workflow_list_jobs_response_jobs_item",
    "V2WorkflowListJobsResponseJobsItemStatus": ".v2workflow_list_jobs_response_jobs_item_status",
    "V2WorkflowRunSyncResponse": ".v2workflow_run_sync_response",
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
    "V2WorkflowCreateJobRequestServiceTier",
    "V2WorkflowCreateJobResponse",
    "V2WorkflowCreateJobResponseStatus",
    "V2WorkflowGetJobResponse",
    "V2WorkflowGetJobResponseError",
    "V2WorkflowGetJobResponseResult",
    "V2WorkflowGetJobResponseStatus",
    "V2WorkflowListJobsResponse",
    "V2WorkflowListJobsResponseJobsItem",
    "V2WorkflowListJobsResponseJobsItemStatus",
    "V2WorkflowRunSyncResponse",
]
