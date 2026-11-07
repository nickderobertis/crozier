



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_all_jobs_request_sort import GetAllJobsRequestSort
    from .get_all_jobs_request_status import GetAllJobsRequestStatus
    from .get_jobs_request_sort import GetJobsRequestSort
    from .get_jobs_request_status import GetJobsRequestStatus
    from .get_reports_by_upload_request_report_format import GetReportsByUploadRequestReportFormat
    from .get_scheduler_options_by_operation_request_operation_name import (
        GetSchedulerOptionsByOperationRequestOperationName,
    )
    from .handle_scheduler_run_request_operation import HandleSchedulerRunRequestOperation
_dynamic_imports: typing.Dict[str, str] = {
    "GetAllJobsRequestSort": ".get_all_jobs_request_sort",
    "GetAllJobsRequestStatus": ".get_all_jobs_request_status",
    "GetJobsRequestSort": ".get_jobs_request_sort",
    "GetJobsRequestStatus": ".get_jobs_request_status",
    "GetReportsByUploadRequestReportFormat": ".get_reports_by_upload_request_report_format",
    "GetSchedulerOptionsByOperationRequestOperationName": ".get_scheduler_options_by_operation_request_operation_name",
    "HandleSchedulerRunRequestOperation": ".handle_scheduler_run_request_operation",
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
    "GetAllJobsRequestSort",
    "GetAllJobsRequestStatus",
    "GetJobsRequestSort",
    "GetJobsRequestStatus",
    "GetReportsByUploadRequestReportFormat",
    "GetSchedulerOptionsByOperationRequestOperationName",
    "HandleSchedulerRunRequestOperation",
]
