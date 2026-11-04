



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .parse_create_job_request_options import ParseCreateJobRequestOptions
    from .parse_create_job_request_service_tier import ParseCreateJobRequestServiceTier
    from .parse_create_job_response import ParseCreateJobResponse
    from .parse_create_job_response_status import ParseCreateJobResponseStatus
    from .parse_get_job_response import ParseGetJobResponse
    from .parse_get_job_response_error import ParseGetJobResponseError
    from .parse_get_job_response_status import ParseGetJobResponseStatus
    from .parse_list_jobs_response import ParseListJobsResponse
    from .parse_list_jobs_response_jobs_item import ParseListJobsResponseJobsItem
    from .parse_list_jobs_response_jobs_item_status import ParseListJobsResponseJobsItemStatus
    from .parse_run_sync_request_options import ParseRunSyncRequestOptions
_dynamic_imports: typing.Dict[str, str] = {
    "ParseCreateJobRequestOptions": ".parse_create_job_request_options",
    "ParseCreateJobRequestServiceTier": ".parse_create_job_request_service_tier",
    "ParseCreateJobResponse": ".parse_create_job_response",
    "ParseCreateJobResponseStatus": ".parse_create_job_response_status",
    "ParseGetJobResponse": ".parse_get_job_response",
    "ParseGetJobResponseError": ".parse_get_job_response_error",
    "ParseGetJobResponseStatus": ".parse_get_job_response_status",
    "ParseListJobsResponse": ".parse_list_jobs_response",
    "ParseListJobsResponseJobsItem": ".parse_list_jobs_response_jobs_item",
    "ParseListJobsResponseJobsItemStatus": ".parse_list_jobs_response_jobs_item_status",
    "ParseRunSyncRequestOptions": ".parse_run_sync_request_options",
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
    "ParseCreateJobRequestOptions",
    "ParseCreateJobRequestServiceTier",
    "ParseCreateJobResponse",
    "ParseCreateJobResponseStatus",
    "ParseGetJobResponse",
    "ParseGetJobResponseError",
    "ParseGetJobResponseStatus",
    "ParseListJobsResponse",
    "ParseListJobsResponseJobsItem",
    "ParseListJobsResponseJobsItemStatus",
    "ParseRunSyncRequestOptions",
]
