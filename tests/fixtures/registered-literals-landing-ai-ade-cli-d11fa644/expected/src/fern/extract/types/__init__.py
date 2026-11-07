



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .v2extract_create_job_request_service_tier import V2ExtractCreateJobRequestServiceTier
    from .v2extract_create_job_response import V2ExtractCreateJobResponse
    from .v2extract_create_job_response_status import V2ExtractCreateJobResponseStatus
    from .v2extract_get_job_response import V2ExtractGetJobResponse
    from .v2extract_get_job_response_error import V2ExtractGetJobResponseError
    from .v2extract_get_job_response_result import V2ExtractGetJobResponseResult
    from .v2extract_get_job_response_status import V2ExtractGetJobResponseStatus
    from .v2extract_list_jobs_response import V2ExtractListJobsResponse
    from .v2extract_list_jobs_response_jobs_item import V2ExtractListJobsResponseJobsItem
    from .v2extract_list_jobs_response_jobs_item_status import V2ExtractListJobsResponseJobsItemStatus
    from .v2extract_run_sync_response import V2ExtractRunSyncResponse
_dynamic_imports: typing.Dict[str, str] = {
    "V2ExtractCreateJobRequestServiceTier": ".v2extract_create_job_request_service_tier",
    "V2ExtractCreateJobResponse": ".v2extract_create_job_response",
    "V2ExtractCreateJobResponseStatus": ".v2extract_create_job_response_status",
    "V2ExtractGetJobResponse": ".v2extract_get_job_response",
    "V2ExtractGetJobResponseError": ".v2extract_get_job_response_error",
    "V2ExtractGetJobResponseResult": ".v2extract_get_job_response_result",
    "V2ExtractGetJobResponseStatus": ".v2extract_get_job_response_status",
    "V2ExtractListJobsResponse": ".v2extract_list_jobs_response",
    "V2ExtractListJobsResponseJobsItem": ".v2extract_list_jobs_response_jobs_item",
    "V2ExtractListJobsResponseJobsItemStatus": ".v2extract_list_jobs_response_jobs_item_status",
    "V2ExtractRunSyncResponse": ".v2extract_run_sync_response",
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
    "V2ExtractCreateJobRequestServiceTier",
    "V2ExtractCreateJobResponse",
    "V2ExtractCreateJobResponseStatus",
    "V2ExtractGetJobResponse",
    "V2ExtractGetJobResponseError",
    "V2ExtractGetJobResponseResult",
    "V2ExtractGetJobResponseStatus",
    "V2ExtractListJobsResponse",
    "V2ExtractListJobsResponseJobsItem",
    "V2ExtractListJobsResponseJobsItemStatus",
    "V2ExtractRunSyncResponse",
]
