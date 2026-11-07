



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .v2ground_create_job_response import V2GroundCreateJobResponse
    from .v2ground_create_job_response_status import V2GroundCreateJobResponseStatus
    from .v2ground_get_job_response import V2GroundGetJobResponse
    from .v2ground_get_job_response_error import V2GroundGetJobResponseError
    from .v2ground_get_job_response_result import V2GroundGetJobResponseResult
    from .v2ground_get_job_response_status import V2GroundGetJobResponseStatus
    from .v2ground_list_jobs_response import V2GroundListJobsResponse
    from .v2ground_list_jobs_response_jobs_item import V2GroundListJobsResponseJobsItem
    from .v2ground_list_jobs_response_jobs_item_status import V2GroundListJobsResponseJobsItemStatus
    from .v2ground_run_sync_response import V2GroundRunSyncResponse
_dynamic_imports: typing.Dict[str, str] = {
    "V2GroundCreateJobResponse": ".v2ground_create_job_response",
    "V2GroundCreateJobResponseStatus": ".v2ground_create_job_response_status",
    "V2GroundGetJobResponse": ".v2ground_get_job_response",
    "V2GroundGetJobResponseError": ".v2ground_get_job_response_error",
    "V2GroundGetJobResponseResult": ".v2ground_get_job_response_result",
    "V2GroundGetJobResponseStatus": ".v2ground_get_job_response_status",
    "V2GroundListJobsResponse": ".v2ground_list_jobs_response",
    "V2GroundListJobsResponseJobsItem": ".v2ground_list_jobs_response_jobs_item",
    "V2GroundListJobsResponseJobsItemStatus": ".v2ground_list_jobs_response_jobs_item_status",
    "V2GroundRunSyncResponse": ".v2ground_run_sync_response",
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
    "V2GroundCreateJobResponse",
    "V2GroundCreateJobResponseStatus",
    "V2GroundGetJobResponse",
    "V2GroundGetJobResponseError",
    "V2GroundGetJobResponseResult",
    "V2GroundGetJobResponseStatus",
    "V2GroundListJobsResponse",
    "V2GroundListJobsResponseJobsItem",
    "V2GroundListJobsResponseJobsItemStatus",
    "V2GroundRunSyncResponse",
]
